'''
自动求导

知乎上看到一个回答，说是自己学习神经网络的时候都是自己对公式求导，
现在常见的DL库都可以自动求导了。这个想必实现过神经网络的同学都有体会，
因为神经网络的back-propagation算法本质上就是求导链式法则的累积，
所以学习这部分的时候就是推来推去，推导对了，那算法你也就掌握了。

粗粗一想，只要能把所有操作用有向图构建出来，通过递归去实现自动求导似乎很简单，
一时兴起写了一些代码，整理成博客记录一下。

http://blog.csdn.net/dark_scope/article/details/62889455
https://github.com/justdark/codeforce_code/tree/master/autoD
'''


# 基础类
class GBaseClass():
    '''
    首先我们需要一个基础类，所有有向图的节点都会有下面两个方法partialGradient()
    是对传入的变量求偏导，返回的同样是一个图。
    expression()是用于将整个式子打印出来
    '''

    def __init__(self, name, value, type):
        self.name = name
        self.type = type
        self.value = value

    def partialGradient(self, partial):
        pass

    def expression(self):
        pass


'''我们主要有三种Class，常量Constant，变量Variable以及算子Operation'''


# 常量
class GConstant(GBaseClass):
    '''我们为常量设置了自增的name，只需要传入value即可定义一个常量。
    而常量对一个变量求导，高中数学告诉我们结果当然是0，
    所以我们返回一个新的常量GConstant(0),
    而它的expression也很简单，就是返回本身的值。'''

    def __init__(self, value):
        global G_STATIC_VARIABLE
        try:
            G_STATIC_VARIABLE['counter'] += 1
        except:
            G_STATIC_VARIABLE.setdefault('counter', 0)
        name = "CONSTANT_" + str(G_STATIC_VARIABLE['counter'])
        type = "CONSTANT"
        super().__init__(name, value, type)

    def partialGradient(self, partial):
        return GConstant(0)

    def expression(self):
        return str(self.value)


# 变量
class GVariable(GBaseClass):
    '''甚至比常量还简单一些，因为是变量，所以它的值可能是不确定的，
    所以构造的时候默认为None，一个变量它对自身的导数是1，
    对其它变量是0，所以我们可以看到在partialGradient()也正是这样操作的。
    变量本身的expression也就是它本身的标识符。'''

    def __init__(self, name, value=None):
        type = "VARIABLE"
        super().__init__(name, value, type)

    def partialGradient(self, partial):
        if partial.name == self.name:
            return GConstant(1)
        return GConstant(0)

    def expression(self):
        return str(self.name)


# Operation
'''紧接着就是大头了,Operation, 例如，
我们将一个变量和一个常量通过二元算子plus连接起来，本身它就构成了一个函数式了。'''


class GOperation(GBaseClass):
    def __init__(self, a, b, operType):
        '''几乎所有计算都是二元的，所以我们可以传入两个算子，
        operType是一个字符串，指示用什么计算项连接两个算子。
        对于特殊的比如exp等单元计算项，可以默认传入的右算子为None.'''
        self.operatorType = operType
        self.left = a
        self.right = b

    '''接下来我们需要求偏导和写expression了。'''

    def partialGradient(self, partial):
        # partial must be a variable
        if partial.type != "VARIABLE":
            return None

        '''回忆一下高中数学，对一个加式（减式）的求导，就是左右两边算子分别求导再相加，
        所以我们在partialGradient就翻译了这个操作而已，
        复杂的事情交给递归去解决，expression同理，更加简单。'''

        if self.operatorType == "plus" or self.operatorType == "minus":
            return GOperationWrapper(self.left.partialGradient(partial), self.right.partialGradient(partial),
                                     self.operatorType)

        '''当然此时我们只有plus这一个计算项，
        肯定无法处理复杂的情况，所以我们添加更多的计算项就可以了'''

        if self.operatorType == "multiple":
            part1 = GOperationWrapper(self.left.partialGradient(partial), self.right, "multiple")
            part2 = GOperationWrapper(self.left, self.right.partialGradient(partial), "multiple")
            return GOperationWrapper(part1, part2, "plus")

        if self.operatorType == "division":
            part1 = GOperationWrapper(self.left.partialGradient(partial), self.right, "multiple")
            part2 = GOperationWrapper(self.left, self.right.partialGradient(partial), "multiple")
            part3 = GOperationWrapper(part1, part2, "minus")
            part4 = GOperationWrapper(self.right, GConstant(2), 'pow')
            part5 = GOperationWrapper(part3, part4, 'division')
            return part5

        # pow should be g^a,a is a constant.
        if self.operatorType == "pow":
            c = GConstant(self.right.value - 1)
            part2 = GOperationWrapper(self.left, c, "pow")
            part3 = GOperationWrapper(self.right, part2, "multiple")
            return GOperationWrapper(self.left.partialGradient(partial), part3, "multiple")

        if self.operatorType == "exp":
            return GOperationWrapper(self.left.partialGradient(partial), self, "multiple")

        if self.operatorType == "ln":
            part1 = GOperationWrapper(GConstant(1), self.left, "division")
            rst = GOperationWrapper(self.left.partialGradient(partial), part1, "multiple")
            return rst

        return None

    def expression(self):
        if self.operatorType == "plus":
            return self.left.expression() + "+" + self.right.expression()

        if self.operatorType == "minus":
            return self.left.expression() + "-" + self.right.expression()

        if self.operatorType == "multiple":
            return "(" + self.left.expression() + ")*(" + self.right.expression() + ")"

        if self.operatorType == "division":
            return "(" + self.left.expression() + ")/(" + self.right.expression() + ")"

        # pow should be x^a,a is a constant.
        if self.operatorType == "pow":
            return "(" + self.left.expression() + ")^(" + self.right.expression() + ")"

        if self.operatorType == "exp":
            return "exp(" + self.left.expression() + ")"

        if self.operatorType == "ln":
            return "ln(" + self.left.expression() + ")"

    def type(self):
        return "OPERATION"


# GOperationWrapper是对GOperation的外层封装
def GOperationWrapper(left, right, operType):
    '''我们打印出来的东西太复杂了，明细有很多地方可以简化，
    比如0*a=0、1*a=a这样的小学知识就可以帮到我们，
    可以明显帮我们简化公式，这个时候就到了我们的GOperationWrapper了，
    加入一些简单的逻辑'''

    if operType == "multiple":
        if left.type == "CONSTANT" and right.type == "CONSTANT":
            return GConstant(left.value * right.value)

        if left.type == "CONSTANT" and left.value == 1:
            return right

        if left.type == "CONSTANT" and left.value == 0:
            return GConstant(0)

        if right.type == "CONSTANT" and right.value == 1:
            return left

        if right.type == "CONSTANT" and right.value == 0:
            return GConstant(0)

    if operType == "plus":
        if left.type == "CONSTANT" and left.value == 0:
            return right

        if right.type == "CONSTANT" and right.value == 0:
            return left

    if operType == "minus":
        if right.type == "CONSTANT" and right.value == 0:
            return left

    '''前面一些优化可以在里面完成，不想优化，直接返回也可以'''
    return GOperation(left, right, operType)


def sigmoid(X):
    a = GConstant(1.0)
    b = GOperationWrapper(GConstant(0), X, 'minus')
    c = GOperationWrapper(b, None, 'exp')
    d = GOperationWrapper(a, c, 'plus')
    rst = GOperationWrapper(a, d, 'division')
    return rst


def main():
    # 验证
    # case 1
    X = GVariable("X")
    y = GVariable("y")
    B = GVariable("B")
    xb = GOperationWrapper(X, B, 'multiple')
    xb_y = GOperationWrapper(xb, y, 'minus')
    f = GOperationWrapper(xb_y, GConstant(2), 'pow')

    print("F:\n\t", f.expression())
    print("F partial gradient of x:\n\t", f.partialGradient(X).expression())

    # case 2
    X = GVariable("X")
    f = sigmoid(X)

    print("F:\n\t", f.expression())
    print("F partial gradient of x:\n\t", f.partialGradient(X).expression())

    # case 3
    x = GVariable("x")
    y = GVariable("y")
    beta = GVariable("beta")
    xb = GOperationWrapper(x, beta, 'multiple')
    s_xb = sigmoid(xb)
    m = GOperationWrapper(s_xb, y, 'minus')
    f = GOperationWrapper(m, GConstant(2), 'pow')

    '''天啦噜!!(╯’ - ‘)╯︵ ┻━┻ ，怎么是这么复杂的一堆，
    如何验证结果是对的呢，你可以把上面的式子拷贝到wolframe alpha上:
    https://www.wolframalpha.com/'''

    print("F:\n\t", f.expression())
    print("F partial gradient of x:\n\t", f.partialGradient(x).expression())



    # print a.partialGradient(x).partialGradient(x).expression()


if __name__ == '__main__':
    G_STATIC_VARIABLE = {}
    main()

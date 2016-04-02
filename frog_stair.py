# https://github.com/taizilongxu/interview_python
# Problem: 台阶问题/斐波纳挈

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

def jump_method(nb_stair):
    fib = lambda n: n if n<2 else fib(n-1)+fib(n-2)
    return fib(nb_stair)

def jump_method_2(nb_stair):
    a, b = 0, 1
    for _ in range(nb_stair):
        b, a = a, a+b
    return a

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
def jump_method_3(n):
    fib = lambda n: n if n<2 else 2*fib(n-1)
    return fib(n)

print(jump_method_3(9))
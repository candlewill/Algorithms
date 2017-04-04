class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_legal(pattern):
    stack = Stack()
    for p in pattern:
        if stack.isEmpty() or ((p, stack.peek()) not in bracket_pairs and (stack.peek(), p) not in bracket_pairs):
            stack.push(p)
        else:
            stack.pop()
    if stack.size() == 0:
        return True
    else:
        return False


bracket_pairs = [('(', ')'), ('[', ']'), ('{', '}')]
test_string = "(){}[()]{[[]}"
print(is_legal(test_string))

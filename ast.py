class Statement:
    pass


class Program:
    def __init__(self, body: list[Statement]):
        self.body = body


class SimpleStatement(Statement):
    pass


class CompoundStatement(Statement):
    pass


class Assign(SimpleStatement):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Name:
    def __init__(self, name):
        self.name = name


class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Statement:
    pass


class Program:
    def __init__(self, body: list[Statement]):
        self.body = body

    def __str__(self):
        return "Program(" + str(self.body) + ")"


class SimpleStatement(Statement):
    pass


class CompoundStatement(Statement):
    pass


class Assign(SimpleStatement):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Assign(" + str(self.left) + ", " + str(self.right) + ")"


class Name:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name(" + str(self.name) + ")"


class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Number(" + str(self.value) + ")"

    def eval(self):
        return int(self.value)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

    def __str__(self):
        return "Sum(" + str(self.left) + ", " + str(self.right) + ")"


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

    def __str__(self):
        return "Sub(" + str(self.left) + ", " + str(self.right) + ")"

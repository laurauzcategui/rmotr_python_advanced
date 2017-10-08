#!/usr/bin/python
# Hint: don't forget the custom exception


class Operation(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.operands = args[0]
        else:
            self.operands = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.operands)


class SubtractOperation(Operation):
    def operate(self):
        value = self.operands[0]
        for i in self.operands[1:]:
            value -= i
        return value


class Calculator(object):
    def __init__(self,operations={}):
        self.op = operations

    def calculate(self,*args):
        if args[-1] not in self.op:
            raise OperationInvalidException
        operation = self.op[args[-1]](args[:-1])
        return operation.operate()

class OperationInvalidException(Exception):
    def __init__(self):
        Exception.__init__(self)

calc = Calculator(operations={'add': AddOperation,'subtract': SubtractOperation})

assert calc.calculate(1, 5, 13, 2, 'add') == 21
assert calc.calculate(13, 3, 7, 'subtract') == 3

op = SubtractOperation(10, 1, 3, 2, 1)
assert op.operate() == 3

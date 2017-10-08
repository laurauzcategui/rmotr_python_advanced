class Calculator(object):

    operations = {
        '+' : lambda x,y : x + y,
        '-' : lambda x,y : x - y,
        '*' : lambda x,y : x * y,
        '/' : lambda x,y : x / y
    }

    #def operation(self,a,b,operate):
    #    return operation(a,b,operate)

    def add(self,a,b):
        return add(a,b,'+')
    def subtract(self,a,b):
        return subtract(a,b,'-')
    def multiply(self,a,b):
        return multiply(a,b,'*')
    def divide(self,a,b):
        return divide(a,b,'/')

    @staticmethod
    def operation(a,b,operate):
        return Calculator.operations[operate](a,b)

    @staticmethod
    def add(a,b):
        return Calculator.operation(a,b,'+')

    @staticmethod
    def subtract(a,b):
        return Calculator.operation(a,b,'-')

    @staticmethod
    def multiply(a,b):
        return Calculator.operation(a,b,'*')

    @staticmethod
    def divide(a,b):
        try:
            return Calculator.operation(a,b,'/')
        except ZeroDivisionError:
            print('Error, You cannot divide by Zero')

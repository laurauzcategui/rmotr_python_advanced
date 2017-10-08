class Calculator(object):

    def __init__(self):
        self.operations = {
            '+' : lambda x,y : x + y,
            '-' : lambda x,y : x - y,
            '*' : lambda x,y : x * y,
            '/' : lambda x,y : x / y
        }

    def operation(self,a,b,operate):
        return self.operations[operate](a,b)

    def add(self,a,b):
        return self.operation(a,b,'+')
    def subtract(self,a,b):
        return self.operation(a,b,'-')
    def multiply(self,a,b):
        return self.operation(a,b,'*')
    def divide(self,a,b):
        try:
            return self.operation(a,b,'/')
        except ZeroDivisionError:
            print('Error, You cannot divide by Zero')

    def 

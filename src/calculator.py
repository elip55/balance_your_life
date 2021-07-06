
# simple calculator
class Calculator:

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def add(self):
        return round(self.val1 + self.val2, 2)
    
    def subtract(self):
        return round(self.val1 - self.val2, 2)

    def multiply(self):
        return round(self.val1*self.val2, 2)
    
    def divide(self):
        return round(self.val1/self.val2, 2)
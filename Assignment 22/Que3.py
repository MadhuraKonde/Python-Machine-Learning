class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
    
    def Accept(self):
        self.value1 = int(input("Enter first number : "))
        self.value2 = int(input("Enter second number : "))
    
    def Addition(self):
        add = self.value1 + self.value2
        return add
    
    def Subtraction(self):
        sub = self.value1 - self.value2
        return sub
    
    def Multiplication(self):
        mul = self.value1 * self.value2
        return mul
    
    def Division(self):
        try :
            div = self.value1 / self.value2
        
        except ZeroDivisionError as zobj:
            print(zobj,"is not allowed !")
            return None
        
        return div

obj1 = Arithmetic()
obj2 = Arithmetic()

obj1.Accept()
print("Addition :",obj1.Addition())
print("Subtraction :",obj1.Subtraction())
print("Multiplication :",obj1.Multiplication())
print("Division :",obj1.Division())

obj2.Accept()
print("Addition :",obj2.Addition())
print("Subtraction :",obj2.Subtraction())
print("Multiplication :",obj2.Multiplication())
print("Division :",obj2.Division())
class Numbers:
    def __init__(self):
        self.Value = int(input("Enter the value : "))
    
    def ChkPrime(self):
        n = self.Value

        for i in range(2,n//2+1):
            if(n % i == 0):
                return False
        
        return True
    
    def ChkPerfect(self):
        n = self.Value

        sum = self.SumFactors()
        sum = sum - n

        if(sum == n):
            return True
        
        return False

    def Factors(self):
        n = self.Value

        for i in range(2,n//2+1):
            if(n % i == 0):
                print(i,end="  ")
        
        print()
    
    def SumFactors(self):
        n = self.Value

        sum = 0
        for i in range(1,n//2+1):
            if(n % i == 0):
                sum = sum + i
        
        sum = sum + n

        return sum

# Object 1   
obj1 = Numbers()

if(obj1.ChkPrime()):
    print(obj1.Value,"is Prime!")
else:
    print(obj1.Value,"is not Prime!")

if(obj1.ChkPerfect()):
    print(obj1.Value,"is Perfect!")
else:
    print(obj1.Value,"is not Perfect!")

print("Factors of ",obj1.Value,end=" : ")
obj1.Factors()

print("Sum of Factors :",obj1.SumFactors())

# Object 2
obj2 = Numbers()

if(obj1.ChkPrime()):
    print(obj2.Value,"is Prime!")
else:
    print(obj2.Value,"is not Prime!")

if(obj2.ChkPerfect()):
    print(obj2.Value,"is Perfect!")
else:
    print(obj2.Value,"is not Perfect!")

print("Factors of ",obj2.Value,end=" : ")
obj2.Factors()

print("Sum of Factors :",obj2.SumFactors())
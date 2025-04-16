class Number:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def addV(self):
        return self.a+self.b
obj=Number(4,5)
print(obj.addV())
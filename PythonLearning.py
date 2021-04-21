
# the only way to access local variable inside a function is to "return" it
class Practise:
    def __init__(self,one,two):
        self.one=one
        self.two=two

    def Check(self):
        a=1
        b=2
        c=3
        
        return a,b


p=Practise(100,200)
val1,val2 = p.Check()
print (val1 , val2)



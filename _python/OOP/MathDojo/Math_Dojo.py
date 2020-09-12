class MathDojo:


    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        splat = 0
        for i in nums:
            splat += i
        self.result += num + splat
        return self
    
    def subtract(self, num, *nums):
        splatvar = 0
        for i in nums:
            splatvar -= i
        self.result -= (num - splatvar)
        return self


# create an instance:
md = MathDojo()

# x = md.add(2).add(2,5,1).subtract(3,2).result
x = md.add(2).result
print(x)


y = md.add(150).add(100,55,45).subtract(30,200).result
print(y)


z = md.add(5).add(5,5,5).subtract(5,5).result
print(z)


# x = md.add(2)
# y = md.add(2,5,1)
# z = md.subtract(3,2,5)




class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y

class MoreCalculator(Calculator):
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num*self.x
        return num

        #return self.x ** self.y

    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            return e
'''
        if self.y ==0:
            return 0
        else:
            return self.x / self.y
'''
cal = MoreCalculator(2,4)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
print(cal.pow())
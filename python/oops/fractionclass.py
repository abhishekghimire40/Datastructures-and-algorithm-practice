#learning oops by creating a fraction class

class Fraction:
    def __init__(self,num=0,den=1):
        if den == 0:
            den == 1
        self.num = num
        self.den = den
    def print(self):
        if self.num == 0:
            print(0)
        elif self.den == 1:
            print(self.num)
        else:
            print(self.num,"/",self.den)
    def simplify(self):
        if self.num == 0:
            return
        current = min(self.num,self.den)
        while current > 1:
            if self.num % current == 0 and self.den % current == 0:
                break
            current -= 1
        self.num = round(self.num // current)
        self.den = round(self.den // current)

    def add(self,new):
        self.num = self.num * new.den + new.num * self.den
        self.den = self.den * new.den
        self.simplify()

    def multiply(self,new):
        self.num = self.num * new.num
        self.den = self.den * new.den
        self.simplify()

f = Fraction(1,7)
f1 = Fraction(1,3)
f.add(f1)
f.simplify()
f.print()   


#maile gareko etro nanathari 
    # def add(self,new):
    #     if self.den == new.den:
    #         self.num = self.num + new.num
    #     elif new.den % self.den == 0:
    #         mul = new.den / self.den
    #         self.num = self.num * mul + new.num
    #         self.den = new.den
    #     elif self.den % new.den == 0:
    #         mul = self.den / new.den
    #         self.num = self.num  + new.num* mul
    #     else:
    #         current = 2
    #         c = True
    #         while c:
    #             if self.den * current == new.den * current:
    #                 c = False
    #                 continue
    #             current +=1
    #         self.num = self.num*current + new.num * current
    #         self.den = self.den * current
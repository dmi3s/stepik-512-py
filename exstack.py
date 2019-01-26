# coding=utf-8
class ExtendedStack(list):
    def sum(self):
        # операция сложения
        r = self.pop()
        r += self.pop()
        self.append(r)

    def sub(self):
        # операция вычитания
        r = self.pop()
        r -= self.pop()
        self.append(r)

    def mul(self):
        # операция умножения
        r = self.pop()
        r *= self.pop()
        self.append(r)

    def div(self):
        # операция целочисленного деления
        r = self.pop()
        r //= self.pop()
        self.append(r)

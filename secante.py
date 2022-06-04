import math

k = 0
erro = 10**(-8)
x_0 = 1
x_1 = 2


def func1(z):
    return ((math.e)**z-2*(math.cos(z)))
    
while abs(func1(x_1))>erro:
    k = k + 1
    x_2 = x_1 - ((func1(x_1))*(x_1-x_0))/((func1(x_1))-(func1(x_0)))
    x_0 = x_1
    x_1 = x_2
   
print(x_1)
print(k)


import math

def func1(z):
    return ((math.e)**(z)-2*math.cos(z))
    
def func1_d(y):
    return (2*math.sin(y)+(math.e)**y)
   
   
k = 0
x_0 = 0
erro = 10**(-8)

while abs(func1(x_0))>erro:
    k = k + 1
    x_k = x_0 - ((func1(x_0))/func1_d(x_0))
    x_0 = x_k
    
print(x_k)
print(k)
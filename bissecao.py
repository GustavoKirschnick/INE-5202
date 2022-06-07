
import math

def func1(x):
    return ((x)**(10)-2)
    
a=0
b=2
k=0
erro = 10**(-10)
x_m=1

while (abs(func1(x_m))>erro):
    k=k+1
    x_m=(a+b)/2
    
    if (((func1(a))*func1(x_m))<0):
        b=x_m
    if (((func1(a))*func1(x_m))>0):
        a=x_m
        
print(k)
print(x_m)
print(func1(x_m))
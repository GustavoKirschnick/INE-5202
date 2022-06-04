import math

def func1(z):
    return ((math.e)**(z)-2*(math.cos(z)))
    
a = -2
b = -1
k = 0
erro = 10**(-8)
x_m = 1

while abs(func1(x_m)) > erro:
    k = k + 1
    if ((func1(a))*(func1(b)) < 0):
        x_m = (a) - ((func1(a))*(b-a))/((func1(b))-(func1(a)))
        
        if (((func1(a))*(func1(x_m))) < 0):
            b = x_m
            
        if (((func1(a))*(func1(x_m))) > 0):
            a = x_m
            
            
print (k)
print (x_m)
print (func1(x_m))
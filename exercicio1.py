import math
def equacao(a,b,c):
    d=(b**2-4*a*c)
    if d < 0:
        return "não exitem raiźes reais"
    x1=(-b+ math.sqrt(d))/(2*a)
    x2=(-b- math.sqrt(d))/(2*a)
    return x1,x2
a=float(input("digite o valor de a:"))
b=float(input("digite o valor de b:"))
c=float(input("digite o valor de c:"))
r= equacao(a,b,c)
print(r)
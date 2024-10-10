def fatorial(g):
    if g<=1:
        return 1
    else:
        return (g*fatorial(g-1))
g = int(input("digite o valor: "))
r=fatorial(g)
print(r)
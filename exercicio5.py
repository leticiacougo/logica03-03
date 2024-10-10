def primo(g):
    if g<2:
        return False
    for i in range (2, g):
        if g%i == 0:
            return True
    return True
g = int(input("digite o valor:"))
resultado = primo(g)
print(resultado)

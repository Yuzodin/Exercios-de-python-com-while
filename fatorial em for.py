from math import factorial
n = int(input ('Digite um numero para calcular o fatorial: '))
c = 0
for c in range(1,n):
    f = factorial(n) 
    c -= 1 
print(f'Aqui esta o resultado do fatorial do numero: {f}')
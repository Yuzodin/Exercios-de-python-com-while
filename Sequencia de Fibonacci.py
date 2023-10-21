print('='* 28)
print('Sequencia de Fibonacci')
print('='* 28)
ter = int(input ('Digite a sequencia de termos de Fibonacci que deseja: '))
t1 = 0
t2 = 1
print('~'* 28)
print(f'{t1} -> {t2}', end= '')
i = 3
while i <= ter:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    i += 1
    print(f'-> {t3}', end= '')

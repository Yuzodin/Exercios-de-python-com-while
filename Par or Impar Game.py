from random import randint
from time import sleep
con = 0
print('=' * 18)
print('Impar ou Par Game')
print('=' * 18)
while True:
    quer = str(input('Deseja impar ou par?:[I/P]: ')).strip().upper()[0]
    while quer not in 'I/P':
        quer = str(input('Ops!! você não escolheu, tente novamente.. Deseja impar ou par?:[I/P]: ')).strip().upper()[0]
    nu = int( input ('Numero da mão para jogar: '))
    print('O computadoe está escolhendo um número...')
    sleep(1)
    cpu = randint(0,10)
    to = (nu+cpu)
    print(f'Você jogou {nu} e o computador jogou {cpu}. O total de {to}')
    print ('Deu Impar..' if to % 2==1 else 'Deu Par..') 
    if quer == 'I':
        if to % 2 == 1:
            print('\033[32mYou Win!\033[m')
            con += 1
        else:
            print('\033[31mYou Lose\033[m')
            break

    elif quer == 'P':
        if to % 2 == 0:
            print('\033[32mYou Win!\033[m')
            con += 1
        else:
            print('\033[31mYou Lose\033[m') 
            break
    print('\033[34mNova rodadda!:\033[m')
print(f'Game Over você ganhou um total de \033[33m{con}\033[m partidas')

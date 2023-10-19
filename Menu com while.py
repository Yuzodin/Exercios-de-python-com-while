from time import sleep
n1 = int(input ('Digite o primeiro valor: '))
n2 = int(input ('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''======= MENU =======
    [1] Soma de numeros
    [2] Multiplicação de numeros
    [3] Maior entre dois numeros
    [4] Novos numeros
    [5] Sair do progama ''')
    opção = int(input('Qual a sua escolha: '))   

    if opção == 1:
        print(f'Aqui está a soma entre os dois: {n1} + {n2} = {n1 +n2}')
    elif opção == 2:
        print(f'Aqui está a multiplicação entre os dois: {n1} x {n2} = {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior valor entre os dois é: {n1}')  
        elif n1 < n2:
            print(f'O maior valor entre os dois é: {n2}') 
        elif n1 == n2:
            print('Não a maior valor entre os dois pois os dois são iguais.')
    elif opção == 4:
        print('Claro! Digite novos valores que deseja:')
        n1 = int(input ('Digite o novo primeiro valor: '))
        n2 = int(input ('Digite o novo segundo valor: '))
    elif opção == 5:
        sleep(2)
        print('OK, fechando o progama!.')
    else:
        print('OPS! opção invalida, tente novamente. ')
        sleep(1)

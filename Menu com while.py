from time import sleep
n1 = int (input('Digite o 1o numero: '))
n2 = int (input ('Digite o 20 numero: '))
op = 0
while op != 5:
    print('''====== MENU ======
          [1] SOMA
          [2] MULTIPLICAÇÃO
          [3] MAIOR NUMERO
          [4] NOVOS NUMEROS
          [5] SAIR DO PROGAMA ''')
    op = int(input ('Digite sua opção: '))
    if op == 1:
        print(f'A soma entre: {n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação entre: {n1} x {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior numero entre os dois foi: {n1}')
        elif n1 < n2:
            print(f'O maior numero entre os dois foi: {n2}')
        elif n1 == n2:
            print('Os dois valores são iguais')    
    elif op == 4:
        print('Digite os novos valores:')
        n1 = int (input('Digite o 1o numero: '))
        n2 = int (input ('Digite o 20 numero: '))
    elif op == 5:
        print('Saindo do progama!!') 
        sleep(2)  
    else:
        print('Opção invalida tente novamnete: ')             
print('Fim do progama!.')    
c = 0
while True:
    nu = int(input ('Deseja visualizar a tabuada de qual numero [Digitarnumeros negativos encerra o progama]: '))
    if nu <0:
        break
    print('=' * 20)
    print(f'Tabuada do numero {nu}')
    print('=' * 20)
    for c in range (0, 11):
        print(f'{nu} x {c} = {nu * c}')
    print('=' * 20)       
print('O progama tabuada foi encerrado com sucesso!!')
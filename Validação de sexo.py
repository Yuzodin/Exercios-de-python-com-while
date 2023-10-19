from time import sleep
sexo = str(input('Digite um  sexo valido. EX:[M/F]: ')).strip().upper()[0]
while sexo not in 'M/F':
    sexo = str(input ('OPS! Sexo digitado inválido. tente novante: ')).strip().upper()[0]
    sleep(1)
if sexo in 'Mm':
    print('Tudo certo, sexo Masculino registrado com sucesso!')
elif sexo in 'Ff':
    print('Tudo certo, sexo Feminino registrado com sucesso!')   
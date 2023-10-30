c = 0
so = me = mai = men = 0
n = int(input ('Digite um numero: '))
c += 1
so += n
if c == 1:
    mai = men = n
else:
    if n > mai:
        mai = n
    if n < men:
        men = n
m = str(input ('Quer continuar?:[S/N]: ')).strip().upper()[0]
while m not in 'Nn':
    n = int(input ('Digite um numero: '))
    c += 1
    so += n
    if c == 1:
        mai = men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n
    m = str(input ('Quer continuar?:[S/N]: ')).strip().upper()[0]
print('End..')    
me = (so/c)
print(f'Você digitou {c} numeros e a media entre eles foi de {me:.2}')   
print(f'Dos numeros digitados o maior foi {mai} e o menor foi {men}') 
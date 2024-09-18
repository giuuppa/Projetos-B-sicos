#Giusepp de Couto Barros Júnior

print('Olá, esta é a sequencia de fibanacci. Esta sequencia funciona através de termos')
n=int(input('Digite quantos termos você quer mostrar: '))

t1=0
t2=1

soma= t1+t2

print( '{} - {}' .format(t1,t2), end='')
contador=3

while contador <= n:
    t3=t1+t2
    soma += t3

    print( ' - {}'.format(t3), end='')
    t1=t2
    t2=t3
    contador +=1

print(' - A soma dos termos até {} é {}'.format(n,soma))
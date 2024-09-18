#Giusepp de Couto Barros Júnior

texto = input("Digite uma string: ")

quantidade_a = texto.lower().count('a')

if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
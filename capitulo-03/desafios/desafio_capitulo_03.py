# Desafio 3 
#
#       1. Exiba três diferentes


print ("Batman")
print ("Homem-Aranha")
print ("Void")


#       2. Escreva um programa que exiba uma mensagem se uma variável for menor do que 10 
#               e outra mensagem se a variável for maior ou igual a 10.

number1 = 10 

if number1 < 10:
    print("Número é menor que 10")

else:
    print ("Número é maior ou igual a 10") 

#       3. "Escreva um programa que exiba uma mensagem se uma variável for menor ou igual a 10, 
#           outra mensagem se a variável for maior do que 10, mas menor ou igual a 25, 
#               e ainda outra mensagem se a variável for maior do que 25."

numero_qualquer = 7

if numero_qualquer <= 10:
    print ("O número é menor ou igual a 10")

elif numero_qualquer <= 25:
    print ("O número é maior que 10 e menor ou igual a 25")

else:
    print ("O número é maior que 25") 


#
#       4. Crie um programa que divida duas variáveis e exiba o resto
#

dividendo = 10
divisor = 2.5

resto = 10 % 2.5
print (resto)

#
#       5. Crie um programa que receba duas variáveis, as divida, e exiba o quociente.
#

numerador = 7
denominador = 2

quociente = 7/2
print (quociente)

#
#       6. Escreva um programa com a variável age (idade) que receba um inteiro 
#           e exiba string diferentes dependendo de que inteiro age receber
#

age = 19

if age <= 17:
    print ("Você é uma pessoa nova!")

elif age <= 50:
    print ("Parabéns,se tornou adulto!")

else:
    print ("Já está na velha vanguarda.")
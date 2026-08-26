# Instrução Condicional
#           - Tomada de decisões
#                   - Baseado: True e False
#
#           - Controla o fluxo 
#                   - True
#                       - Executa -> bloco de código
#
#                   - False 
#                       - Esquece -> Pula pro próximo
#
#           - Programa
#               - Executa -> certos blocos de códigos
#                       - Depedendo da condição
#       
#           - Condições
#               - If (Se)
#                   - 1° Condição -> Programa irá testar
#                      
#               - Elif (Se não, se)
#                   - Testa -> nova condição
#                       - Caso a condição anterior falhar
#
#               - Else (Senão)
#                   - Quando só resta essa condição por último
#
#
#           Exemplo:.
#
#               | n°1  (Explicação)  
#         
#                   // Armazena o valor -> variável -> Mensagem
#                   Mensagem = "Hi!"   
#
#                   // If = Se // Caso a variável "Mensagem" tenha o valor "Hi!" // Execute o bloco de código abaixo -> print ("Hello!")
#                   if Mensagem == "Hi!":
#                       print ("Hello!")
#
#                   // Else = Senão // Caso todos os outras condições (if, elif) -> não forem // Programa executará por último isso
#                   else:                 
#                       print ("Twitter!")
#
#               | n°2  (If -> True)
#               
#                   home = "Barzil"
#                   
#                   if home == "Barzil":
#                       print ("Hello Barzil")
#
#                   else: 
#                       print ("Hello World")
#
#                           // Hello Barzil
#                   
#               | n°3 (If -> False)
#               
#                   home = "Barzil"
#               
#                   if home == "Australia": 
#                       print ("Hello Australia")
#
#                   else: 
#                       print ("Hello World")
#
#                           // Hello World
#
#               | n°4 (If solitário)
#           
#                   home = "Barzil"
#
#                   if home == "Barzil":
#                       print ("Bostileiros")
#           
#                          // Bostileiros
#   
#               | n°5 (If -> sequência)
#       
#                   z = 2
#
#                   if z == 2: 
#                       print ("O número é 2.")
#                           // True -> aparecerá na tela
#
#                   if x % 2 == 0: 
#                       print ("O número é par.")
#                           // True -> aparecerá na tela
#
#                   if x % 2 != 0 
#                       print ("O núnmero é ímpar.")                       
#                           // False -> não aparecerá na tela
#
#               | n°6 (If -> Aninhado)
#                   
#                   a = 10
#                   b = 15
#
#                   if a == 10:
#                       if b == 15:
#                           print(a + b)
#
#                           // 25 (resultado)
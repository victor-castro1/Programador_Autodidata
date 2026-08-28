# Erro & Exceção
#       - Situações -> impede -> programa executar 
#
#     Visão Geral
#       - Código Fonte -> Análise
#       
#       - 1° Análise 
#           - Existe algum problema?
#               - Sim? -> Sintaxe
#               - Não 
#                   - Etapa de Execução
#
#       - 2° Execução
#           - Existe algum problema?
#               - Sim? -> Exceção
#               - Não 
#                   - Resultado Normal
#    |------------------------------------------------------|
#       
#   1. Erros de Sintaxe
#       - Regras da linguagem -> não são seguidas
#          
#       Ex:.
#           print ("Olá Mundo!) 
#               SyntaxError (")
#
#           if idade >= 18           
#               print ("Maior de idade")
#                   SyntaxError (:)
#
#
#   2. Erros de exceção
#       - Programa -> roda normalmente
#       - Entretanto -> algo inesperado surge
#
#       1. Ex:.
#           a = 90
#           b = 0
#
#           resultado = a / b
#
#           - Observação:
#               - Sintaxe CORRETA
#               - Problema -> Não é possível dividir por ZERO
#               - "ZeroDivisionError"
#
#      2. Ex:.
#           print (nome)
#
#           - Observação
#               - Sintaxe Correta
#               - Problema -> Existe variável nome? 
#                       Não existe -> não foi declarada
#
#               - "NameError"
#
#   | -------------------------------------------------------------- |        
#
#   Solução:
#
#       - Quando encontrar os erros
#               - Vá até a linha -> problema
#               - Examine-a 
#               - Ache a solução
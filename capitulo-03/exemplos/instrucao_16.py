#   Instrução
#       - Um Comando/ordem -> compilador -> executa 
#
#       Ex:.
#           print ("Hello World!!")
#
#       1. Instrução Simples    
#           - Única -> Linha de código
#
#           Ex:.
#
#               print ("Hello, Carlos!")                            # Executa diretamente 
#   
#               print (2+2)                                         # Pode ocupar -> única linha 
#
#               x = 10                                              
#               print (x)        
#   
#
#       2. Instrução Composta
#           - Formada -> uma ou + cláusulas
#
#           - Linhas de código
#                   - Estrutura de controle -> agrupa outras intruções
#               
#           - Estrutura 
#                   - Cabeçalho/-> Define o tipo de controlador (if, try, for...)
#                   - Bloco de código -> pertecente ao cabeçalho
#               
#           - Cláusula
#                   - Cabeçalho + Bloco de código (indentado)
#
#                   Ex:.
#                       Cabeçalho
#                           conjunto de instruções
#
#                       Cabeçalho
#                           instrução 1 
#                           instrução 2 
#                           instrução 3 
#                           instrução 4
#
#            Ex:.
#
#                   # Instrução Composta -> Contexto Idade
#
#                   # Cláusula (if + bloco de código)
#                   if idade >= 18                                      # Cabeçalho (define a regra / tipo de controle) -> If (Condição)
#                       print ("Parabéns você é maior de idade")        # Bloco de código -> pertence ao cabeçalho IF (por causa da sua indentação) 
#
#                   
#
#                   # Instrução Composta -> Contexto de Notas
#
#                   nota = 8
#
#                   if nota >= 9:                                       # Cláusula 1 -> if 
#                       print ("Excelente Desempenho!")                     # Conjunto de instruções -> dentro da Cláusula 1 
#
#                   elif nota >= 6:                                     # Cláusula 2 -> elif
#                       print ("Aprovado!")                                 # Conjunto de instruções -> dentro da Cláusula 2 
#
#                   else                                                # Cláusula 3 -> else
#                       print ("Reprovado!")                                # Conjunto de instruções -> dentro da Cláusula 3                                
#
#                   
#                   # Instrução Composta -> Contexto de acesso
#                                 
#                   if usuario_logado:   
# 
#                       # Conjunto de instruções 
#                       print ("Bem-Vindo")                             # Instrução n°1                       
#                       carregar_painel()                               # Instrução n°2 
#                       mostrar_notificacoes()                          # Instrução n°3
#
# Crie um programa que leia o ano de nascimento 
# de sete pessoas .No final, mostre quantas 
# pessoas ainda não atingiram a maioridade e 
# quantas já são maiores
from datetime import date
atual = date.today().year
soma = 0
me = 0
ma = 0
for x in range(1 , 8):
    print("---------{} PESSOA-------------".format(x))
    a = int(input("DIGITE O ANO DO SEU NASCIMENTO "))
    ano = atual - a
    if ano <= 17:
        me = me + 1
    else:
        print()    
    if ano >= 18:
        ma = ma + 1
    else:
        print()        
print("TEMOS {} PESSOAS QUE ATIGIRAM A MAIORIDADE ".format(ma)) 
print("TEMOS {} PESSOAS QUE NÃO ATIGIRAM A MAIORIDADE ".format(me))



    

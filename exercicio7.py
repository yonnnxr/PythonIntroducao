nome = input("Nome do vendedor: ")
sala = float(input("Qual o seu salario fixo: "))
quan = float(input("Qual o valor total de vendas voce fez: "))
tota = quan * 0.15
totb = sala + tota

print(f"Olá,{nome}")
print(f"Seu salario fixo é {sala}")
print(f"O seu salario final é {totb}")
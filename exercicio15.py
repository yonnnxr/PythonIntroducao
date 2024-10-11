custo = float(input("Insira o valor do produto: "))
perce = float(input("Qual a porcentagem de aumento: "))
total = (custo*perce) / 100
tot1 = custo + total
print(f"O Valor do produto é {custo} ")
print(f"O percentual é {perce}")
print(f"O valor de venda é {tot1}")
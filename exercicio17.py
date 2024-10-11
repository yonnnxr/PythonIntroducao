pao = int(input("Quantos pães foram vendidos? "))
bro = int(input("Quantas Broas foram vendidas? "))
totb = bro * 1.50
totp = pao * 0.12
total = totb + totp
conta = total * 0.10

print(f"O valor total de vendas foi {total}")
print(f"O valor a ser guardado será {conta}")

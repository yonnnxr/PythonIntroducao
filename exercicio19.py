lit = float(input("Quantos Km foram percorridos: "))
ped = float(input("Quantos Pedagios foram passados: "))
totl = lit / 15
gastol = totl * 5.30
totp = ped * 8
total = gastol + totp
print(f"O Valor gasto foi de {total}")
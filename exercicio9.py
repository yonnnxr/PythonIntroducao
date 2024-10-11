nome = input("Qual o seu nome? ")
nota1 = float(input("Qual a sua primeira nota: "))
nota2 = float(input("Qual a sua segunda nota: "))
nota3 = float(input("Qual a sua terceira nota: "))
Pes1 = 1 
Pes2 = 2 
Pes3 = 3 
media = (nota1*Pes1 + nota2*Pes2 + nota3*Pes3) / (Pes1+Pes2+Pes3)
mediaround = round(media, 1)
print(f"Olá,{nome}")
print(f"A sua média ponderada é: {media}")
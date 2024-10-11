nome = input("Qual é o seu nome: ")
nota1 = float(input("Qual foi a sua primeira nota: "))
nota2 = float(input("Qual foi a sua segunda nota: "))
nota3 = float(input("Qual foi a sua terceira nota: "))
total = nota1 + nota2 + nota3
print(f"Olá,{nome}")
print(f"As suas 3 notas foram: {nota1},{nota2},{nota3}")
print(f"A sua média é: {total}")
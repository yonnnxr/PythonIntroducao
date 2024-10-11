area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
area_com_folga = area * 1.1
litros_necessarios = area_com_folga / 6
latas_necessarias = int(litros_necessarios // 18) 
if litros_necessarios % 18 != 0:
    latas_necessarias += 1
custo_latas = latas_necessarias * 80
galoes_necessarios = int(litros_necessarios // 3.6)
if litros_necessarios % 3.6 != 0:
    galoes_necessarios += 1
custo_galoes = galoes_necessarios * 25
latas_mistura = int(litros_necessarios // 18)
litros_restantes = litros_necessarios - (latas_mistura * 18)
galoes_mistura = int(litros_restantes // 3.6)
if litros_restantes % 3.6 != 0:
    galoes_mistura += 1
custo_mistura = (latas_mistura * 80) + (galoes_mistura * 25)
print("\nOpções de compra:")
print(f"A) {latas_necessarias} latas - R$ {custo_latas:.2f}")
print(f"B) {galoes_necessarios} galões - R$ {custo_galoes:.2f}")
print(f"C) {latas_mistura} latas e {galoes_mistura} galões - R$ {custo_mistura:.2f}")
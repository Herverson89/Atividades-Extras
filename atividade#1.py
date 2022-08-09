valorAplicado = float(input('digite o valor aplicado: '))
juros = float(input("digite a taxa de juros do mes: "))

meses = 0

while meses < 12:
    valorAplicado += valorAplicado * juros / 100
    meses += 1
    print(f"o mes {meses}, seu rendimento foi de R$:{valorAplicado:.2f}.")
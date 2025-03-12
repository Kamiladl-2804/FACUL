dias = int(input("quantos dias?"))
horas = int (input ("quantas horas?"))
minutos = int (input("quantos minutos?"))
segundos =int (input ("quantos segundos?"))
total =(dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"total de segundos é de {total:.2f}")
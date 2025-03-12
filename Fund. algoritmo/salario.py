valorHoras = float (input("quantas horas de trabalho?"))
horasTrab = int (input("quantas horas trabalhadas?"))

salariobruto = valorHoras * horasTrab
IR = salariobruto * (11/100)
INSS = salariobruto *(8/100)
Sindicato = salariobruto * (5/100)
salarioliquido = salariobruto -IR - INSS - Sindicato

print()
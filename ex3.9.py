#Exercício 3.9
dias = int(input("Digite o número de dias"))
horas = int(input("Digite o número de horas"))
minutos = int(input("Digite o número de minutos"))
segundos = int(input("Digite o número de segundos"))
#igualando a ordem de grandeza das variáveis
df = dias*86400
hf = horas*3600
mf = minutos*60
soma = (df+hf+mf+segundos)
print("O total de segundo dado é de:", soma, "segundos")

from datetime import datetime

hoje = datetime.now()

if(len(str(hoje.day)) == 2):
    dia = hoje.day

else:
    dia = "0" + str(hoje.day)

if(len(str(hoje.month)) == 2):
    mes = hoje.month

else:
    mes = "0" + str(hoje.month)


ano = hoje.year

print(dia)

print(mes)

print(ano)
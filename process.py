import csv 
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter

arq = open('TESTE.csv', 'r')
reader = csv.reader(arq)
names = list()

for line in reader:
    for word in line:
        x = word.split(';')
        y = x[4].strip('"')
        if y.upper() != 'NOME':
            names.append(y)

wb = load_workbook('Rotulo.xlsx')
ws = wb['Envolope']
positions = ['C5', 'H5', 'C12', 'H12', 'C19', 'H19', 'C26', 'H26', 'C33', 'H33']

y = 0
for i in range(0, int(len(names)), 1):
    
    if y == 10:
        y = 0
        string = 'perfil' + str(i) + '.xlsx' 
        wb.save(string)
    
    print(y, i)
    ws[positions[y]] = names[i] 
    
    y+=1

string = 'perfil' + str(i) + '.xlsx' 
wb.save(string)
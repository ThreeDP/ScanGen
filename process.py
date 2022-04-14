from createTable import create_table
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter

wb = load_workbook('Rotulo.xlsx')
ws = wb['Envolope']
count = 0

n = 0

table = create_table()

def te(n, table):
    print(n)
    positions = ['C5', 'H5', 'C12', 'H12', 'C19', 'H19', 'C26', 'H26', 'C33', 'H33']
    for p in positions:
        try:
            ws[p] = table[n]
            n+= 1
        except:
            print('erro')
            break

    string = 'Clientes' + str(n) + '.xlsx'
    wb.save(string)
    return n


while count <= len(table):
    n = te(n, table)
    
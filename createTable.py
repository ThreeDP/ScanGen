from catchCsv import catch_csv
from manageFiles import find_files

path = "./Arquivos/"

def create_table():
    files = find_files(path)
    table = list()

    for file in files:
        pathfile = path + file
        data = catch_csv(pathfile)

        y = data[0].replace('"', '') # Elimina as aspas da string (Cabeçalho)
        header = y.split(';') # Divide a string em um array (Cabeçalho)
        for line in range(1, len(data), 1):
            x = data[line].replace('"', '')
            words = x.split(';')
            
            row = dict().fromkeys(header, '') # Cria um dicionario vazio.

            for column_index in range(0, len(header) - 1, 1): # Pula o cabeçalho e realiza o laço de inserção de dados.
                    row[header[column_index]] = words[column_index] # Preenche o dicionário criado com os dados

            for i in row.values(): # Valida se a row está vazia antes de inserir.
                if i != '':
                    table.append(row)
                    break
        
    return table
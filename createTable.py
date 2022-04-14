from catchCsv import catch_csv
from manageFiles import find_files

path = "./Arquivos/"

def create_table():
    files = find_files(path)
    table = list()

    for file in files:
        pathfile = path + file
        data = catch_csv(pathfile)

        y = data[0].replace('"', '')
        header = y.split(';')
        for line in range(1, len(data) - 1, 1):
            x = data[line].replace('"', '')
            words = x.split(';')
            
            row = dict().fromkeys(header, '')

            for w in range(1, len(header) - 1, 1):
                row[header[w]] = words[w]
            
            table.append(row)
        
    return table
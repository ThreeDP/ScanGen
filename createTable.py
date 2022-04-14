from catchCsv import catch_csv

def create_table():
    #files = [str(x) for x in input().split(" ")]
    files = ['Arq01.csv', 'Arq02.csv']
    table = list()

    for file in files:
        data = catch_csv(file)

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
import csv 

files = [str(x) for x in input().split(" ")]
table = list()

#for file in files:
arq = open('Arq01.csv', 'r')
reader = csv.reader(arq)

data = list()
for objectcsv in reader:
    for i in objectcsv:
        data.append(i)


y = data[0].replace('"', '')
header = y.split(';')
for line in range(1, len(data) - 1, 1):
    x = data[line].replace('"', '')
    words = x.split(';')
    
    row = dict().fromkeys(header, '')

    for w in range(1, len(header) - 1, 1):
        row[header[w]] = words[w]
    
    table.append(row)
    
print(table[0])
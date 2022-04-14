import csv 

def catch_csv(file):
    with open(file) as arq:
        reader = csv.reader(arq, delimiter='\t')

        data = list()
        for objectcsv in reader:
            for i in objectcsv:
                data.append(i)
        
        arq.close()
        return data
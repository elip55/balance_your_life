import csv

def gather_all():
    with open('reference.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

k = gather_all()

v = []
a = []
g = []
for i in range(len(k)):
    v.append(k[i][0])
    a.append(float(k[i][1]))
    g.append(float(k[i][2]))
j = [a,g]

# v = accounts starting with checking
# j = [[balances],[min payment]]
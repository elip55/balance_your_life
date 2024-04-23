import csv
def gather_all():
    with open("reference.csv", 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    header = []
    balances = []
    min_payments = []
    for i in range(len(data)):
        data[i][1] = float(data[i][1])
        data[i][2] = float(data[i][2])
        header.append(data[i][0])
        balances.append(data[i][1])
        min_payments.append(data[i][2])
    j = [balances,min_payments]
    return header,j

v,j = gather_all()
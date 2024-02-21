import csv

def gather_all():
    rows = []
    with open("reference.csv", 'r') as file:
        header_reader = csv.reader(file)
        header = next(header_reader) # header is the name of the accounts
        rowboat = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in rowboat:
            rows.append(row) # rows import data as floats using quote_nonnumeric
    return header, rows

v,j = gather_all()

print(v,j)
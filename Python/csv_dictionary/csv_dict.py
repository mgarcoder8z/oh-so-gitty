import csv

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = 'r\n',
    quoting = csv.QUOTE_MINIMAL)

with open('us-500.csv', 'rb') as f:
    dictofdata = csv.DictReader(f, dialect='mydialect')
    for row in dictofdata:
        print(row['first_name']+" "+row['last_name'])
        print(row['first_name'])+"\n"+(row['last_name'])
        print(row['company_name'])+"\n"+(row['address'])
        print(row['city'])+"\n"+(row['county'])
        print(row['state'])+"\n"+(row['zip'])
        print(row['phone1'])+"\n"+(row['phone2'])
        print(row['email'])+"\n"+(row['web'])+"\n"+("-"*50)

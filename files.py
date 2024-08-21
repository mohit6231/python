import csv

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'name'])
    writer.writerow([1, 'mohit'])
    writer.writerow([2, 'demo'])

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

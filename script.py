import csv

with open('tpc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'<li class="list-group-item"> {row[0]}, {row[1]} </li>')
            line_count += 1
    print(f'Processed {line_count} lines.')
import csv

def save(d):
    f = open('students.csv', 'w', newline='')
    writer = csv.writer(f)
    for surname in d:
        writer.writerow([surname, d[surname]])
    f.close()

def read():
    f = open('students.csv', 'r', newline='')
    reader = csv.reader(f)
    for row in reader:
        print(row[0], ':', row[1])
    f.close()

students = {'Іваненко': 2005, 'Петренко': 2004, 'Сидоренко': 2006}

save(students)
read()

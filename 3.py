import csv

with open('products.csv', encoding='utf-8-sig', newline='\n') as f:
    r = list(csv.reader(f, delimiter=';'))
    head = r[0]
    lst = r[1:]

inp = input()
while inp != 'молоко':
    mn = 10000
    pr = ''
    for line in lst:
        if line[0] == inp:
            if float(line[-1]) < mn:
                mn = float(line[-1])
                pr = line[1]
    if pr:
        print(f'В категории: {inp} товар: {pr} был куплен {mn} раз')
    else:
        print('Такой категории не существует в нашей БД')
    inp = input()



import csv

with open('products.csv', encoding='utf-8-sig') as f:
    r = list(csv.reader(f, delimiter=';'))
    head = r[0]
    lst = r[1:]
    cnt = 0
    with open('products_new.csv', 'w', encoding='utf-8-sig') as fo:
        w = csv.writer(fo, delimiter=';')
        w.writerow(head)
        for line in lst:
            line.append(str(float(line[-1]) * float(line[-2])))
            w.writerow(line)
            if line[0] == 'Закуски':
                cnt += float(line[-1])
    print(cnt)


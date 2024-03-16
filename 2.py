import csv


def sorting(lst_):
    """Сортировка вставками

    lst - список, к которому будет применяться сортировка
    """
    n = len(lst_)
    for i in range(1, n):
        x = lst_[i]
        j = i

        while j > 0 and lst_[j - 1] > x:
            lst_[j] = lst_[j - 1]
            j -= 1

        lst_[j] = x


with open('products.csv', encoding='utf-8-sig', newline='\n') as f:
    r = list(csv.reader(f, delimiter=';'))
    head = r[0]
    lst = r[1:]

    sorting(lst)
    cat = lst[0][0]

    mx = 0
    pr = ''
    with open('products.csv', 'w', encoding='utf-8-sig') as fo:
        w = csv.writer(fo, delimiter=';', lineterminator='\n')
        w.writerow(head)
        for line in lst:
            w.writerow(line)
            # поиск самого дорогого товара
            if line[0] == cat:
                if float(line[-2]) > mx:
                    mx = float(line[-2])
                    pr = line[1]
    print(f'В категории: {cat} самый дорогой товар: {pr} его цена за единицу товара составляет {int(mx)}')


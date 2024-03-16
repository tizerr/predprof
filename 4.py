import csv


def promo(info):
    """Функция для генерации промокодов к товарам

    info - список с информацией о товаре
    """
    cat, name, date, price, count = info
    day, month, year = date.split('.')
    promocode = name[:2] + day + name[-1:-3:-1] + month[::-1]
    return promocode.upper()


with open('products.csv', encoding='utf-8-sig', newline='\n') as f:
    r = list(csv.reader(f, delimiter=';'))
    head = r[0]
    lst = r[1:]

    promos = [promo(i) for i in lst]

    head.append('promocode')
    # добавление к строкам списка столбца с промокодом
    lst = [line + [promo] for line, promo in zip(lst, promos)]

    with open('product_promo.csv', 'w', encoding='utf-8-sig') as fo:
        w = csv.writer(fo, delimiter=';', lineterminator='\n')
        w.writerow(head)
        w.writerows(lst)

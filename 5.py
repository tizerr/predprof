import csv
from hashlib import sha3_256


def gen_hash(cat_):
    """Функция для генерации хэша товара

    cat_ - категория товаров
    """
    return sha3_256(bytes(cat_, encoding='utf8')).hexdigest()


with open('products.csv', encoding='utf-8-sig', newline='\n') as f:
    r = list(csv.reader(f, delimiter=';'))
    head = r[0]
    lst = r[1:]

    cnts = {}
    # распределение товаров по категориям (категория, количество)
    for line in lst:
        cat = line[0]
        cnts[cat] = cnts.get(cat, 0) + float(line[-1])

    # составление хэш-таблицы
    hash_table = {gen_hash(k): v for k, v in cnts.items()}
    for k in sorted(hash_table, key=lambda x: hash_table[x])[:10]:
        print(k, hash_table[k])



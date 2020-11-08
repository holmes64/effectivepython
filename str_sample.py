## Chapter1
from urllib.parse import parse_qs

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(green_str[0])
    else:
        return default


def bubble_sort(a):
    # アンパック構文を使用してスマートにスワップを行う
    for _ in range(len(a)):
         for i in range(1, len(a)):
             if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1] # sawp


print('[effective python term3: difference between str and bytes]')
print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))


# Cスタイルフォーマット文字列とstr.formatは使わずf文字列で埋め込む

## C style format
a = 0b10111011
b = 0xc5f
print('Binary is %d hex is %d' % (a, b))

pantry = [
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
]
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s - %.2f' % (i, item, count))


key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value} # 元の状態

reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key # スワップした状態
}

assert old_way == new_way == reordered

print('\n')


## best method is follows
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count))

    new_style = '#{}: {:<10s} = {}'.format(
        i+1,
        item.title(),
        round(count))

    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'

    assert old_style == new_style == f_string
    print(f_string)


## use helper function than difficult one liner
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
green = get_first_int(my_values, 'green')

item = ('Peanuut butter', 'Jelly')
first, second = item

print(first, 'and', second)


## term6: not index use multiple substitute unpack
# pythonicなやり方ではfor文でインデックスを使用しない
names = ['carrots', 'bacon', 'arugula', 'pretzels']
bubble_sort(names)
print(names)


## term7: use enumerate rather than range
# enumerateの簡潔な構文で、イテレータでループしながら、要素のインデックスを取り出せる
# rangeでループして、シーケンスのインデックスを処理するよりも、enumerateを使うほうが良い
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list):
    print(f'{i+1}: {flavor}')


## term8: use zip when process iteraors parallel
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
max_count = 0
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_letters = count


## term13: use catch-all unpack rather than slice
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)


car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}


((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')


## item14: key引数を使い複雑な基準でソートする













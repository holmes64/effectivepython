# item14
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case Sentitive: ', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive:', places)


# item15
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


my_func(goose='gosling', kangaroo='joey')

# ダックタイピング Pythonは性的片付けではないため、ほとんどのコードは厳格なtクラス階層に基づく代わりに
# オブジェクトの振る舞いがデファクトの型に基づくダックタイピングに依存します。





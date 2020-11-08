
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

'''
    ジェネレータ関数は、呼び出されると実際の作業をせずに、直ちにイテレータを返す。
    組み込み関数nextが呼び出されるごとに、イテレータはジェネレータを次のyield式に1つすすめる。
'''
address = 'Four score and seven years ago...'
it = index_words_iter(address)
print(next(it))
print(next(it))

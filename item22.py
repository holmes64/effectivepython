
# こっちだと、値がないときに空のリストを渡さなければいけなくなる
def log_original(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{message}: {values_str}')


# こっちのほうがbetter
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers are', 1, 2)
log('Hi there')  # ずっと良い

'''
    アンパック代入文で値を渡すことも可能.
    Problems:
        可変個数の引数が、関数に渡される前に常にタプルに変換されている
        つまり、関数の呼び出し元がジェネレータで＊演算子を使用していれば終わるまでイテレーションされる。
        結果のタプルにはすべての値が含まれるのでメモリを大量に消費して、プログラムをクラッシュさせる危険あり
        argsを受け入れる関数は、引数リストの入力個数が少ないことがをわかっている場合が一番適している。
'''
favorites = [7, 33, 99]
log('favorite colost', *favorites)

'''
    すべての呼び出し元を修正せずには関数に対して新たな位置引数を追加できない
    Solution：
        キーワード専用引数を使う。 items25
        型ヒントを使う items90　
'''

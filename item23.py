
def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6
# すべて等価
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 位置引数は、キーワード引数より前の位置で指定しなければ行けない。
# remainder(number=20, 7) # これはNG

my_kwargs = {
    'number': 20,
    'divisor': 7,
}
assert remainder(**my_kwargs) == 6

# 関数呼び出しでは、重複がない限り、**演算子を位置引数またはキーワード引数と混在させることができる。
my_kwargs2 = {
    'divisor': 7,
}
assert remainder(number=20, **my_kwargs2) == 6

# 重複がなければ何個も使用可能
my_kwargs3 = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}
assert remainder(**my_kwargs3, **other_kwargs) == 6

'''
    キーワード引数のもたらす利点３つ
        1. 関数呼び出しを初めて読む人にとってわかりやすくなる
        2. 関数定義においてデフォルト値を持てる。
        3. 既存の呼び出し元と後方互換性を保ちながら、関数の引数を拡張できる
'''


# 2.
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period


flow_rate(0.5, 3)
flow_rate(0.5, 3, period=3600)

'''
    #3の問題点は、キーワード引数を位置引数としても使用できてしまうこと。
    オプションの引数は、キーワード名を使って指定し、位置引数を使わないことが一番良い方法です。
'''

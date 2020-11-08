
# イテレータを使えるところならどこでも使える。

# 一番汚い例
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)


# list内包表記
squares2 = [x**2 for x in a]
print(squares2)


# mapを使用する場合
alt = map(lambda x: x ** 2, a)
print(list(alt))

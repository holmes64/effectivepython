
# 普通のリスト内包表記
value = [x for x in [100, 57, 15, 1, 12, 75, 5, 86, 89, 11]]
print(value)

# ジェネレータ式
it = (x for x in [100, 57, 15, 1, 12, 75, 5, 86, 89, 11])
print(it)
print(next(it))
print(next(it))

roots = ((x, x ** 0.5) for x in it)
print(next(roots))

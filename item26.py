from functools import wraps
import pickle

'''
    例えば、関数呼び出しの引数と戻り値を出力したい場合、再帰関数で
    関数呼び出しの入れ子になったスタックをデバッグするときに特に有用です。
    !r はreprの略
    !s はstr
    !a はascii
'''
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f'->{result}')
        return result
    return wrapper


@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

# ＠記号は、デコレータがラップする関数を引数として呼び出して、戻り値を同じスコープのもともとの名前に代入することと等価
# fibonacci = trace(fibonacci)

fibonacci(4)

'''
    functoolsのwrapsヘルパー関数を使用する。
    これは、デコレータを書くのを助けるデコレータ
    適用すると、内部関数についてのすべての重要なメタデータが外部関数に複製される.
'''

def trace2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f'->{result}')
        return result
    return wrapper


@trace2
def fibonacci2(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


help(fibonacci2)
print(pickle.dumps(fibonacci2))

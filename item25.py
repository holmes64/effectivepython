
'''
    以下のコードの問題は、2つのブール値引き数の位置を混同しやすいことです。
'''
def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)

result = safe_division(1.0, 0, False, True)
print(result)


'''
    位置専用引数として、2つの必須引数を定義する.
'''
def safe_division2(number, divisor, /, *,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


assert safe_division2(2, 5) == 0.4


'''
    キーワード専用引数と位置専用引数の重要な結論は、引数リストの記号/と*の間にある引数名は位置またはキーワードで渡される
'''
def safe_division3(numerator, denominator, /, ndigits=10, *,
                   ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division3(22, 7)
print(result)

result = safe_division3(22, 7, 5)
print(result)

result = safe_division3(22, 7, ndigits=2)
print(result)


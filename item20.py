
def careful_divide(a: float, b: float) -> float:
    """Divides a by b

    Raises:
        ValueError: When th inputs cannot be invalid.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('Invalid inputs')


x, y = 5, 0
ans = careful_divide(x, y)
print(ans)

x, y = 5, 2
ans = careful_divide(x, y)
print(ans)

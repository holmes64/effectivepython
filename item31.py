from collections.abc import Iterator

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percentages)
    return result


path = 'my_numbers.txt'
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0


def normalize_defensive(numbers):
    if iter(numbers) is numbers: # イテレータ　良くない
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


# normalize_defensiveをチェックするための別の方法
def normalize_defensive2(numbers):
    if isinstance(numbers, Iterator): # チェックする別の方法
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
normalize_defensive2(visits)
assert sum(percentages) == 100.0



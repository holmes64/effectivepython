

# example1
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_stats(lengths)

print(f'Min: {minimum}, Max: {maximum}')


# example2
# アスタリスクを使って最小値と最大値、そして中間の値をタプルにして　返却するような関数を作成する
def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


longest, *middle, shortest = get_avg_ratio(lengths)

print(f'Longest: {longest:>4.9%}')
print(f'Shortest: {shortest:>4.9%}')

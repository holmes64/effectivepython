from time import sleep
from datetime import datetime

import json


'''
    デフォルト引数は関数が定義されたときの一度しか評価されない。
    なので以下の例はタイムスタンプが同じになる。
'''
def log(message, when=datetime.now()):
    print(f'{when}: {message}')


log('Hi there!')
sleep(0.1)
log('Hi again!')


'''
    デフォルト値をNoneにして、doctringに実際の振る舞いを記述する
'''
def log2(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log2('Hi there!')
sleep(0.1)
log2('Hi again!')


'''
    同じくデフォルト引数が一度しか呼び出されないので、すべてのdecodeへの呼び出しで共有される。
    なので以下の例ではfooとbarがそれぞれ同じ値を参照しており、表示してしまう。
'''
def decode(data, defaults={}):
    try:
        return json.loads(data)
    except ValueError:
        return defaults


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)


'''
    Solution
'''
def decode2(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo2 = decode2('bad data')
foo2['stuff'] = 5
bar2 = decode2('also bad')
bar2['meep'] = 1
print('Foo:', foo2)
print('Bar:', bar2)




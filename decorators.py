import datetime
from functools import wraps


def time_me(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'\n {func.__name__}')
        start = datetime.datetime.now()
        print(f'Start: {start.minute:02}:{start.second:02}')
        print('*' * 10)

        result = func(*args, **kwargs)

        print('*' * 10)
        end = datetime.datetime.now()
        print(f'End: {end.minute:02}:{end.second:02}')
        print(f'Elapsed time: {end - start}')

        return result

    return inner

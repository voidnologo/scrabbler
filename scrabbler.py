import asyncio
from itertools import chain

from files import get_file_paths
from search import check, Pattern


def file_contents(path):
    with open(path, 'r') as f:
        return f.read().splitlines()


async def filter(pattern, word, key):
    return await asyncio.to_thread(check, pattern, word, key)


async def finder(path, pattern, key):
    blocking = asyncio.to_thread(file_contents, path)
    word_list = list(await asyncio.create_task(blocking))
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(filter(pattern, word, key)) for word in word_list]

    results = zip(word_list, (t.result() for t in tasks))
    return [_[0] for _ in results if _[1] is True]


async def coordinator(pattern, key, buckets):
    data_paths = get_file_paths(buckets)

    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(finder(path, pattern, key)) for path in data_paths]
    return [t.result() for t in tasks]


def flatten(data):
    return chain.from_iterable(data)


def main(pattern, key, buckets='text/buckets'):
    results = asyncio.run(coordinator(pattern, key, buckets))
    r = sorted(flatten(results))
    print(r)


if __name__ == '__main__':
    main(Pattern.SUBSET, 'fish', 'text/buckets')

from decorators import time_me
from files import get_file_paths
from search import check, Pattern


def filter(pattern, word, key):
    return check(pattern, word, key)


@time_me
def main(pattern, key, buckets='text/buckets'):
    data_paths = get_file_paths(buckets)

    good_words = []

    for path in data_paths:
        with open(path, 'r') as f:
            words = f.read().splitlines()
            good = [word for word in words if check(pattern, word, key)]
            good_words.extend(good)

    r = sorted(good_words)
    print(pattern)
    print(f'{len(r)} results found.')
    print(r)


if __name__ == '__main__':
    main(Pattern.ENDSWITH, 'fish', 'text/buckets')
    main(Pattern.STARTSWITH, 'fish', 'text/buckets')
    main(Pattern.SUBSTR, 'fish', 'text/buckets')
    main(Pattern.CONTAINS, 'hifs', 'text/buckets')

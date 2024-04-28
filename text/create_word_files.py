from itertools import batched


def clean(word):
    return word.lower().replace("'", '')


with open('wordlist.txt', 'r') as f:
    lines = f.read().splitlines()

for words in batched(lines, 5):
    fname = f'buckets/{clean(words[0])}-{clean(words[-1])}.txt'
    with open(fname, 'w') as f:
        for word in words:
            f.write(f'{word}\n')

from itertools import batched
import subprocess


def clean(word):
    return word.lower().replace("'", '')


def chunk_write(word_list, chunk_size):
    for words in batched(word_list, chunk_size):
        fname = f'buckets/{clean(words[0])}-{clean(words[-1])}.txt'
        with open(fname, 'w') as f:
            for word in words:
                f.write(f'{word}\n')


# def test_list():
#     with open('wordlist.txt', 'r') as f:
#         lines = f.read().splitlines()
#     chunk_write(lines, 5)


def system_dictionary():
    word_list = subprocess.check_output(
        "cat /usr/share/dict/words | grep -v \"'s\"", shell=True, universal_newlines=True
    ).split('\n')
    chunk_write(word_list, 100)

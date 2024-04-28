from pathlib import Path


def get_file_paths(dir_name='text/buckets'):
    return Path(dir_name).glob('*.txt')

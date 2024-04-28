from enum import Enum, auto


class Pattern(Enum):
    SUBSET = auto()


def subset(val, key):
    return key in val


def check(pattern, value, key):
    match pattern:
        case Pattern.SUBSET:
            return subset(value, key)
        case _:
            raise ValueError(f'Unknown pattern: {pattern}')

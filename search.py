from enum import Enum, auto


class Pattern(Enum):
    CONTAINS = auto()
    ENDSWITH = auto()
    STARTSWITH = auto()
    SUBSTR = auto()


def check(pattern, value, key):
    match pattern:
        # all the letters in `key` are found in `value` regardless of order or quantity
        case Pattern.CONTAINS:
            return set(key).issubset(set(value))

        # specific substring is at the END of word
        case Pattern.ENDSWITH:
            return value.endswith(key)

        # specific substring is at the START of word
        case Pattern.STARTSWITH:
            return value.startswith(key)

        # specific substring can be found anywhere in the word
        case Pattern.SUBSTR:
            return key in value

        # whatch talkin about!?
        case _:
            raise ValueError(f'Unknown pattern: {pattern}')

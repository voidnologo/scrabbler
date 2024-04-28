from unittest import TestCase


from search import Pattern, check


class PatternChecksTests(TestCase):
    def test_SUBSET_should_return_True_if_key_is_in_value(self):
        value = 'behind'
        key = 'hi'
        result = check(Pattern.SUBSET, value, key)
        self.assertTrue(result)

    def test_SUBSET_should_return_False_if_key_is_not_in_value(self):
        value = 'behind'
        key = 'nope'
        result = check(Pattern.SUBSET, value, key)
        self.assertFalse(result)

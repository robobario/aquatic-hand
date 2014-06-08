from unittest import TestCase
from items import ScimatarRune

__author__ = 'python'


class TestItem(TestCase):
    def test_types(self):
        rune = ScimatarRune()
        type = rune.types
        type1 = getattr(rune, 'types')
        self.assertEquals(type, type1)
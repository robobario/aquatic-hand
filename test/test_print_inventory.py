from unittest import TestCase

import character
import items
import snapshot_printer


__author__ = 'python'


class TestPrint_inventory(TestCase):
    def test_print_inventory(self):
        char = character.Pc()
        invent = char.inventory
        invent.append(items.ScimatarRune())
        check_string = 'bone\nscimatar rune'
        self.assertEqual(snapshot_printer.print_inventory(char.inventory), check_string)

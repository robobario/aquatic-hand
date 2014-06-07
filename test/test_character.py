from unittest import TestCase

from character import Character


__author__ = 'python'


class TestCharacter(TestCase):
    def test_attack(self):
        character = Character()
        other = Character()
        character.attack(other)
        self.assertEqual(90, other.hp)

from unittest import TestCase

from bestiary import Bestiary


__author__ = 'python'


class TestBestiary(TestCase):
    def test_getMobsProducesCatOnFive(self):
        bestiary = Bestiary()
        bestiary.rng = (lambda: 5)
        mobs = bestiary.get_random_mobs([])
        self.assertEqual(1, len(mobs))
        self.assertEqual("cat", mobs[0].name)

    def test_getMobsProducesNothingWhenNotModFive(self):
        bestiary = Bestiary()
        bestiary.rng = (lambda: 2)
        mobs = bestiary.get_random_mobs([])
        self.assertEqual(0, len(mobs))
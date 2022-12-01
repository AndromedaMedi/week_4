import unittest
from models.player import Player, players
from models.game import Game


class TestGame(unittest.TestCase):

    def test_player_has_name(self):
        self.assertEqual("John", self.player1.name)


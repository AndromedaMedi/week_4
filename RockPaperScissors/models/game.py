from models.player import Player, players

class Game:

    def setUp(self):

        self.player1 = Player('John', 'paper')
        self.player2 = Player('Hannah', 'rock')
        self.player3 = Player('Mike', 'scissors')
        # self.player4 = Player('Jake', 'rock')
        # self.player5 = Player('Laura', 'paper')
        # self.player6 = Player('Jess', 'scissors')



        def compare_player_choices(player_1, player_2, player_3):
            player_1 = self.player1.choice
            player_2 = self.player2.choice
            player_3 = self.player3.choice
            if player_1 and player_2:
                return "Player 1 wins by playing paper"
            elif player_1 and player_3:
                return "Player 3 wins by playing scissors"
            elif player_2 and player_3:
                return "Player 2 wins by playing rock"
            else:
                None

        print(compare_player_choices)




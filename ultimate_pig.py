import random


def roll():
    """This function will randomly select a number from 1 - 6, the amount of
    faces on a dice"""  # part of the game function
    return random.randint(1, 6)


class Player():
    def __init__(self):
        # player starts with 0 points
        # all the players share the attribute that they start with 0 points
        self.points = 0
        # all the players share the attribute that they haven't rolled the dice
        self.count = 0

    def begin_round(self):
        """This function will start the round by using the points and the rolls
        that the player had from his previous round."""
        self.points = 0
        self.count = 0

    def will_roll(self):
        """This function will be the player's logic to roll. The base
        player will roll only one time."""
        # since the base player will only roll one time, return False.
        return False

    def roll_dice(self):
        # call the function to begin the round
        self.begin_round()
        # a while loop will continue to run for all the subclasses until breaks
        while True:
            rolling = roll()
            # increment number of rolls by one
            self.count += 1

            if rolling == 1:
                break
            else:
                self.points += 1

            if not self.will_roll():
                break

        return self.points


class Game:

    def __init__(self, player):
        self.player = player
    results_list = []

    def play(self):
        total_points = 0

        for _ in range(7):
            total_points += self.player.roll_dice()

    results_list.append(total_points)
    print(results_list)



class Aggressive(Player):
    def will_roll(self):
        """the dumb player will continue to roll the dice no matter what the points
        or the count of the game."""
        return self.count < 60


class Dumb(Player):
    def will_roll(self):
        return self.count < 200


class Cautious(Player):
    def will_roll(self):
        return self.count < 3

game = Game(Aggressive())
print("The aggressive player got {} points.".format(game.play()))
game = Game(Cautious())
print("The cautious player got {} points.".format(game.play()))
game = Game(Dumb())
print("The dumb player got {} points.".format(game.play()))

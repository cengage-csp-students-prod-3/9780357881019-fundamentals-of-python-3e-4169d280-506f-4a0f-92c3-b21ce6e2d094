"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Initializes the player for a new game."""
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ""            # String form of most recent roll
        self.rollsCount = 0       # Number of rolls made
        self.atStartup = True     # True before first roll
        self.winner = False       # True if player wins
        self.loser = False        # True if player loses
        self.point = 0            # Point to be made after first roll

    
    def rollDice(self):
        """Rolls the dice once, updates the game state, and returns a tuple of values."""
        if self.winner or self.loser:
            # Game already finished
            return None

        self.die1.roll()
        self.die2.roll()
        v1 = self.die1.getValue()
        v2 = self.die2.getValue()
        total = v1 + v2
        self.roll = f"({v1}, {v2}) total = {total}"
        self.rollsCount += 1

        # ----- Game logic -----
        if self.atStartup:
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
            else:
                self.point = total
                self.atStartup = False
        else:
            if total == self.point:
                self.winner = True
            elif total == 7:
                self.loser = True

        return (v1, v2)

    def getNumberOfRolls(self):
        """Returns the number of rolls made so far."""
        return self.rollsCount

    def play(self):
        """Plays a game, saves the rolls for that game, 
        and returns True for a win and False for a loss."""
        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while (True):
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(),
                        self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()
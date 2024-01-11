
# 'Hello, world!'.partition('XYZ')
# ('Hello, world!', '', '')
# 'Hello, world!'.partition('o')
# ('Hell', 'o', ', world!')
# 'Hello, world!'.partition('w')
# ('Hello, ', 'w', 'orld!')
# 'Hello, world!'.partition('world')
# ('Hello, ', 'world', '!')


# picnicItems = {
#     'sandwiches': 4,
#     'apples': 12,
#     'cups': 4,
#     'cookies': 8000
# }

# def printPicnicItems(total, ljust, rjust):
#     print('picnic items'.upper().center(total, '-'))

#     for items in picnicItems:
#         print(items.ljust(ljust,'.') + str(picnicItems[items]).rjust(rjust))


# printPicnicItems(17, 12, 5)
# printPicnicItems(26, 20, 6)

#! python3
# Chapter6.py - A multi-clipboard program

TEXT = {'busy': """Sorry, can we do this later this week or next week?""",
    'agree': """Yes, I agree.  That sounds find to me.""",
    'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

# print("This is a test!")

# if len(sys.argv) < 2:
#     print('Usage: python mclip.py [keyphrase] - copy phrase text')
#     sys.exit()

# keyphrase = sys.argv[1]

# if keyphrase in TEXT:
#     pyperclip.copy(TEXT[keyphrase])
#     print('Text for ' + keyphrase + ' copied to clipboard')
# else:
#     print('There is no text for ' + keyphrase)

#! python3
#bulletPointAdder.py - Adds Wiki bullet points to start
# of each line of text in clipboard

# text = pyperclip.paste()

# listOfText = text.split('\n')
# for index, items in enumerate(listOfText):
#     listOfText[index] = "* " + items

# text = '\n'.join(listOfText)

# pyperclip.copy(text)


# print('Enter the English message to translate into Pig Latin');
# msg = input()

#convert to pig latin
#if word begins with a vowel, add the word "yay" at the end
#if the word begins with a consanant/cluster, moved to the end of the word followed by 'ay'

# vowels = ['a', 'o', 'e', 'i', 'u', 'y']

# array = msg.split(' ')

# for index, item in enumerate(array):
#     if item[0].lower() in vowels:
#         array[index] = item + 'yay'
#     elif item[0].lower() not in vowels:
#         array[index] = item[1:] + item[0] + 'ay'

# print(' '.join(array))

# a cup of 13 dice with Brains, Footsteps and Shotgun Icons on their faces

#every die has 2 sides with footsteps on them
# dice with green icons have more brain sides
# dice with red icons have more shotgun sides
# dice with yellow icons have an even split between brains and shotguns

#on each players turn, do the following

#1: place all 13 dice in cup. player randomly draws 3 dice from that cup and rolls them.  Player always rolls exactly three dice

#2: count brains (humans whose brains were eaten), shotguns (humans who fought back). 3 shotguns ends a players turn with 0 points, regardless of how many brains there are. They can continue rolling if they have between 0 and 2 shotguns.  They can also end their turn and get 1 point per brain

#3: if they decide to reroll, they must roll all dice with footsteps. If they have less than 3 footsteps to roll.  They can keep rolling until 3 shotguns are rolled, or all 13 dice are rolled. Cannot stop mid-roll or reroll only one or two dice

#4. If someone reaches 13 brains, other players finish the round. The person with the most brains wins. On tie, tied players play one last tiebreaker round.

import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

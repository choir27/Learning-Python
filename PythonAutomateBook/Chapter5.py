# import sys

# birthdays = {'Alice': 'April 8', 'Melusine': 'June 20', 'illya': 'May 10'}
# print(birthdays.keys())     
# print(birthdays.values())   
# print(birthdays.items())    

# while True:
#     try:
#         print('Enter a name: (blank to quit)')
#         name = input()
#         if name == '':
#             sys.exit()
#         if name in birthdays:
#             print(birthdays[name] + ' is the birthday of ' + name + '.')
#         else:
#             print('I do not have birthday information for ' + name + '.')
#             print('What is their birthday?')
#             birthday = input()
#             birthdays[name] = birthday
#             print('Birthday database updated.')
#     except:
#         sys.exit()


# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# list = list(message);

# count = {}

# for i in message:
#     if message and i not in count:
#         count[i] = 1
#     elif message and i in count:
#         count[i] += 1

# print(count)

# for char in message:
#     count.setdefault(char,0)
#     count[char] = count[char] + 1

# import pprint

# pprint.pprint(count)

#create a simple tic tac toe game

# import random, sys

# #we need a board, and we need always show the player that board

# board = {1:' ',2:' ',3:' ',
# 4:' ',5:' ',6:' ',
# 7:' ',8:' ',9:' '}


# #we need to take in an input

# #alternate between O and X
# #player will always go first for now

# def screenBoard():
#     print(board[1] + '|' + board[2] + '|' + board[3])
#     print(board[4] + '|' + board[5] + '|' + board[6])
#     print(board[7] + '|' + board[8] + '|' + board[9])

# wins = 0
# losses = 0
# draws = 0

# def determineWinner():
#     choice = 'X'
#     global wins
#     if board[1] == choice and board[2] == choice and board[3] == choice:
#         print('You win!')
#         wins+=1
#     if board[4] == choice and board[5] == choice and board[6] == choice:
#         print('You win!')
#         wins+=1
#     if board[7] == choice and board[8] == choice and board[9] == choice:
#         print('You win!')
#         wins+=1
#     if board[1] == choice and board[4] == choice and board[7] == choice:
#         print('You win!')
#         wins+=1
#     if board[2] == choice and board[5] == choice and board[8] == choice:
#         print('You win!')
#         wins+=1
#     if board[3] == choice and board[6] == choice and board[9] == choice:
#         print('You win!')
#         wins+=1
#     if board[1] == choice and board[5] == choice and board[9] == choice:
#         print('You win!')
#         wins+=1
#     if board[3] == choice and board[5] == choice and board[7] == choice:
#         print('You win!')
#         wins+=1

#     global losses
#     choice = 'O'
#     if board[1] == choice and board[2] == choice and board[3] == choice:
#         print('You lose!')
#         losses+=1
#     if board[4] == choice and board[5] == choice and board[6] == choice:
#         print('You lose!')
#         losses+=1
#     if board[7] == choice and board[8] == choice and board[9] == choice:
#         print('You lose!')
#         losses+=1
#     if board[1] == choice and board[4] == choice and board[7] == choice:
#         print('You lose!')
#         losses+=1
#     if board[2] == choice and board[5] == choice and board[8] == choice:
#         print('You lose!')
#         losses+=1
#     if board[3] == choice and board[6] == choice and board[9] == choice:
#         print('You lose!')
#         losses+=1
#     if board[1] == choice and board[5] == choice and board[9] == choice:
#         print('You lose!')
#         losses+=1
#     if board[3] == choice and board[5] == choice and board[7] == choice:
#         print('You lose!')
#         losses+=1


# def printScore():
#     print('Wins: ' + wins + ' Losses: ' + losses + ' Draws: ' + draws)

# while True:
#     try:
#         print('enter a number from 1-9')
#         playerChoice = input();
    
#         if int(playerChoice) < 1 or int(playerChoice) > 9:
#             print('that is not a valid choice, please try again')
#             continue
#         else:
#             board[int(playerChoice)] = 'X'
#             computerChoice = random.randint(1,9)

#             while True:
#                 computerChoice = random.randint(1,9)
#                 if(board[computerChoice] == ' '):
#                     board[computerChoice] = 'O'
#                     break;
        
#         screenBoard()
#         determineWinner()
#     except KeyboardInterrupt:
#         sys.exit()
  

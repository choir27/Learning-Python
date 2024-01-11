# import sys

# arr = ['cat', 'dog', 'fish', 'IU']
# print(arr[0: 3])

# listOfServants = []

# for i in range(8):
#     try:
#         print("Enter the name of Servant " + str(i+1))
#         nameOfServant = input()
#         if nameOfServant == "":
#             sys.exit()
#         listOfServants = listOfServants + [nameOfServant]
#     except KeyboardInterrupt:
#         sys.exit()

# print("The servant names are: ")
# for name in listOfServants:
#     try:
#         print(name)
#     except KeyboardInterrupt:
#         sys.exit()
 

# listOfServants = ['kama', 'illya', 'melusine', 'miyu']

# print("Enter a servants name: ")
# usersInput = input()
# if usersInput in listOfServants:
#     print("That is a servant I own!")
# else:
#     print("That is not a servant I own.")

# list = []
# def appendList(servant):
#     list.append(servant)
#     print(list)

# appendList('kama')
# appendList('illya')
# appendList('melusine')
# appendList('miyu')

# import random

# messages = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply is no',
#     'Outlook not so good',
#     'Very doubtful']

# print(messages[random.randint(0,len(messages)-1)])

import sys

#rows 1, 2, 3, 4, 5, 6
#columns 1, 2, 3, 4, 5, 6
#'alive' t
#'dead' f
# [[f,f,f,f,f,f]
# [f,f,t,f,f,f]
# [f,f,f,t,f,f]
# [f,t,t,t,f,f]
# [f,f,f,f,f,f]
# [f,f,f,f,f,f]]

#if t has a t in same column index, +/-1 row index, it is considered a neighbor
#if t has a t in same row index, +/-1 column index, it is considered a neighbor
#if t has 2 or 3 neighbors, it stays t. otherwise, it becomes f
#if f has EXACTLY 3 neighbors, it becomes t.


# f = False
# t = True
# board = [
# [f,f,f,f,f,f],
# [f,f,t,f,f,f],
# [f,f,f,t,f,f],
# [f,t,t,t,f,f],
# [f,f,f,f,f,f],
# [f,f,f,f,f,f],
# ]#we have our board established

# #we have our neighbors established

# #we have a way to iterate through every element of the board established

# newBoard = []

# def countNumOfN(rightN, leftN, upN, downN):
#     numOfN = 0

#     if rightN:
#         numOfN += 1
#     if leftN:
#         numOfN += 1
#     if upN:
#         numOfN += 1
#     if downN:
#         numOfN += 1
#     return numOfN

# for i, row in enumerate(board):
#     newRow = []
#     for index, num in enumerate(board):
#         try:
#             if index != len(board)-1:
#                 rightN = row[index+1]
            
#             if index != 0:
#                 leftN = row[index-1]

#             if i!= len(board)-1:    
#                 upN = board[i+1][index]

#             if i!= 0:    
#                 downN = board[i-1][index]

#             if row[index]:

#                 numOfN = countNumOfN(rightN, leftN, upN, downN)
#                 #we have a way to count the number of neighbors

#                 if numOfN == 2 or numOfN == 3:
#                     newRow.append(True)    
#                 else:
#                     newRow.append(False)
#             else:
#                 leftN = None
#                 rightN = None
#                 upN = None
#                 downN = None

#                 if index != len(board)-1:
#                     rightN = row[index+1]
            
#                 if index != 0:
#                     leftN = row[index-1]

#                 if i!= len(board)-1:    
#                     upN = board[i+1][index]

#                 if i!= 0:    
#                     downN = board[i-1][index]

#                 numOfN = "" 

#                 if rightN is not None and leftN is not None and upN is not None and downN is not None:
#                     numOfN = countNumOfN(rightN, leftN, upN, downN)
#                     #we have a way to count the number of neighbors
#                 elif rightN is not None and leftN is not None and upN is not None:
#                     numOfN = countNumOfN(rightN, leftN, upN, False)
#                 elif rightN is not None and leftN is not None and downN is not None:
#                     numOfN = countNumOfN(rightN, leftN, False, downN)
#                 elif rightN is not None and upN is not None and downN is not None:
#                     numOfN = countNumOfN(rightN, False, upN, downN)
#                 elif leftN is not None and upN is not None and downN is not None:
#                     numOfN = countNumOfN(False, leftN, upN, downN)

#                 if numOfN == 3:
#                     newRow.append(True)
#                 else:
#                     newRow.append(False)

#         except KeyboardInterrupt:
#             sys.exit()
#     newBoard.append(newRow)

# print(newBoard)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#print this diagram out to show the following image:

# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

for i in range(len(grid)):
    line = ""
    for index in range(len(grid)):
        if i < 6:
            line += grid[index][i]
    if line:
        print(line)
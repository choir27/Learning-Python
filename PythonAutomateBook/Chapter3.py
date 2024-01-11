# def printFizzBuzz(n):
#     i = 1;
#     for i in range(n+1):
#         if i % 3 == 0 and i % 5 == 0 : 
#                print("Fizzbuzz")
#         elif i % 3 == 0:
#                print("Fizz")
#         elif i % 5 == 0:
#                print("Buzz")
#         else:
#                print(i)


# printFizzBuzz(15)

# name = "Melsuine"
# def test():
#      global name
#      name = "Shuten"

# name = "Elizabeth"
# test()
# print(name)


# name = "Melusine"
# if name == "Melusine":
#     test = "Shuten"

# print(test)

# try:
#       42/0
# except:
#       print("Cannot divide by zero")

# import time, sys

# try:
    
#     indent = 4
#     increaseIndent = False
#     animation = "********"
        
#     while True:
#         print(" " * indent + animation)
#         time.sleep(0.5)

#         if indent == 4:
#             increaseIndent = False
#         elif indent == 0:
#             increaseIndent = True

#         if increaseIndent:
#             indent = indent + 1
#         else:
#             indent = indent - 1
# except KeyboardInterrupt:
#         sys.exit()

import sys   

def collatz(number):
    try:
        if number % 2 == 0:
            perfectDivision = number // 2
            print(perfectDivision)
            return perfectDivision
        elif number % 2 != 0:
            product = number * 3 + 1
            print(product)
            return product
    except:
        print("Enter a number")
   

# if number is even, print number // 2 and return value
# if number is odd, print and return 3 * number + 1

# user types in integer
# keep calling collatz until you return 1

print("Enter number:")
userNumber = input()

finalNumber = collatz(int(userNumber))
while finalNumber != 1:
    try:
        finalNumber = collatz(int(finalNumber))
    except KeyboardInterrupt:
        sys.exit()
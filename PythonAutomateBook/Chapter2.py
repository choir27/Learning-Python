import random, sys

# name = "Illya"
# className = "Caster"

# if name == "Illya":
#     print("Hello " + name)
#     if className == "Caster":
#         print("Access Granted")
#     else:
#         print("Access Denied")

# className = "Assassin"

# if name == "Illya":
#     print("Hello " + name)
#     if className == "Caster":
#         print("Access Granted")
#     else:
#         print("Access Denied")

# name = "Melusine"
# className = "Caster"

# if name == "Illya":
#     print("Hello " + name)
#     if className == "Caster":
#         print("Access Granted")
#     else:
#         print("Access Denied")

# if "illya" == "illya":
#       print("hello illya")

# if "melusine" != "illya":
#       if "melusine" == "melusine":
#               print("hello melusine")


# name = "Melusine"
# className = "Lancer"
# rarity = 5

# if rarity > 1:
#      if className == "Lancer":
#           if name == "Melusine":
#                print(name + ' is a ' + className + ' and is a ' + str(rarity) + ' star servant in Fate Grand Order.');
# elif rarity < 5:
#      print("This is a low rarity servant.");
# else:
#      print("Please try again");

# rarity = 3

# if rarity > 1:
#      if className == "Lancer":
#           if name == "Melusine":
#                print(name + ' is a ' + className + ' and is a ' + str(rarity) + ' star servant in Fate Grand Order.');
# elif rarity < 5:
#      print("This is a low rarity servant.");
# else:
#      print("Please try again");

# rarity = "1"

# if int(rarity) > 1:
#      if className == "Lancer":
#           if name == "Melusine":
#                print(name + ' is a ' + className + ' and is a ' + str(rarity) + ' star servant in Fate Grand Order.');
# elif not(int(rarity) < 5):
#      print("This is a low rarity servant.");
# else:
#      print("Please try again");


# n = 80
# i = 0
# while i <= n:
#     if i % 5 == 0 and i % 3 == 0:
#         print('FizzBuzz');
#     elif i % 5 == 0:
#         print('Fizz');
#     elif i % 3 == 0:
#         print('Buzz');
#     else:
#         print(i);
#     i = i+1

# while True:
#     print("Who are you?");
#     name = input();
#     if name != "Melusine":
#         continue
#     print("Hello Melusine, what is today's password? (hint: it is on the rainbow)")
#     password = input()
#     if password == "blue":
#         break
# print("Acces Granted")

# for i in range(5):
#    print(random.randint(1, 10))

# for i in range(0, 20, 5):
#    print('' + str(i) + '')

# import random

# num = random.randint(1, 20);

# print('I am thinking of a number between 1 and 20.');

# for numOfGuess in range(1, 7):
#     print('Take a guess.');
#     print(num)
#     guess = input();
#     if int(guess) == int(num):
#         numOfGuess = numOfGuess + 1;
#         break;
#     elif int(guess) < int(num):
#         print('Your guess is too low');
#         numOfGuess = numOfGuess + 1;
#         continue;
#     elif int(guess) > int(num):
#         print('Your guess is too high');
#         numOfGuess = numOfGuess + 1;
#         continue;
# if int(guess) == int(num):
#     print('Good job! You guessed my number in ' + str(numOfGuess) + ' guesses!')
# else:
#     print('Too bad, my number was ' + str(num));

# import random;

print("ROCK, PAPER, SCISSORS");

win = 0
loss = 0
tie = 0

print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

choices = ["r", "p", "s"];

while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.");
    choice = input();
    computerChoice = choices[random.randint(0,2)];
    if choice == "r" and computerChoice == "p":
        print("ROCK versus...")
        print("PAPER")
        print("You lose!")
        loss = loss + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "r" and computerChoice == "r":
        
        print("ROCK versus...")
        print("ROCK")
        print("It's a tie!")
        tie = tie + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");


    elif choice == "r" and computerChoice == "s":
        print("ROCK versus...")
        print("SCISSORS")
        print("You win!")
        win = win + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "s" and computerChoice == "p":
        print("SCISSORS versus...")
        print("PAPER")
        print("You win!")
        win = win + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "s" and computerChoice == "r":
        print("SCISSORS versus...")
        print("ROCK")
        print("You lose!")
        loss = loss + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "s" and computerChoice == "s": 
        print("SCISSORS versus...")
        print("SCISSORS")
        print("It's a tie!")
        tie = tie + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "p" and computerChoice == "p":
        print("PAPER versus...")
        print("PAPER")
        print("It's a tie!")
        tie = tie + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "p" and computerChoice == "r":
        print("PAPER versus...")
        print("ROCK")
        print("You win!")
        win = win + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "p" and computerChoice == "s":
        print("ROCK versus...")
        print("SCISSORS")
        print("You lose!")
        loss = loss + 1
        print(str(win) + " Wins, " + str(loss) + " Losses, " + str(tie) + " Ties");

    elif choice == "q":
        sys.exit()
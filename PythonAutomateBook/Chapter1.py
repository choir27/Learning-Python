print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input() #Temporarily stops the program to ask the user to type in the terminal
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) #len is a function that returns the length of the argument/input
print('What is your age?')    # ask for their age
myAge = input() #temporarily stops the program to ask the user to type in the terminal
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

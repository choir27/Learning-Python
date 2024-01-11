# Randomize order of questions so all quizzes are unique Y

# 10 multiple choice questions for each quiz, in random order Y

# Provide correct answer and 3 random wrong answers for each question, random order Y

# Create 35 text files for the 35 quizzes Y

# Create 35 answer keys for the 35 quizzes Y

# Accept input from user, where the user can add their own customized questions, answers, multiple choices, the number of students and the number of questions. Y

# Take those customized inputs and create quizzes Y

# Save the input regardless of quitting the program to 'save' your progress

import random, os, sys
from pathlib import Path

def createQuiz():
    try:
        
        questions = [
        ]

        print("How many students are in your classroom?")
        numOfStudents = int(input())

        print("How many questions do you want on your quiz/test?")
        numOfQuestions = int(input())

        for i in range(1, numOfQuestions+1):
            exam = {}
            print(f"What will the question be for question {i}?")
            question = input()

            exam.setdefault('question', question)
            choices = []
            for j in range(1,5):
                print(f"What will be the multiple choice {j} for this question?") 
                choice = input()
    
                choices.append(choice)
            exam.setdefault('choices', choices)
            print(f"What will be the answer for question {i}, '{question}'?") 
            answer = input()
            exam.setdefault('answer', answer)
    

            questions.append(exam)

    # exclude 'a' and exclude 'q' when randomizing your questions
            currentWorkingPath = Path.cwd()

            if not Path(str(currentWorkingPath) + rf'\quizzes') and not Path(str(currentWorkingPath) + rf'\answers'):
                os.makedirs(Path(str(currentWorkingPath) + rf'\quizzes'))
                os.makedirs(Path(str(currentWorkingPath) + rf'\answers'))

        for i in range(1, numOfStudents+1):

            quizPath = Path(str(currentWorkingPath) + rf'\quizzes\quiz{i}.txt')
            quizAnswerPath = Path(str(currentWorkingPath) + rf'\answers\quizAnswer{i}.txt')

            quizFile = open(quizPath, 'w')
            quizAnswerFile = open(quizAnswerPath, 'w')

            # randomize the question order
            random.shuffle(questions)

            for index,items in enumerate(questions):
                random.shuffle(items['choices'])
                quizFile.write(f'''

    Question {index+1}: {items['question']}
        1. {items['choices'][0]}
        2. {items['choices'][1]}
        3. {items['choices'][2]}
        4. {items['choices'][3]}

                ''')

                quizAnswerFile.write(f'''

    Question {index+1}: {items['question']}

        Answer: {items['answer']}

                ''')


            quizFile.close()
            quizAnswerFile.close()
    except:
        print("Your input was invalid or something went wrong, please try again!")
        sys.exit()

try:
    createQuiz()
except KeyboardInterrupt:
    sys.exit()

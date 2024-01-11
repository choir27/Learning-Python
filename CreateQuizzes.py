# Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on Anime. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

# 5 students

# Randomize order of questions so all quizzes are unique Y

# 10 multiple choice questions for each quiz, in random order Y

# Provide correct answer and 3 random wrong answers for each question, random order Y

# Create 35 text files for the 35 quizzes Y

# Create 35 answer keys for the 35 quizzes Y

import random, os, sys
from pathlib import Path

questions = [
    {
        'q': 'Who is the main character of Kaguya-sama: Love is Not War?',
        'choices': ['Miyuki Shirogane', 'Kaguya Shinomiya', 'Kei Shirogane', 'Both 1 and 2'],
        'a': 'Both 1 and 2',
    },
       {
        'q': 'Which of the following is not an isekai anime?',
        'choices': ['Steins:Gate;','Re:Creators','Gate','Konosuba'],
        'a': 'Steins:Gate;',
    },
       {
        'q': 'What are the 7 main servant classes in the fate series?',
        'choices': ['caster, berserker, rider, assassin, saber, archer, lancer',
        'shielder, alter-ego, foreigner, avenger, pretender, ruler, moon cancer',
        'caster, berserker, rider, ruler, saber, archer, lancer',
        'caster, berserker, rider, assassin, foreigner, archer, lancer'],
        'a': 'caster, berserker, rider, assassin, saber, archer, lancer',
    },
       {
        'q': 'Where does Luffy originally start off from, in regards to the 4 different sections of the world?',
        'choices': ['West Blue',
        'North Blue',
        'East Blue',
        'South Blue'],
        'a': 'East Blue',
    },
      {
        'q': 'How are you able to summon a high level monster in the game of Duel Monsters, Yu-Gi-Oh?',
        'choices': ['Use the power of friendship to overcome any obstacle.',
        'Use the heart of the cards to guide your way.',
        'Sacrifice your life points to 1, flip your deck upside down, and dance for 30 seconds.',
        'Sacrifice at least one of your monsters that you currently control.'],
        'a': 'Sacrifice at least one of your monsters that you currently control.',
    },
      {
        'q': 'When are you ususally able to challenge the Elite Four?',
        'choices': ['When you get 16 badges.',
        'When you get 9 badges.',
        'When you get 8 badges.',
        'When you get 3 badges.'],
        'a': 'When you get 8 badges.',
    }
]

#exclude 'a' and exclude 'q' when randomizing your questions

totNumOfStudents = 6

for i in range(1,totNumOfStudents):
    try:
        currentWorkingPath = Path.cwd()
        quizPath = Path(str(currentWorkingPath) + rf'\quiz{i}.txt')
        quizAnswerPath = Path(str(currentWorkingPath) + rf'\quizAnswer{i}.txt')

        quizFile = open(quizPath, 'w')
        quizAnswerFile = open(quizAnswerPath, 'w')

        # randomize the question order
        random.shuffle(questions)

        for index,items in enumerate(questions):
            random.shuffle(items['choices'])
            quizFile.write(f'''
                Question {index+1}: {items['q']}
                1. {items['choices'][0]}
                2. {items['choices'][1]}
                3. {items['choices'][2]}
                4. {items['choices'][3]}
                ''')
            quizAnswerFile.write(f'''
                Question {index+1}: {items['q']}
                Answer: {items['a']}
            ''')

            
        quizFile.close()
        
    except KeyboardInterrupt:
        sys.exit()

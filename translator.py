# Importing pip library to install python packages
import pip

# Function to install python module within code
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Installing deep-translator for translation purposes and inquirer to generate selector interface
install ('deep-translator')
install ('inquirer')

# Importing required libraries
import inquirer
from deep_translator import GoogleTranslator as translate

# Input the file name that you require to be translated
file = input('Enter your input file name: ')
file2 = input('Enter the output file name in which you want to store the output: ')

#Language options to select from
options = ['Bengali: bn', 'Gujarati: gu', 'Hindi: hi', 'Malayalam: ml', 'Marathi: mr', 'Punjabi: pa', 'Tamil: ta', 'Telugu: te', 'Urdu: ur']

# Translation functionality and printing the output
questions = [
    inquirer.List('language',
                  message="Which language do you want to choose?",
                  choices=options,
                  ),
]
answers = inquirer.prompt(questions)

print("Your selected language is: " + answers['language'])

lang = answers['language'][-2:]

translated = translate(source='auto', target= lang).translate_file(file)

print(translated)

# Storing the output in an output file
lst = [translated]

with open(file2, "w", encoding="utf-8") as f:
    f.writelines(lst)
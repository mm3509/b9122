import random

jokes = [
    "What do you get when you cross a snowman with a vampire? Frostbite!",
    "What cheese is made backwards? Edam!",
    "What do lawyers wear to courts? Lawsuits!",
    "What do you call a grizzly bear with no teeth? A gummy bear"
]

answer = input("Would you like to hear a joke? ")

if answer == "yes":
    print(random.choice(jokes))
if answer == "no":
    print("Fine, I won't tell you a joke")
else:
    print("I don't understand")
    

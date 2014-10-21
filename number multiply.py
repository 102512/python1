import random
import time
import sys

list = ["Yes, most definitely!", "The chances are high!", "May the odds be ever in your favor.",
                        "99.9% success rate",
                        "Congratulations, yes!", "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again",
        ]
def userinput():
        question = 'Enter your question:'
        print(question)
        stuff = input("> ")
 
        print("\nThinking..\n")
        time.sleep(1)
        print(random.choice(list))
       
        final()
       
def final():
        print("Would you like to ask another question?")
        user_reply = input('> ')
        while(input):
                if user_reply == "yes":
                        userinput()
                else:
                        print("Thanks for playing!")
                        sys.exit(0)
print("Welcome to the Magic 8 Ball!")
userinput()

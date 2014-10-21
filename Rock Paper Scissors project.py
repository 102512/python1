#Began on 10/15/14 3pm
import random
import time
import sys

list = ["Rock", "Paper", "Scissors"]

def play():
    question = input("Do you choose Rock, Paper, or Scissors?: ") #Asks user to choose one
    print("Thinking..")
    time.sleep(2) #sleeps for 2 seconds

    compchoice = random.choice(list) #variable for computer choice
    print("Computer chose", compchoice) #prints computer choice
    time.sleep(1)


    if question.lower() == "rock" and compchoice.lower() == "paper":
        print("You lose")
        final()
    elif question.lower() == "paper" and compchoice.lower() == "scissors":
        print("You lose")
        final()
    elif question.lower() == "scissors" and compchoice.lower() == "rock":
        print("You lose")
        final()
    elif question.lower() == "paper" and compchoice.lower() == "rock":
        print("You win!!")
        final()
    elif question.lower() == "rock" and compchoice.lower() == "scissors":
        print("You win!!")
        final()
    elif question.lower() == "scissors" and compchoice.lower() == "paper":
        print("You win!!")
        final()
    else:
        print("Tie")
        final()
        

def final():
    reply = input("Do you suck dick? (YES OR NO)")
    while(input):
        if reply.lower() == "yes":
            play()
        else:
            print("Thanks for playing!")
            sys.exit(0)
play()
    

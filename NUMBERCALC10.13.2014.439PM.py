while 1 == 1:
    def x():
        a = int(input("What number are you thinking of?:")) #Takes input
        if a > 0 and a <= 10: #decides what to do with input
            print("That number is under 10 but over 0")
            answer = str(input("Continue?")) #asks if user wants to continue
            if answer ==("y"): #if yes, prints a statement and returns to calc
                print("Okay, go on")
                return
            else: #otherwise, prints statement and exits.
                print("Okay, all done!")
                exit()
        if a >= 10 and a <= 20:
            print("That number is over 10 :::STATEMENT UNDER CONSTRUCTION:::")
            answer = str(input("Continue?"))
            if answer ==("y"):
                print("Okay, go on")
                return
            else:
                print("All done")
                exit()
            
# FOLLOWING REGION IS COMMENTED OUT TO SAVE CODE BUT NOT USE IT.
# CODE IS USELESS BECAUSE PROGRAM IS WRAPPED IN FUNCTION X
##    def y():
##        a = int(input("What number are you thinking of?:"))
##        if a > 10 and a <= 20:
##            print("That number is under 20 but over 10")
##            answer = str(input("Continue?"))
##            if answer ==("y"):
##                print("Okay, go on")
##                return
    x() #calls function inside of while loop

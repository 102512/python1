while 1 == 1:
    def x():
        a = int(input("What number are you thinking of?:"))
        if a > 0 and a <= 10:
            print("That number is under 10 but over 0")
            answer = str(input("Continue?"))
            if answer ==("y"):
                print("Okay, go on")
                return
            else:
                print("Okay, all done!")
                exit()
        if a >= 10:
            print("That number is over 10 :::STATEMENT UNDER CONSTRUCTION:::")
            answer = str(input("Continue?"))
            if answer ==("y"):
                print("Okay, go on")
                return
            else:
                print("All done")
                exit()
            
    def y():
        a = int(input("What number are you thinking of?:"))
        if a > 10 and a <= 20:
            print("That number is under 20 but over 10")
            answer = str(input("Continue?"))
            if answer ==("y"):
                print("Okay, go on")
                return
    x()

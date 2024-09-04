print("You are in an abandoned building.")
print("You do not remember how you got here.")
print("There are no signs. ")
answerA = input("Where will you go now? (forward/back/left/right)")

if answerA == "forward":
    print("You start walking forward.")

elif answerA == "back":
    answerb = input("Are you sure?")
    if answerb == "yes":
        print("I wouldn't recommend it, but alright.")
        print("")
    elif answerb == "no":
        print("Where will you go now? (forward/back/left/right)")

elif answerA == "left":
    print("")

elif answerA == "right":
    print("")
print("You are in an abandoned building.")
print("You do not remember how you got here.")
print("There are no signs. There are no people. Cold, pale lighting radiates from the dim ceiling light directly above you. You can see in front of you and behind you just enough to notice the glass shards by your feet. To your left is an unlabeled door.")
answerA = input("Where will you go now? (forward/back/left)")

if answerA == "forward":
    print("You start walking forward.")

elif answerA == "back":
    answerb = input("Are you sure?")
    if answerb == "yes":
        print("I wouldn't recommend it, but alright.")
        print("")
    elif answerb == "no":
        answerA = input("Where will you go now? (forward/back/left)")
        if answerA == "back":
            answerc = input("Didn't you just say you weren't going to do that? Or did you mean you're not sure, but you're doing it anyway? (1/2)")
            if answerc == "1":
                print("Well, then, why are you doing it? Seriously, you make about as much sense as... whatever this place is. It almost feels like you're doing this just to mess with me.")
                print("Oh, well, whatever. I'm not going to stop you. It's not my job to understand what goes on in that head of yours, and it's not my job to protect you. I'm just the narrator.")
                print("You turn around and start walking back the way you... seem to have come? You're not sure. This place doesn't make any sense. I don't need to tell you that -- you're the one in this mess, and anyway, you don't make sense, either,.")
                print("The space around you gets darker as you go, and there are more and more glass shards the further you get from where you started. You can't see them, but you can feel them all too well. You're sure you must have a thousand cuts by now, but you keep going, for whatever reason. Strangely, they don't seem to hurt -- maybe it's just the adrenaline?")
                print("You hear a sound. It doesn't sound like anything you've ever heard before, or even something that should exist. It is loud and quiet and everywhere and nowhere, and, above all, EMPTY. You don't know what it is. You don't know what it means. It doesn't seem... safe.")
                answerd = input("Look, I know I said it wasn't my job to protect you, but I'm honestly starting to get a bit concerned. Are you sure you want to keep going? (yes/no)")

            elif answerc == "2":
                print("Alright, then. I can already tell you that this is a bad idea, but I'm not going to stop you.")

elif answerA == "left":
    print("You reach towards the door and feel for the handle. It takes you a while to find it, as you can barely see, and the door is oddly patterned, but you do find it eventually, and the door clicks open. As you step inside, you notice that there are more doors. There is also a flashlight, dropped on the floor as if")
    answerb = input("Do you take the flashlight? (yes/no)")
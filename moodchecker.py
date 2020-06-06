user_name = input("Please enter your name: ")

print("Hello " + user_name + "!")

mood = input(user_name + "," + " " + "how are you feeling? ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Cheer up, Mate!")
elif mood == "excited":
    print("Get a tee to relax.")
elif mood == "relaxed":
    print("Well, that's a good state of mind!")
else:
    print("I don't recognize this mood")
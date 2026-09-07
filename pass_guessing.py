import random
easy_word = ["apple","mango","papaya","banana","guava"]
medium_word = ["Tata curve","pyhton","javascript","rust"]
hard_word = ["mitocondria","redbloodcell","omega","parden"]
print("------Welcome to the password guessing game------")
print("Choose difficulty level")

level = input("Enter Difficulity level : ").lower()
if level == "easy":
    main_guess = random.choice(easy_word)
elif level == "medium":
    main_guess = random.choice(medium_word)
elif level == "hard":
    main_guess = random.choice(hard_word)
else:
    print("Invalid Choice, Default directed to easy level")
    main_guess  = random.choice(easy_word)

attempts = 0
print("\nGuess the secret password")                           
   
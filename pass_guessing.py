import random
easy_word = ["apple","mango","papaya","banana","guava"]
medium_word = ["Tata curve","pyhton","javascript","rust"]
hard_word = ["mitocondria","redbloodcell","omega","parden"]
print("------Welcome to the password guessing game------")
print("Choose difficulty level")

level = input("Enter Difficulity level : ").lower()
if level == "easy":
    secret_word = random.choice(easy_word)
elif level == "medium":
    secret_word = random.choice(medium_word)
elif level == "hard":
    secret_word = random.choice(hard_word)
else:
    print("Invalid Choice, Default directed to easy level")
    secret_word  = random.choice(easy_word)

attempts = 0
print("\nGuess the secret password")              

while True:
    guess = input("Enter Your guess : ").lower()
    attempts+=1

    if guess ==secret_word  :
        print(f"You guessed it in {attempts} attempts!!!!")
        break
    hint = ""
    for i in range(len(secret_word)):
        if i < len(guess) and guess[i] == secret_word[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print(f"Hint{hint}")
print("Game over")           
   
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "AIR": 3, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")

    for word, points in WORDS.items():
        print(f"{word} is worth {points} points")

    print("You can make words using these letters: A I P C R H G")

    while len(WORDS) > 0:
        print(f"\n{len(WORDS)} words left to guess.")
        guess = input("Guess a word: ")

        # TODO: Check if the guess is valid
        if guess == "GRAPHIC":
            WORDS.clear()
            print("Congratulations! You guessed the secret word and won the game!")
        if guess in WORDS:
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")
    
    print("That's the game!")

main()
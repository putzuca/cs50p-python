def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Invalid input. Please enter a valid difficulty")
        return
    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Invalid input. Please enter a valid option for players.")
        return
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Dark Souls")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Poker")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    elif difficulty == "Casual" and players == "Single-player":
        recommend("Clock Tower")

def recommend(game):
    print("I recommend playing " + game + "!")

main()
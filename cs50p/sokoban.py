def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
            print("History cleared.")
        else:
            history.append(action)

        print(f"History: {history}")

main()
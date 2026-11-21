import sys

import requests


def main():
    print("Search the Open Library!")
    author = input("Author: ")

    try:
        response = requests.get(
            "https://openlibrary.org/search", {"q": author, "limit": 3}, headers={"User-Agent": "cs50p-esercizio"}
        )
        response.raise_for_status()
    except requests.RequestException:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    print(response)
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
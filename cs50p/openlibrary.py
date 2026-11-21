import requests


def main():
    response = requests.get(
        "https://openlibrary.org/search.json",
        {"q": "tolkien", "limit": 3},
        headers={"User-Agent": "cs50p-esercizio"},
    )
    response.raise_for_status()
    content = response.json()
    for book in content["docs"]:
        print(f"* {book['title']}")


main()

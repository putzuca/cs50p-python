SHOWS = [
    " Avatar: The last Airbender",
    "Breaking bad",
    " Game of Thrones",
    "Arthur ",
    " Spongebob Squarepants",
    "Kim Possible",
    "Jimmy Neutron",
    "the Proud Family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())        
    
    print(', '.join(cleaned_shows))

main()
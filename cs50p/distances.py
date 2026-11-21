distances = {
    "Voyager 1": "163",
    "Voyager 2": "126",
    "Pioneer 10": "122 AU",
    "New Horizons": "50",
    "Pioneer 11": "100"
}

def main():
    spacecraft = input("Spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not a valid spacecraft.")
        return
    except ValueError:
        print(f"Invalid input for {spacecraft}: '{distances[spacecraft]}' is not a number.")
        return
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()
def area(length, width):
    print(str(length * width) + " square units")
    return length * width

def main():
    house = area(50, 20)

    yard = area(50,50)

    total = house + yard
    print(str(total) + " total square units")

main()
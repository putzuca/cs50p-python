import re

def main():
    code = input("Hexadecimal color code: ")
    
    pattern = r"#"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. MAtched with {match.group()}")
    else:
        print("Invalid.")

main()
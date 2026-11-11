emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = "o.o"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()
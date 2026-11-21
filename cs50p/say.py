import sys  # noqa: I001
import cowsay
from sayings import hello


def main():
    if len(sys.argv) == 2:
        cowsay.cow(sys.argv[1])
        hello(sys.argv[1])
        

main()
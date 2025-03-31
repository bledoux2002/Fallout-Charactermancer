#test file for experimenting with small chunks of python code, just to see if something will work

from character import Character
from creator import Creator

def main():
    char = Character()
    char.info()
    
    creator = Creator(char)
    char.info()


if __name__ == "__main__":
    main()
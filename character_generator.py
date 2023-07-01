# Character Creator for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 5/27/2023 1848, last editted 6/30/2023 2118

from time import sleep

#class Character:
    
#    def __init__(self):

#textSpeed = 0.0325
textSpeed = 0    
def main():
    while True:
        printDelay('Welcome to the Fallout Tabletop Roleplaying Game Character Creator!', textSpeed, True)
        printDelay('Please select one of the options from the menu below by entering the corresponding number:', textSpeed, True)
        printDelay('1. Create a new character', textSpeed, True)
        printDelay('2. View saved characters', textSpeed, True)
        printDelay('3. Upload a character file', textSpeed, True)
        printDelay('4. Quit', textSpeed, True)
        printDelay('Please enter corresponding number: ', textSpeed, False)
        menuChoice = input()
        #either use if/elif/elif or match-case/switch, determine efficiency for menu selection
        match menuChoice:
            case '1':
                generateChar()
            case '2':
                listChar()
            case '3':
                uploadChar()
            case '4':
                printDelay('Bombs dropping in ', textSpeed, False)
                printDelay('3....2....1....', 0.2, True)
                quit()
            case _:
                printDelay('Entry not recognized', textSpeed, True)
                main()

def printDelay(str, speed, newLine):
#    strLength = len(string)
    for i in range(len(str)):
        print(str[i], end='')
        sleep(speed)
    if newLine:
        print('')
    
def generateChar():
    printDelay('Generating new character...', textSpeed, True)
    pass
    main()
        
def listChar():
    printDelay('Here are your currently saved characters: ', textSpeed, True)
    pass
    main()
        
def uploadChar():
    printDelay('Please type the name of the character file you wish to upload: ', textSpeed, False)
    charFile = input() + '.json'
    printDelay('Uploading ' + charFile + '...', textSpeed, True)
    main()
    
main()
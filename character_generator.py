# Character Creator for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 5/27/2023 1848, last editted 7/13/2023 1139

import json
import os
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
                fileName = generateChar()
                editChar(fileName)
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

#printDelay() adds a pause between each character being printed to simulate a Fallout-style terminal
def printDelay(str, speed, newLine):
#    strLength = len(string)
    for i in range(len(str)):
        print(str[i], end='')
        sleep(speed)
    if newLine:
        print('')

#generateChar() takes the template.json character file and creates a copy to be editted
def generateChar():
    printDelay('Please enter the file name to save the character to: ', textSpeed, False)
    fileName = input()
    printDelay('Generating new character...', textSpeed, True)
    
    # Increment filename if already in use
    if os.path.exists(f"{fileName}.json"):
        printDelay('Character already exists, incrementing file name.', textSpeed, True)
        i = 1
        while os.path.exists(f"{fileName + str(i)}.json"):
            i += 1
        fileName += str(i)
    fileName += ".json"
    printDelay(f"Your character\'s file name is {fileName}", textSpeed, True)
    
    # Create copy of template.json w/ new fileName
    with open("template.json", "r") as templateFile:
        #template = templateFile.read()
        #testChar = json.loads(template)
        testChar = json.load(templateFile)
        with open(f"{fileName}", "w") as charFile:
            json.dump(testChar, charFile, indent=4)
            print(f"Successfully copied template to {fileName}")
    return (f"{fileName}")

#editChar() takes json filename as input, opens file as write file, presents menu listing contents of character sheet to edit
def editChar(file):
    pass
    main()

#listChar() gives a list of all character files saved/uploaded, and will have a view function to see each character's stats       
def listChar():
    printDelay('Here are your currently saved characters: ', textSpeed, True)
    pass
    main()

#uploadChar() registers a character file from the user inputted name, afetr the file has been dropped into the program folder 
def uploadChar():
    printDelay('Please type the name of the character file you wish to upload: ', textSpeed, False)
    charFile = input() + '.json'
    printDelay('Uploading ' + charFile + '...', textSpeed, True)
    main()

if __name__ == "__main__":
    main()
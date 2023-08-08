# Character Creator for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 5/27/2023 1848, last editted 7/13/2023 1139

import json
import os
from time import sleep

#class Character:
    
#    def __init__(self):

#printDelay('PSYCH! Coming soon tho...', textSpeed, True)
#textSpeed = 0.0325
textSpeed = 0 #may not be necessary but could be useful in case setting.json doesn't work
with open('settings.json', 'r') as settingsFile:
    settingsData = json.load(settingsFile)
    textSpeed = settingsData['tSpeed']

def main():
    textSpeed
    printDelay('Welcome to the Fallout Tabletop Roleplaying Game Character Creator!', textSpeed, True)
    mainChoice = 0
    #While quit has not been selected, run appropriate code for selection
    while mainChoice != '5':
        printMenu()
        mainChoice = input()
        match mainChoice:
            case '1':
                fileName = generateChar()
                editChar(fileName)
            case '2':
                listChar()
            case '3':
                uploadChar()
            case '4':
                settings()
            case '5':
                pass
            case _:
                printDelay('Entry not recognized', textSpeed, True)
    #Quit selected
    printDelay('Bombs dropping in ', textSpeed, False)
    printDelay('3....2....1....', 0.2, True)

#printDelay() adds a pause between each character being printed to simulate a Fallout-style terminal
def printDelay(str, speed, newLine):
#    strLength = len(string)
    for i in range(len(str)):
        print(str[i], end='')
        sleep(speed)
    if newLine:
        print('')

def printMenu():
    printDelay('Please select one of the options from the menu below by entering the corresponding number:', textSpeed, True)
    printDelay('1. Create a new character', textSpeed, True)
    printDelay('2. View saved characters', textSpeed, True)
    printDelay('3. Upload a character file', textSpeed, True)
    printDelay('4. Options', textSpeed, True)
    printDelay('5. Quit', textSpeed, True)
    printDelay('Please enter corresponding number: ', textSpeed, False)

#generateChar() takes the template.json character file and creates a copy to be editted
def generateChar():
    printDelay('Please enter the file name to save the character to: ', textSpeed, False)
    fileName = input()
    printDelay('Generating new character...', textSpeed, True)
    
    # Increment filename if already in use
    if os.path.exists(f'characters/{fileName}.json'):
        printDelay('Character already exists, incrementing file name.', textSpeed, True)
        i = 1
        while os.path.exists(f'characters/{fileName + str(i)}.json'):
            i += 1
        fileName += str(i)
    fileName += '.json'
    printDelay(f'Your character\'s file name is {fileName}', textSpeed, True)
    
    # Create copy of template.json w/ new fileName
    with open('template.json', 'r') as templateFile:
        #template = templateFile.read()
        #testChar = json.loads(template)
        testChar = json.load(templateFile)
        with open(f'characters/{fileName}', 'w') as charFile:
            json.dump(testChar, charFile, indent=4)
            print(f'Successfully copied template to {fileName}')
    return (f'{fileName}')

#editChar() takes json filename as input, opens file as write file, presents menu listing contents of character sheet to edit
def editChar(file):
    pass

#listChar() gives a list of all character files saved/uploaded, and will have a view function to see each character's stats       
def listChar():
    printDelay('Here are your currently saved characters: ', textSpeed, True)

#uploadChar() registers a character file from the user inputted name, afetr the file has been dropped into the program folder 
def uploadChar():
    printDelay('Please type the name of the character file you wish to upload: ', textSpeed, False)
    charFile = input() + '.json'
    printDelay('Uploading ' + charFile + '...', textSpeed, True)

#settings() will present another menu for different elements of the program to change, such as text speed
def settings():
    global textSpeed
    setChoice = '0'
    while setChoice != '2':
        printDelay('Please select one of the options from the menu below by enterring the corresponding number:', textSpeed, True)
        printDelay('1. Text speed', textSpeed, True)
        printDelay('2. Back', textSpeed, True)
        printDelay('Please enter the corresponding number: ', textSpeed, False)
        setChoice = input()
        match setChoice:
            case '1':
                printDelay('Speed options:', textSpeed, True)
                printDelay('1. Slow', textSpeed, True)
                printDelay('2. Medium', textSpeed, True)
                printDelay('3. Fast', textSpeed, True)
                printDelay('4. Instant', textSpeed, True)
                printDelay('Current selection: ', textSpeed, False)
                if textSpeed == 0.0625:
                    printDelay('Slow', textSpeed, True)
                elif textSpeed == 0.0375:
                    printDelay('Medium', textSpeed, True)
                elif textSpeed == 0.0125:
                    printDelay('Fast', textSpeed, True)
                elif textSpeed == 0: #could jsut be else instead of elif
                    printDelay('Instant', textSpeed, True)
                printDelay('Please enter the corresponding number: ', textSpeed, False)
                spdChoice = input()
                match spdChoice:
                    case '1':
                        textSpeed = 0.05
                    case '2':
                        textSpeed = 0.0375
                    case '3':
                        textSpeed = 0.025
                    case '4':
                        textSpeed = 0
                    case _:
                        printDelay('Sorry, that wasn\'t an option. Try again', textSpeed, True)
                with open('settings.json', 'r+') as setFile:
                    settingsData = json.load(setFile)
                    settingsData['tSPeed'] = textSpeed
            case '2':
                pass
            case _:
                printDelay('Oop, you done goofed. Try it again.', textSpeed, True)

if __name__ == '__main__':
    main()
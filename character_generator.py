# Character Creator for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 5/27/2023 1848, last editted 7/13/2023 1139

import json
import os
from time import sleep

#class Character: #could be useful for more indepth character management, for now jsut using JSON dict
    
#    def __init__(self):

#printDelay('PSYCH! Coming soon tho...')

# Initialize program with saved settings from JSON file
textSpeed = 0 #may not be necessary but could be useful in case setting.json doesn't work
with open('settings.json', 'r') as settingsFile:
    settingsData = json.load(settingsFile)
    textSpeed = settingsData['tSpeed']

def main():
    printDelay('Welcome to the Fallout Tabletop Roleplaying Game Character Creator!')
    #While quit has not been selected, present main menu, take input, then execute appropriate code
    mainChoice = '0'
    while mainChoice != '5':
        printDelay('Please select one of the options from the menu below:')
        printDelay('1. Create a new character')
        printDelay('2. View or edit a saved characters')
        printDelay('3. Create a copy of a character file')
        printDelay('4. Options')
        printDelay('5. Quit')
        printDelay('Enter corresponding number: ', False)
        mainChoice = input()
        match mainChoice:
            case '1':
                fileName = generateChar() #creates new character file using template.json, returns fileName including .json 
                if fileName != 0:
                    editChar(fileName)
            case '2':
                fileName = listChar()
                if fileName != 0:
                    listChoice = '0'
                    while listChoice != '3':
                        printDelay('Would you like to view or edit ' + fileName + '?')
                        printDelay('1. View')
                        printDelay('2. Edit')
                        printDelay('3. Back')
                        printDelay('Enter corresponding number: ', False)
                        listChoice = input()
                        match listChoice:
                            case '1':
                                with open(f'characters\\{fileName}', 'r') as charFile:
                                    charData = json.load(charFile)
                                    printDelay(json.dumps(charData, indent=1)) #will be replaced by printChar() function that tidies up the json data, only if user selects view instead of edit
                            case '2':
                                editChar(fileName)
                            case '3':
                                pass
                            case _:
                                printDelay('Entry invalid, try again.')
            case '3':
                #copyChar()
                printDelay('PSYCH! Coming soon tho...')
            case '4':
                settings()
                print(textSpeed)
            case '5':
                pass
            case _:
                printDelay('Entry invalid, try again.')
    #Quit selected, program should end right after two print statements
    printDelay('Bombs dropping in ', False)
    printDelay('3....2....1....', True, 0.2)

#printDelay() takes string, whether or not to add new line, and length of delay between printing string characters
def printDelay(str, newLine=True, speed=-1): #if using unique speed, have to declare newLine, even if default value
    global textSpeed
    if speed == -1:
        speed = textSpeed
    for i in range(len(str)):
        print(str[i], end='')
        sleep(speed)
    if newLine:
        print('')

#generateChar() takes creates a copy of template.json to be an edittable character file
def generateChar():
    printDelay('Please enter a file name (without file type extension): ', False)
    fileName = input()
    printDelay('Generating new character...') #not necessary, only slows program down, but who doesn't love a little showmanship
    
    # Increment filename if already in use
    if os.path.exists(f'characters\\{fileName}.json'):
        printDelay('Character already exists, incrementing file name...')
        i = 1
        while os.path.exists(f'characters\\{fileName + str(i)}.json'):
            i += 1
        fileName += str(i)
    fileName += '.json'
    printDelay(f'Your character\'s file name (with extension) is {fileName}')
    
    # Create copy of template.json w/ new fileName
    try:
        with open('template.json', 'r') as templateFile:
            testChar = json.load(templateFile)
            with open(f'characters\\{fileName}', 'w') as charFile:
                json.dump(testChar, charFile, indent=4)
        printDelay(f'Successfully copied template to {fileName}')
        return fileName
    except:
        printDelay('Whoops, something went wrong. Make sure the template.json file is still located in the same directory as this program.')
        return 0        

def listChar():
    charList = os.listdir('characters')
    editChoice = '0'
    while editChoice != str(len(charList) + 1):
        printDelay('Here are your currently saved characters: ')
        i = 0
        while i < len(charList):
            printDelay(str(i + 1) + '. ' + charList[i])
            i += 1
        printDelay(str(i + 1) + '. Back')
        printDelay('Enter the corresponding number: ', False)
        editChoice = input()
        if editChoice != str(len(charList) + 1):
            try:
                editChoice = int(editChoice)
                printDelay('You have selected ' + str(editChoice) + '. ' + charList[editChoice - 1])
                return charList[editChoice - 1]
            except:
                printDelay('Entry invalid, try again.')

#editChar() takes json filename as input, opens file as write file, presents menu listing contents of character sheet to edit
def editChar(file):
    printDelay('PSYCH! Coming soon tho...')

''' probably not necessary since file upload/download will likely have to be manual. could be implemented in future for website or unity app integration
#uploadChar() registers a character file from the user inputted name, afetr the file has been dropped into the program folder 
def uploadChar():
    printDelay('Please type the name of the character file you wish to upload: ', False)
    charFile = input() + '.json'
    printDelay('Uploading ' + charFile + '...')
'''

#settings() will present another menu for different elements of the program to change, such as text speed
def settings():
    global textSpeed
    setChoice = '0'
    while setChoice != '2':
        printDelay('Please select one of the options from the menu below:')
        printDelay('1. Text speed')
        printDelay('2. Back')
        printDelay('Enter the corresponding number: ', False)
        setChoice = input()
        match setChoice:
            case '1':
                spdChoice = '1'
                while spdChoice == ('1' or '2' or '3' or '4'):
                    printDelay('Speed options:')
                    printDelay('1. Slow')
                    printDelay('2. Medium')
                    printDelay('3. Fast')
                    printDelay('4. Instant')
                    printDelay('Current selection: ', False)
                    if textSpeed == 0.0625:
                        printDelay('Slow')
                    elif textSpeed == 0.0375:
                        printDelay('Medium')
                    elif textSpeed == 0.0125:
                        printDelay('Fast')
                    elif textSpeed == 0: #could jsut be else instead of elif
                        printDelay('Instant')
                    printDelay('Enter the corresponding number: ', False)
                    spdChoice = input()
                    match spdChoice:
                        case '1':
                            textSpeed = 0.0625
                            printDelay('Text speed is now Slow.')
                        case '2':
                            textSpeed = 0.0375
                            printDelay('Text speed is now Medium.')
                        case '3':
                            textSpeed = 0.0125
                            printDelay('Text speed is now Fast.')
                        case '4':
                            textSpeed = 0
                            printDelay('Text speed is now Instant.')
                        case _:
                            printDelay('Entry invalid, try again.')
                with open('settings.json', 'r') as setFile:
                    settingsData = json.load(setFile)
                settingsData['tSpeed'] = textSpeed
                with open('settings.json', 'w') as setFile:
                    json.dump(settingsData, setFile, indent=4)
                print(textSpeed)
            case '2':
                pass
            case _:
                printDelay('Entry invalid, try again.')

if __name__ == '__main__':
    main()
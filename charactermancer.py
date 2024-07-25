# Character creation and management system for the Fallout 2d20 Tabletop Roleplaying system by Modiphius Entertainment
# Created by Benjamin Ledoux using the Core Rulebook February 2023 edition.
# First created 5/27/2023 1848, last editted 7/13/2023 1139

import json
import os
from time import sleep

#class Character: #could be useful for more indepth character management, for now jsut using JSON dict
    
#    def __init__(self):

#printDelay('PSYCH! Coming soon tho...')

# Initialize program with saved settings from JSON file
try:
    with open('settings.json', 'r', encoding='utf-8') as settingsFile:
        settingsData = json.load(settingsFile)
        textSpeed = settingsData['tSpeed']
except:
    textSpeed = 0

def main():
    printDelay('Welcome to the Fallout Tabletop Roleplaying Game Character Creator!')
    #While quit has not been selected, present main menu, take input, then execute appropriate code
    mainChoice = '0'
    while mainChoice != 'q':
        printDelay('Please select one of the options from the menu below:')
        printDelay('1. New character')
        printDelay('2. Saved characters')
        printDelay('3. Options')
        printDelay('q. Quit')
        printDelay('Entry: ', False)
        mainChoice = input().lower()
        match mainChoice:
            case '1':
                fileName = generateChar() #creates new character file using template.json, returns fileName including .json 
                if fileName != 0:
                    editChar(fileName)
            case '2':
                fileName = listChar()
                if fileName != None: #listChar has not returned anything if "Back" was selected
                    listChoice = '0'
                    while listChoice != 'q':
                        printDelay(f'What would you like to do with {fileName} ?')
                        printDelay('1. View')
                        printDelay('2. Edit')
                        printDelay('3. Duplicate')
                        printDelay('4. Delete')
                        printDelay('q. Back')
                        printDelay('Entry: ', False)
                        listChoice = input().lower()
                        match listChoice:
                            case '1':
                                printChar(fileName)
                            case '2':
                                editChar(fileName)
                            case '3':
                                newFile = generateChar(f'characters\\{fileName}') #creates new character file using template.json, returns fileName including .json 
                                if newFile != 0:
                                    editChar(newFile)
                            case '4':
                                delChoice = None
                                while delChoice == None:
                                    printDelay(f'Are you sure you want to delete {fileName}? (y/n) ', False)
                                    delChoice = input().lower()
                                    match delChoice:
                                        case 'y':
                                            os.remove(f'characters\\{fileName}')
                                            printDelay(f'{fileName} removed')
                                            listChoice = 'q'
                                        case 'n':
                                            printDelay('Operation cancelled')
                                        case _:
                                            printDelay('Entry invalid, try again.')
                                            delChoice = None
                            case 'q':
                                pass
                            case _:
                                printDelay('Entry invalid, try again.')
            case '3':
                settings()
            case 'q':
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

#generateChar() takes creates a copy of template.json to be an edittable character file, will change to have default input for template.json, can be changed for duplicateChar
def generateChar(baseFile = 'template.json'):
    invalidChars = '<>:"/\|?*'
    printDelay('Please enter a file name (default "character"): ', False)
    fileName = input() #NO PROTECTION FOR FILE-NAMING RULES (for non-windows machines)
    # Remove illegal characters
    for char in invalidChars:
        fileName = fileName.replace(char, '')
    # Remove illegal ending characters
    if fileName != '': #needed in case all characters were illegal
        while fileName[-1] == ' ' or fileName[-1] == '.':
            fileName = fileName[:-1]
            if fileName == '':
                break
    # Default filename if empty
    if len(fileName) == 0:
        fileName = 'character'
    # Increment filename if already in use
    if os.path.exists(f'characters\\{fileName}.json'):
        printDelay('Character already exists, incrementing file name...')
        i = 1
        while os.path.exists(f'characters\\{fileName + str(i)}.json'):
            i += 1
        fileName += str(i)
    # Append filetype extension
    fileName += '.json'

    printDelay(f'Your character\'s file name (with extension) is {fileName}')
    
    # Create copy of baseFile w/ new fileName
    try:
        with open(baseFile, 'r', encoding='utf-8') as templateFile:
            testChar = json.load(templateFile)
            with open(f'characters\\{fileName}', 'w', encoding='utf-8') as charFile:
                json.dump(testChar, charFile, indent=4)
        printDelay(f'Successfully copied {baseFile} to {fileName}')
        return fileName
    except:
        printDelay(f'Whoops, something went wrong. Make sure {baseFile} file is still located in the same directory as this program.')
        return 0

#listChar() prints out all of the saved characters to select from, and allows the user to select one
def listChar():
    charList = os.listdir('characters')
    editChoice = '0'
    while editChoice != 'q':
        printDelay('Here are your currently saved characters: ')
        i = 0
        while i < len(charList):
            printDelay(str(i + 1) + '. ' + charList[i])
            i += 1
        printDelay('q. Back')
        printDelay('Entry: ', False)
        editChoice = input().lower()
        while editChoice != 'q': #if the user selects "Back," nothing is returned
            try:
                editChoice = int(editChoice)
                printDelay('You have selected ' + str(editChoice) + '. ' + charList[editChoice - 1])
                return charList[editChoice - 1]
            except:
                printDelay('Entry invalid, try again.')

#editChar() takes json filename as input, opens file as write file, presents menu listing contents of character sheet to edit
def editChar(file):
    #Maybe use length of dict to print out character editting options? should always be the same for this first menu so won't bother, but could be useful for listing assigned perks, equipment, etc.
    editChoice = '0'
    while editChoice != 'q':
        printDelay('Select what you would like to change:') #For now, functional options overwrite original values, so to add a last name one would write out the entire name in the input
        charData = printChar(file)
        printDelay('q. Back')
        printDelay('Entry: ', False)
        editChoice = input().lower()
        match editChoice:
            case '1':
                printDelay('New name: ', False)
                charData['name'] = input()
            case '2':
                printDelay('New level: ', False)
                charData['level'] = int(input())
            case '3':
                printDelay('New action points: ', False)
                charData['ap'] = int(input())
            case '4':
                printDelay('New experience points: ', False)
                charData['xp'] = int(input())
            case '5':
                printDelay('New health points: ', False)
                charData['health'] = int(input())
            case '6':
                printDelay('isRobot (True/False): ', False)
                charData['isRobot'] = bool(input())
            case '7':
                printDelay('isNPC (True/False): ', False)
                charData['isNPC'] = bool(input())
            case '8':
                printDelay('New origin: ', False)
                charData['origin'] = input()
            case '9':
                printDelay('Trait(s): ', False)
                charData['traits'] = input()
            case '10':
                printDelay('New equipment pack: ', False)
                charData['equipmentPack'] = input()
            case '11':
                specChoice = '0'
                while specChoice != 'q':
                    printDelay('Which S.P.E.C.I.A.L. stat would you like to change?')
                    keys = list(charData['attributes'].keys())
                    values = list(charData['attributes'].values())
                    for i in range(len(charData['attributes'])):
                        printDelay(str(i + 1) + '. ' + keys[i] + ' ' + str(values[i])) #why is this commented out?
                    printDelay('q. Back')
                    printDelay('Enter the corresponding number: ', False)
                    specChoice = input().lower()
                    match specChoice:
                        case '1':
                            printDelay('Strength: ', False)
                            charData['attributes']['STR'] = int(input())
                        case '2':
                            printDelay('Pereption: ', False)
                            charData['attributes']['PER'] = int(input())
                        case '3':
                            printDelay('Endurance: ', False)
                            charData['attributes']['END'] = int(input())
                        case '4':
                            printDelay('Charisma: ', False)
                            charData['attributes']['CHA'] = int(input())
                        case '5':
                            printDelay('Intelligence: ', False)
                            charData['attributes']['INT'] = int(input())
                        case '6':
                            printDelay('Agility: ', False)
                            charData['attributes']['AGI'] = int(input())
                        case '7':
                            printDelay('Luck: ', False)
                            charData['attributes']['LCK'] = int(input())
                        case 'q':
                            pass
                        case _:
                            printDelay('Entry invalid, try again.')
            case '12':
                printDelay('PSYCH! Coming soon tho...')
            case '13':
                printDelay('PSYCH! Coming soon tho...')
            case '14':
                printDelay('PSYCH! Coming soon tho...')
            case '15':
                printDelay('PSYCH! Coming soon tho...')
            case 'q':
                #ability to discard changes would require some sort of temporary file system to hold changes, and im too lazy to implement that (would be similar to duplicating a file, deleting old one, renaming new one)
                '''saveChoice = None
                while saveChoice == None:
                    printDelay('Save changes? (y/n) ', False)
                    saveChoice = input()
                    match saveChoice:
                        case 'y':
                            with open(f'characters\\{file}', 'w', encoding='utf-8') as charFile:
                                json.dump(charData, charFile, indent=4)
                            printDelay('Changes saved')
                        case 'n':
                            printDelay('Changes discarded')
                        case _:
                            printDelay('Entry invalid, try again.')
                            saveChoice = None'''
                pass
            case _:
                printDelay('Entry invalid, try again.')
        with open(f'characters\\{file}', 'w', encoding='utf-8') as charFile:
            json.dump(charData, charFile, indent=4)
        printDelay('Changes saved')

#printChar() takes a file name to print out the contents of and returns the data variable for use
def printChar(file):
    with open(f'characters\\{file}', 'r', encoding='utf-8') as charFile:
        charData = json.load(charFile)
    printDelay('1. Name: ' + charData['name'])
    printDelay('2. Level: ' + str(charData['level']))
    printDelay('3. Action Points: ' + str(charData['ap']))
    printDelay('4. Experience Points: ' + str(charData['xp']))
    printDelay('5. Health Points: ' + str(charData['health']))
    printDelay('6. isRobot: ' + str(charData['isRobot'])) #keep for now, will try to automate with backgrounds but manual assignment is needed for homebrew
    printDelay('7. isNPC: ' + str(charData['isNPC']))
    printDelay('8. Origin: ' + charData['origin'])
    printDelay('9. Traits: ' + charData['traits'])
    printDelay('10. Equipment Pack: ' + charData['equipmentPack'])
    attributeStr = ''
    for key, value in (charData['attributes'].items()):
        attributeStr += key + ' ' + str(value)
        if (key != 'LCK'):
            attributeStr += ', '
    printDelay('11. ' + attributeStr) #looks terrible but code is so much simpler. will go back and revamp but for now im lazy
    printDelay('12. Skills')
    printDelay('13. Perks')
    printDelay('14. Stats')
    printDelay('15. Inventory')
    return charData

#settings() will present another menu for different elements of the program to change, such as text speed
def settings():
    global textSpeed
    setChoice = '0'
    while setChoice != 'q':
        printDelay('Please select one of the options from the menu below:')
        printDelay('1. Text speed')
        printDelay('q. Back')
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
                with open('settings.json', 'r', encoding='utf-8') as setFile:
                    settingsData = json.load(setFile)
                settingsData['tSpeed'] = textSpeed
                with open('settings.json', 'w', encoding='utf-8') as setFile:
                    json.dump(settingsData, setFile, indent=4)
                print(textSpeed)
            case 'q':
                pass
            case _:
                printDelay('Entry invalid, try again.')

if __name__ == '__main__':
    main()
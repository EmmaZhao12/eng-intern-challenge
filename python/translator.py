import re
user_input = input()
output = []

language = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO"
}

numbers = {"1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO.."
    }

def translate_to_braille(input):
    #Edge case, user input is only a space 
    if input.isspace() :
        output.append("......")
    else:
        for char in input:
            #To append capital letter braille indicator
            if char.isupper():
                output.append(".....O")
                output.append(language.get(char.lower()))
            
            #To append number braille indicator
            elif char.isnumeric():
                output.append(".O.OOO")
                output.append(numbers.get(char))
            
            #To append space braille indicator
            elif char.isspace():
                output.append("......")
            
            #To append lowercase letters
            else:
                output.append(language.get(char))
    return
        
def translate_to_english(input):
    #Edge case, user input is only a space 
    if input=="......" :
        output.append(" ")        
    else:
        #Detectors for integer and capital letters, 0 represents no integer/capital indicator, and 1 means that they have been detected
        integer = 0
        capital = 0
        for index in range(0, len(input), 6):
                #To get a braille "character"
                curr = input[index:index+6]

                #Integer indicator
                if curr == ".O.OOO":
                    integer = 1
                
                #Capital letter indicator
                elif curr == ".....O":
                    capital = 1
                
                #Space detector, also resets integer indicator based on instructions
                elif curr == "......":
                    if bool(integer):
                        integer = 0
                    output.append(" ")
                
                #Appends numbers
                elif bool(integer):
                    for key in numbers.keys():
                        if numbers.get(key) == curr:
                            output.append(key)
                            break

                #Appends letters
                else:
                    for key in language.keys():
                        if language.get(key) == curr:
                            if bool(capital):
                                output.append(key.upper())
                                capital=0
                                break
                            else:
                                output.append(key)
                                break
    return


#Edge case, user input is nothing (newline)
if user_input=="\n":
    print(" ")
else:
    #Defining all the characters that are considered as "English" for the problem
    alphabet = re.compile(r'[a-zA-Z0-9]')
    if alphabet.match(user_input):
        translate_to_braille(user_input)
    else:
        translate_to_english(user_input)

print("".join(output))


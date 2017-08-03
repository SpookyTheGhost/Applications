#####################################################################
# Author: Kevin Zhang
# Date: 12/19/2014
# purpose: translator between english and morse code
#####################################################################

import string

def punctuation_test(convert):
    ##################################################################################################
    # purpose: test input for any punctuation. returns true if detected otherwise false
    ##################################################################################################
    test = False
    
    for x in convert:
        
        if x in string.punctuation:
            
            test = True
            
    return test

def convert_to_morse_code(convert):
    #####################################################################
    # translates to morse code
    #####################################################################
    
    conversion = ""
    
    upper_case = convert.upper() # forces all text to upper case
    
    words = upper_case.split(" ") # splits input into a list of the words for conversion
    
    for y in words: # locate spacing between words
        
            for z in y: # loops through each word and performs translation to morse code
                
                conversion += alpha_to_morse[z]
                
                conversion += " "
                
    conversion += "  " # this is to add appropriate spaces
            
    words.clear() # clear previous input
    
    return conversion # returns finished translation to morse code


def convert_to_alpha(convert):
    #####################################################################
    # translates to English
    #####################################################################
    
    print("""Please use the following guidelines otherwise conversion will fail
use 1 space between each dot or dash
use 2 spaces between words
""")
    conversion = ""
    
    words = convert.split("  ") # splits input into a list of the words for conversion
    
    for y in words: # locate spacing between words
        
        conversion += morse_to_alpha[y] # loops through each word and performs translation to morse code
        
    conversion += " " # this is to add appropriate spaces
    
    words.clear() # clear previous input
    
    return conversion # returns finished translation to morse code


alpha_to_morse = {
"A": ". -",
"B": "- . . .",
"C": "- . - .",
"D": "- . .",
"E": ".",
"F": ". . - .",
"G": "- - .",
"H": ". . . .",
"I": ". .",
"J": ". - - -",
"K": "- . -",
"L": ". - . .",
"M": "- -",
"N": "- .",
"O": "- - -",
"P": ". - - .",
"Q": "- - . -",
"R": ". - .",
"S": ". . .",
"T": "-",
"U": ". . -",
"V": ". . . -",
"W": ". - -",
"X": "- . . -",
"Y": "- . - -",
"Z": "- - . .",
"1": ".- - - -",
"2": ". . - - -",
"3": ". . . - -",
"4": ". . . . -",
"5": ". . . . . .",
"6": "- . . . .",
"7": "- - . . .",
"8": "- - - . .",
"9": "- - - - .",
"0": "- - - - -"}

morse_to_alpha = {
". -": "A",
"- . . .": "B",
"- . - .": "C",
"- . .": "D",
".": "E",
". . - .": "F",
"- - .": "G",
". . . .": "H",
". .": "I",
". - - -": "J",
"- . -": "K",
". - . .": "L",
"- -": "M",
"- .": "N",
"- - -": "O",
". - - .": "P",
"- - . -": "Q",
". - .": "R",
". . .": "S",
"-": "T",
". . -": "U",
". . . -": "V",
". - -": "W",
"- . . -": "X",
"- . - -": "Y",
"- - . .": "Z",
"- - - - -": "0",
". - - - -": "1",
". . - - -": "2",
". . . - -": "3",
". . . . -": "4",
". . . . . .": "5",
"- . . . .": "6",
"- - . . .": "7",
"- - - . .": "8",
"- - - - .": "9"}

def main():
    print("""
    MENU
    -------------------------------
    morse code to alphanumeric: man
    alphanumeric to morse code: anm
    quit: q

    notes: morse code does not contain puntuation marks, inputs containing these will result in conversion failures

    """)

    print("--------------------------------------------------------------------------------")

    response = input("What would you like to do?: ")      
    while (True):
        if response.lower() == "q":
            
            print("Thanks for Playing!")
            
            quit()


        elif response.lower() == "anm":
            
            conversion = input("What would you like to convert? ")
            
            detector = punctuation_test(conversion) # checks for punctuation
            
            if detector == False:
                
                print("converting to morse code")
                
                morse = convert_to_morse_code(conversion)
                
                print(conversion,"in morse code is",morse)
                
                print("conversion success!")

                response = input("What would you like to do?: ")
                
            else: # tells user to retry
                
                print ("punctuation detected, unable to translate to morse code")
                
                response = input("What would you like to do?: ")

            
        elif response.lower() == "man":

            print("""Please use the following guidelines otherwise conversion will fail
    use 1 space between each dot or dash
    use 2 spaces between words
    """)
            conversion = input("What would you like to convert? ")

            for x in conversion:
                
                if x == "." or x == "-":
                    
                    print("converting to morse code")
                    
                    english = convert_to_alpha(conversion)
                    
                    print(conversion,"in English is",english)
                    
                    print("conversion success!")

                    response = input("What would you like to do?: ")
                    
                else: # tells user to retry
                    
                    print ("unknown input, unable to translate to English")
                    
                    response = input("What would you like to do?: ")
        
            
        print("Unknown Command, please try again")
            
        response = input("What would you like to do?: ")
            
main()

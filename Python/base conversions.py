####################################################################
# Date: 12/20/2014
# purpose: decimal, binary, octal, hexadecimal conversions
####################################################################
import math

def string_reverse(s):
    return s[::-1]


def separator(s,step): 
    ##########################################
    # purpose: split string into 'n' chucks
    ##########################################
    l = []
    for x in range(0,len(str(s)),step):
        l.append(s[x:x+step])
    return l


def convert_to_decimal(base,num): 
    reverse = string_reverse(str(num)) # reverses string to allow correct calculations
    digit = len(reverse) - 1 # gets correct digits
    value = 0 # setting return variable to 0
    while (digit >= 0):
        value += pow(base,digit)*int(float(reverse[digit])) # multiplies correct digit and base power, updates return value
        digit -= 1 # reduces power by 1 for each iteration
    return value            


def decimal_to_binary(num):
    convert = ""
    split = separator(num,2) # splits into pieces of 2
    for x in split:
        while len(x) != 2:
            # checks each piece has a total of 2 1's or 0's
            # if not, adds 0's at the front
            x = '0' + x
        else:
            convert = binary[x] + convert # looks up value in dictionary
    return convert


def decimal_to_octal(num):
    convert = ""
    split = separator(num,3) # splits into pieces of 3
    for x in split:
        while len(x) != 3:
            # checks each piece has a total of 3 1's or 0's
            # if not, adds 0's at the front
            x = '0' + x
        else:
            convert = octal[x] + convert # looks up value in dictionary
    return convert


def decimal_to_hexadecimal(num):
    convert = ""
    split = separator(num,4) # splits into pieces of 4
    for x in split:
        while len(x) != 4:
            # checks each piece has a total of 4 1's or 0's
            # if not, adds 0's at the front
            x = '0' + x
        else:
            convert = hexadecimal[x] + convert # looks up value in dictionary
    return convert


def main():
    print("""
    MENU
    ----------------------
    decimal to binary: db
    decimal to octal: do
    decimal to hexadecimal: dh
    binary to decimal: bd
    binary to octal: bo
    binary to hexadecimal: bh
    octal to decimal: od
    octal to binary: ob
    octal to hexadecimal: oh
    hexadecimal to decimal: hd
    hexadecimal to binary: hb
    hexadecimal to octal: ho
    quit: q
    """)

    menu_select = input("Please choose an option from the above menu: ")


    while (True):
        
        if menu_select.lower() == "q":
            print("Thanks for Playing")
            quit()

          
        elif menu_select.lower() == "db":
            convert = float(input("Enter value to convert: "))
            print(convert," from decimal to binary is ",decimal_to_binary(convert))
            
        elif menu_select.lower() == "do":
            convert = float(input("Enter value to convert: "))
            print(convert," from decimal to octal is ",decimal_to_octal(convert))
            
        elif menu_select.lower() == "dh":
            convert = float(input("Enter value to convert: "))
            print(convert," from decimal to hexadecimal is ",decimal_to_hexadecimal(convert))
            
        elif menu_select.lower() == "bd": 
            convert = float(input("Enter value to convert: "))
            print(convert," from binary to decimal is ",convert_to_decimal(2,convert))

        elif menu_select.lower() == "bo":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(2,convert)
            to_octal = decimal_to_octal(to_decimal)
            print(convert," from binary to octal is ",to_octal)
            
        elif menu_select.lower() == "bh":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(2,convert)
            to_hexadecimal = decimal_to_hexadecimal(to_decimal)
            print(convert," from binary to hexadecimal is ",to_hexadecimal)
            
        elif menu_select.lower() == "od":
            convert = float(input("Enter value to convert: "))
            print(convert," from octal to decimal is ",convert_to_decimal(8,convert))
            
        elif menu_select.lower() == "ob":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(8,convert)
            to_binary = decimal_to_binary(to_decimal)
            print(convert," from octal to binary is ",to_binary)
            
        elif menu_select.lower() == "oh":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(8,convert)
            to_hexadecimal = decimal_to_hexadecimal(to_decimal)
            print(convert," from octal to hexadecimal is ",to_hexadecimal)
            
        elif menu_select.lower() == "hd":
            convert = float(input("Enter value to convert: "))
            print(convert," from hexadecimal to decimal is ",convert_to_decimal(16,convert))
            
        elif menu_select.lower() == "hb":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(16,convert)
            to_binary = decimal_to_binary(to_decimal)
            print(convert," from hexadecimal to binary is ",to_binary)
            
        elif menu_select.lower() == "ho":
            convert = float(input("Enter value to convert: "))
            to_decimal = convert_to_decimal(16,convert)
            to_octal = decimal_to_octal(to_decimal)
            print(convert," from hexadecimal to octal is ",to_octal)
            
        print("Unknown response, please try again")
        menu_select = input("Please choose an option from the above menu: ")

main()

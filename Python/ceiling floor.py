#####################################################################
# Author: Kevin Zhang
# Date: 12/20/2014
# purpose: calculate ceiling and floor values
#####################################################################

def ceiling(c):
########################################
# purpose: does ceiling operations
########################################

    if (int(float(c)) > 0) == True:
        
        return (int(float(c)) + 1)

    else:
        
        return (int(float(c)))


def floor(f):
#####################################
# purpose: does floor operations
#####################################

    if (int(float(f)) > 0) == True:
        
        return (int(float(f)))

    else:
        
        return (int(float(f)) - 1)


def main():
    print("""
        MENU
        ceiling: c
        floor: f
        quit: q
        """)

    print("--------------------------------------------------------------------------------")

    response = input("What would you like to do?: ")

    while (True):
        
        if response.lower()== "q":
            
            print("Thanks for Playing!")
            
            quit()
            

        elif response.lower() == "c":

            compute = input("Enter value to take ceiling of: ")

            print("""
            MENU
            -------------------------------------------------------------
            addition: add
            subtraction: sub
            NOTES: only add 1 space between addition or subtraction signs
            """)
            
            question = input("Would you like to add or subtract a number?: (Y/N) ")
            if question.lower() == "y": 
                menu_select = input("Please select an option from the above menu: ")
                
                if menu_select.lower() == "add":
                    find = compute.find("+")
                    ceiling_operation = float(compute[:find])
                    arithmetic = float(compute[find+2:])
                    print("The ceiling of ",ceiling_operation," + ",arithmetic,"is ", ceiling(ceiling_operation) + arithmetic)
                    
                elif menu_select.lower() == "sub":
                    find = compute.find("-")
                    find1 = compute[find+1:].find("-")
                    ceiling_operation = float(compute[:find1])
                    arithmetic = float(compute[find1+2:])
                    print("The ceiling of ",ceiling_operation," - ",arithmetic,"is ", ceiling(ceiling_operation) - arithmetic)
                    
            elif question.lower() == "n":
                print("The ceiling of ",compute,"is ", ceiling(compute))

            else:
                print("Unknown response, please try again")
                question = input("Would you like to add or subtract a number?: (Y/N) ")

            response = input("What would you like to do?: ")

        elif response.lower() == "f":
        
            compute = input("Enter value to take ceiling of: ")

            print("""
            MENU
            addition: add
            subtraction: sub
            NOTES: only add 1 space between addition or subtraction signs
            """)
            
            question = input("Would you like to add or subtract a number?: (Y/N) ")
            if question.lower() == "y": 
                menu_select = input("Please select an option from the above menu: ")
                
                if menu_select.lower() == "add":
                    find = compute.find("+")
                    floor_operation = float(compute[:find])
                    arithmetic = float(compute[find+2:])
                    print("The floor of ",floor_operation," + ",arithmetic,"is ", floor(floor_operation) + arithmetic)
                    
                elif menu_select.lower() == "sub":
                    find = compute.find("-")
                    find1 = compute[find+1:].find("-")
                    floor_operation = float(compute[:find1])
                    arithmetic = float(compute[find1+2:])
                    print("The floor of ",floor_operation," - ",arithmetic,"is ", floor(floor_operation) - arithmetic)
                    
            elif question.lower() == "n":
                print("The floor of ",compute,"is ", floor(compute))

            else:
                print("Unknown response, please try again")
                question = input("Would you like to add or subtract a number?: (Y/N) ")

        print("Unknown response, please try again")
        response = input("What would you like to do?: ")

main()

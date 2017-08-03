num = input("Enter a number: ")
while((num.isdigit() == False) or (int(num) < 0)):
    print("Invalid Input")
else:
    divide = input("Split by what integer?: ")
    count = 0
    save=''
    for x in num:
        if count <= int(divide)-1:
            c = x
            save = c
            count += 1
        if count == int(divide):
            count = 0
            save += ' '
        print(save, end='')
            


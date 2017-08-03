"""Calendar"""
from time import sleep, strftime
FIRSTNAME = input("What is your name? ")

calendar = {}
def welcome(FIRSTNAME):
  print("Welcome " + FIRSTNAME)
  print("starting up the calendar")
  sleep(1)
  print( strftime("%A %B, %d %Y") )
  print(strftime("%H:%M:%S"))
  print("What would you like to do?")


def start_calendar():
  welcome(FIRSTNAME)
  start = True
  while (start):
    print("""MENU
    Add: A
    Update: U
    View: V
    Delete: D
    Exit: X""")
    user_choice = input("Make a selection: ").upper()
    if user_choice == "V":
      if (len(calendar.keys()) < 1):
        print("Empty Calendar")
      else:
        print(calendar)

    elif (user_choice == "U"):
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print(calendar)
    
    elif (user_choice == "A"):
      event = input("Enter event: ")
      date =input("Enter date (MM/DD/YYYY): ")
      if ( len(date)!= 10 or int( date[6:] ) < int( strftime("%Y") )) :
        try_again = input("Try Again? Y for Yes, N for No: ").upper()
        if (try_again == "Y"):
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("Event added to calendar!")
        print(calendar)
    
    elif (user_choice == "D"):
      if ( len(calendar.keys()) < 0 ):
        print("Empty!")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if (event == calendar[date]):
            del calendar[date]
            print("Event removed")
          else:
            print("Event not found")
    
    elif (user_choice == "X"):
      print("Quiting program")
      start = False
  
    else:
      print("Invalid")
      start = False
start_calendar()

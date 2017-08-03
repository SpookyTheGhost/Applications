def rgbHex():
  R = input("Enter a value for Red: ")
  G = input("Enter a value for Green: ")
  B = input("Enter a value for Blue: ")
  
  try:
    R = int(R)
    G = int(G)
    B = int(B)
  except TypeError:
    pass
  except ValueError:
    pass
  
  if (R < 0 or R > 255 or G < 0 or G > 255 or B < 0 or B > 255):
    print("Invalid RGB value to convert")
    return
    
  val = (R << 16) + (G << 8) + B
  HEX = hex(val)
  print(HEX[2:].upper())
  return HEX

def hexRGB():
  hexVal = input("Enter a hex value to convert: ")
  if (len(hexVal) != 6):
    print("Invalid Hexcode")
    return
  else:
    hexVal = int(hexVal, 16)
    twoHexDigits = 2**8
    blue = hexVal % twoHexDigits
    hexVal = hexVal >> 8
    green =  hexVal % twoHexDigits
    hexVal = hexVal >> 8
    red = hexVal % twoHexDigits
    print("%s%s%s" % (red, green, blue))
    
def convert():
  option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to quit: ")
  
  if (option == "1"):
    print("RGB to HEX")
    rgbHex()
  elif (option == "2"):
    print("HEX to RGB")
    hexRGB()
  elif (option.lower() == "x"):
    print("Goodbye!")
    quit()
  else:
    print("Invalid input")
convert()

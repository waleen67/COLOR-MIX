print("Mix two colors: red, blue, yellow, green, orange, purple, black, white")

color1 = input("First color: ").lower()
color2 = input("Second color: ").lower()

if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("You get PURPLE!")
    
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("You get ORANGE!")
    
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("You get GREEN!")

elif (color1 == "red" and color2 == "purple") or (color1 == "purple" and color2 == "red"):
    print("You get RED-PURPLE (Magenta)!")
    
elif (color1 == "blue" and color2 == "purple") or (color1 == "purple" and color2 == "blue"):
    print("You get BLUE-PURPLE (Violet)!")
    
elif (color1 == "red" and color2 == "orange") or (color1 == "orange" and color2 == "red"):
    print("You get RED-ORANGE!")
    
elif (color1 == "yellow" and color2 == "orange") or (color1 == "orange" and color2 == "yellow"):
    print("You get YELLOW-ORANGE!")
    
elif (color1 == "blue" and color2 == "green") or (color1 == "green" and color2 == "blue"):
    print("You get BLUE-GREEN (Cyan)!")
    
elif (color1 == "yellow" and color2 == "green") or (color1 == "green" and color2 == "yellow"):
    print("You get YELLOW-GREEN!")

elif (color1 == "black" and color2 == "red") or (color1 == "red" and color2 == "black"):
    print("You get DARK RED!")
    
elif (color1 == "black" and color2 == "blue") or (color1 == "blue" and color2 == "black"):
    print("You get DARK BLUE!")
    
elif (color1 == "black" and color2 == "yellow") or (color1 == "yellow" and color2 == "black"):
    print("You get DARK YELLOW (Olive)!")
    
elif (color1 == "black" and color2 == "green") or (color1 == "green" and color2 == "black"):
    print("You get DARK GREEN!")
    
elif (color1 == "black" and color2 == "purple") or (color1 == "purple" and color2 == "black"):
    print("You get DARK PURPLE!")
    
elif (color1 == "black" and color2 == "orange") or (color1 == "orange" and color2 == "black"):
    print("You get DARK ORANGE (Brown)!")

elif (color1 == "white" and color2 == "red") or (color1 == "red" and color2 == "white"):
    print("You get PINK!")
    
elif (color1 == "white" and color2 == "blue") or (color1 == "blue" and color2 == "white"):
    print("You get LIGHT BLUE!")
    
elif (color1 == "white" and color2 == "yellow") or (color1 == "yellow" and color2 == "white"):
    print("You get LIGHT YELLOW!")
    
elif (color1 == "white" and color2 == "green") or (color1 == "green" and color2 == "white"):
    print("You get LIGHT GREEN!")
    
elif (color1 == "white" and color2 == "purple") or (color1 == "purple" and color2 == "white"):
    print("You get LAVENDER!")
    
elif (color1 == "white" and color2 == "orange") or (color1 == "orange" and color2 == "white"):
    print("You get PEACH!")

elif (color1 == "black" and color2 == "white") or (color1 == "white" and color2 == "black"):

elif color1 == color2:
    print(f"You get {color1.upper()}!")


else:
    print("I don't know that mix")

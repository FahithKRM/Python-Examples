#user input is speed result is which gear

speed = int(input("User enter the speed (in Kmph): "))

if speed >=0 and speed < 25 : 
    print("Gear is 1")
elif speed >=25 and speed < 35 : 
    print("Gear is 2")
elif speed >=35 and speed < 50 : 
    print("Gear is 3")
elif speed >=50 and speed < 80 : 
    print("Gear is 4")
elif speed >=80 : 
    print("Gear is 5")
else :
    print("Gear is revered")

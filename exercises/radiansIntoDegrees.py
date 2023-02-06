#Convert radians into degrees
import math

def radians_to_degress(radians):
    degrees = radians * 180 / math.pi
    return degrees

#Convert degrees into radians
def degrees_to_radians(degrees):
    radians = degrees * math.pi / 180
    return radians

#Convert degrees, minutes, and seconds into degrees
def dms_to_degrees(degrees, minutes, seconds):
    degrees = degrees + minutes / 60 + seconds / 3600
    return degrees

#Convert degrees into degrees, minutes, and seconds
def degrees_to_dms(degrees):
    minutes = (degrees - int(degrees)) * 60
    seconds = (minutes - int(minutes)) * 60
    degrees = int(degrees)
    minutes = int(minutes)
    return degrees, minutes, seconds


def execute():
    print("1. Convert radians into degrees")
    print("2. Convert degrees into radians")
    print("3. Convert degrees, minutes, and seconds into degrees")
    print("4. Convert degrees into degrees, minutes, and seconds")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        radians = float(input("Enter radians: "))
        print(radians_to_degress(radians))
    elif choice == 2:
        degrees = float(input("Enter degrees: "))
        print(degrees_to_radians(degrees))
    elif choice == 3:
        degrees = float(input("Enter degrees: "))
        minutes = float(input("Enter minutes: "))
        seconds = float(input("Enter seconds: "))
        print(dms_to_degrees(degrees, minutes, seconds))
    elif choice == 4:
        degrees = float(input("Enter degrees: "))
        print(degrees_to_dms(degrees))
    elif choice == 5:
        quit()
    else:
        print("Invalid choice")
    execute() #Recursion

execute()
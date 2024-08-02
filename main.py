# Project: Calculating volume of some common Solid / 3D Shapes

from math import pi
from time import sleep

def cube():
    print("\n*** Calculating the Volume of a Cube ***")
    a = float(input("\nEnter the length of sides: "))
    v = a ** 3
    print(f"\nThe volume of this Cube = {v} (units)³")

def cuboid():
    print("\n*** Calculating the Volume of a Cuboid ***")
    l = float(input("\nEnter the length: "))
    w = float(input("Enter the width: "))
    h = float(input("Enter the height: "))
    v = l * w * h
    print(f"\nThe volume of this Cuboid = {v} (units)³")

def cylinder():
    print("\n*** Calculating the Volume of a Cylinder ***")
    r = float(input("\nEnter the radius of the circular base: "))
    h = float(input("Enter the height: "))
    v = pi * (r**2) * h
    print(f"\nThe volume of this Cylinder = {v} (units)³")

def sphere():
    print("\n*** Calculating the Volume of a Sphere ***")
    r = float(input("\nEnter the radius: "))
    v = (4/3) * pi * (r**3)
    print(f"\nThe volume of this Sphere = {v} (units)³")

def hemisphere():
    print("\n*** Calculating the Volume of a Hemisphere ***")
    r = float(input("\nEnter the radius: "))
    v = (2/3) * pi * (r**3)
    print(f"\nThe volume of this Hemisphere = {v} (units)³")

def cone():
    print("\n*** Calculating the Volume of a Cone ***")
    r = float(input("\nEnter the base radius of the Cone: "))
    h = float(input("Enter the height of the Cone: "))
    v = pi * (r**2) * (h/3)
    print(f"\nThe volume of this Cone = {v} (units)³")

def prism():
    print("\n*** Calculating the Volume of a Prism ***")
    B = float(input("\nArea of the base (i.e. length x width or side²): "))
    h = float(input("Enter the height: "))
    v = B * h
    print(f"\nThe volume of this Prism = {v} (units)³")

def pyramid():
    print("\n*** Calculating the Volume of a Pyramid ***")
    B = float(input("\nEnter the area of the base: "))
    h = float(input("Enter the height of the Pyramid: "))
    v = (1/3) * B * h
    print(f"\nThe volume of this Pyramid = {v} (units)³")

def sq_rec_pyramid():
    print("\n*** Calculating the Volume of a Square or Rectangular Pyramid ***")
    l = float(input("\nEnter the length of the base: "))
    w = float(input("Enter the width of the base: "))
    h = float(input("Enter the height (from base to tip): "))
    v = (1/3) * l * w * h
    print(f"\nThe volume of this Square or Rectangular Pyramid = {v} (units)³")

# Creating Main Menu and Options for the user using loop

while True:
    print("\n----------------------------------------------")
    print("|       ***** Volume Calculator *****        |")
    print("----------------------------------------------")
    
    choice = int(input("\nPress 1 - Cube\nPress 2 - Cuboid\nPress 3 - Cylinder\nPress 4 - Sphere\nPress 5 - Hemisphere \nPress 6 - Cone\nPress 7 - Prism\nPress 8 - Pyramid\nPress 9 - Square or Rectangle Pyramid\nPress 10 - Quit/Exit\n\nEnter your choice: "))

    if choice<1 or choice>10:
        print("\nInvalid Choice, Enter a number between 1 and 10")

    elif choice == 1:
        cube()

    elif choice == 2:
        cuboid()

    elif choice == 3:
        cylinder()

    elif choice == 4:
        sphere()

    elif choice == 5:
        hemisphere()

    elif choice == 6:
        cone()

    elif choice == 7:
        prism()

    elif choice == 8:
        pyramid()

    elif choice == 9:
        sq_rec_pyramid()

    elif choice == 10:
        print("\nQuitting the Program\n")
        sleep(2)
        break
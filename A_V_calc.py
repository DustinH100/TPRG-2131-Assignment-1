#TPRG 2131 A_V_calc.py A simplistic Area/Volume calculator
#TPRG 2131 Fall 2023 Assignment 1
#Oct 15, 2023
#Dustin Horne, 100844416
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
'''
*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

#from assertions import add2
import math
import sys

if __name__ == "__main__":

def arec(leng, wid):    #Calculates the area of a rectangle
    return print(leng*wid)

def asqr(leng):    #Calculates the area of a square
    return print(leng**2)

def acir(radi):    #Calculates the area of a circle
    return print(math.pi*radi**2)

def acub(leng):    #Calculates the area of a cube
    return print(6*(leng**2))

def vcub(leng):    #Calculates the volume of a cube
    return print(leng**3)

while True:
    select = input("""Enter V/v for a detailed calculation or D/d for the default view
    or press Q/q to quit """)
    
    if select == "Q" or select == "q":
        sys.exit(0)
        
    if select == "D" or select == "d":
        dcalc = int(input("""Which calculation using the designated number
        1.Area of a Square
        2.Area of a Rectangle
        3.Area of a Circle
        4.Area of a Cube
        5.Volume of a Cube
        """))
        
        if dcalc == 1:
            leng = float(input("What is the length? "))
            print(leng, "^2", "=", asqr(leng))
            
        if dcalc == 2:
            leng = float(input("What is the length? "))
            wid = float(input("What is the width? "))
            print(leng, "*", wid, "=", arec(leng, wid))
        
        if dcalc == 3:
            radi = float(input("What is the radius? "))
            print("3.14", "*", radi, "=", acir(radi))
            
        if dcalc == 4:
            leng = float(input("What is the length? "))
            print("6", "*", leng, "^2", "=", acub(leng))
        
        if dcalc == 5:
            leng = float(input("What is the length? "))
            print(leng, "^3", "=", vcub(leng))
        
    if select == "V" or select == "v":
        vcalc = int(input("""Which calculation using the designated number
        1.Area of a Square
        2.Area of a Rectangle
        3.Area of a Circle
        4.Area of a Cube
        5.Volume of a Cube
        """))
        
        if vcalc == 1:
            leng = float(input("What is the length? "))
            print(leng, "^2", "=", asqr(leng), "length^2")
            
        if vcalc == 2:
            leng = float(input("What is the length? "))
            wid = float(input("What is the width? "))
            print(leng, "*", wid, "=", arec(leng, wid), "length * width")
        
        if vcalc == 3:
            radi = float(input("What is the radius? "))
            print("3.14", "*", radi, "=", acir(radi), "pi*r^2")
            
        if vcalc == 4:
            leng = float(input("What is the length? "))
            print("6", "*", leng, "^2", "=", acub(leng), "6*length^2")
        
        if vcalc == 5:
            leng = float(input("What is the length? "))
            print(leng, "^3", "=", vcub(leng), "length^3")
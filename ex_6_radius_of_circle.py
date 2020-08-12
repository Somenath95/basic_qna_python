#Find the Area of a circle, given pi = 3.141

n = input("Enter the radius of a circle: ")
pi = 3.141
try:
    radi = float(n)
    area = (pi * (radi ** 2))
    print("Area of the circle is:",area)
except:
    print("Please insert a valid number")    
    quit()
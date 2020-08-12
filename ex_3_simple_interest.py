#Program to find the simple interest of a given capital

cap = input("Enter the Capital: ")
interest = input("Enter the annual interest: ")
time = input("Enter the investment year: ")

try:
    p = int(cap)
    r = float(interest)
    t = int(time)
except:
    print("Please give valid number")    
    quit()

simple_interest = (p * r *t)/100

print("The simple interest will be: ",simple_interest)
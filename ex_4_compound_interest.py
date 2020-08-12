#Program to find the compound interest of a given capital

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

compound_interest = p * (1 + r / 100) ** t
print("The compound interest will be: ", compound_interest)
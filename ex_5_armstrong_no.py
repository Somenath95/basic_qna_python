#Program to find whether a number is armstrong or not

n = input("Enter the number: ")

try:
    num = int(n)
except:
    print("Please enter a valid number.")
    quit()    
count = order(num)

print(count)
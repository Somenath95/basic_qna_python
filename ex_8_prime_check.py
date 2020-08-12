#Program to check whether as number is Prime or not

n = input("Enter the number:")

try:
    num = int(n)
except:
    print("Please enter a valid number.")
    quit()

count = 0
for i in range(1, num):
    if(num % i == 0):
        count = count + 1

if(count > 1):
    print('False')
elif(count == 1):
    print('True')
else:
    print("Something's Wrong!")    
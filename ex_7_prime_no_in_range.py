#Print all the prime numbers in the given range

n = int(input("Enter the range: "))

for num in range(1, n+1):
    count = 0
    for i in range(1, num):
        if(num % i == 0):
            count = count+1

    if(count > 2):
        continue
    elif(count == 1):
        print(num)
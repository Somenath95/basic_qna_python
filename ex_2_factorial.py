#Find factorial of a number using **Recursion**

#define factorial **Recursion**
def fun_factorial(value):
    if(value == 0) | (value == 1):
        return 1
    elif(n < 0):
        return "NA"    
    else:
        return (value * fun_factorial(value-1))

#Actual Code
num = input("Enter the number: ")

try:
    n = int(num)
    fact_num = fun_factorial(n)
    print("The Factorial of",n ,"is:", fact_num)
except:
    print("Please enter a valid number")    
    quit()

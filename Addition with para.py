

def addition(num1,num2):
    sum = 0
    for i in range(num1,num2+1):

        sum +=i


    print("The sum of the numbers between",num1,"and" ,num2, "is", sum)


num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
addition(num1,num2)
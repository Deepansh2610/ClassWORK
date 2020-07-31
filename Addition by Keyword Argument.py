def addition(num1,num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i


n1 = int(input("Enter the 1st number"))
n2 = int(input("Enter the 2nd number"))
addition(n1,n2)
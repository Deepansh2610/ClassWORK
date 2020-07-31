def addition(num1,num2=20):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
    print("sum from",num1,"to",num2,"is",sum)


num1 = int(input("Enter the 1st number"))

addition(num1)
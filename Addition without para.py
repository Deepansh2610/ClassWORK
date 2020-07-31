def addition():
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
    print("sum from",num1,"to",num2,"is",sum)
    return sum
num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd number"))
addition()



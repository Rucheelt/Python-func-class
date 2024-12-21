def refact(n):
    if n==1:
        return n
    else:
        return n*refact(n-1)

num=int(input("Enter the number for factorial: "))
if num<0:
    print("the number is in negative there is no factorial")
elif num==0:
    print("there is no factorial for the no. 0")
else:
    print("The factorial of the given number is: ", refact(num))
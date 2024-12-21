def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def exp(x,y):
    return x**y
def rem(x,y):
    return x%y

n1=int(input("Enter the first num : "))
n2=int(input("Enter the second num : "))

print("Addition : ", add(n1,n2))
print("Subtraction : ", sub(n1,n2))
print("Multiplication : ", mul(n1,n2))
print("Division : ", div(n1,n2))
print("Exponents : ", exp(n1,n2))
print("Remainder : ", rem(n1,n2))
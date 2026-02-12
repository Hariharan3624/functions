def add(p, q):
    return p+q
def subtract(p, q):
    return p-q
def multiply(p, q):
    return p*q
def divide(p, q):
    return p/q
print("please select the operation")
print("+ is addition")
print("- is subtraction")
print("* is multiplication")
print("/ is division")
choice = input("please chose your choice +,-,*,/: ")
num1 = int(input("please type in your first number: "))
num2 = int(input("please type in your second number: "))
if choice == "+":
    print(num1,"+",num2,"=",add(num1, num2))
elif choice == "-":
    print(num1,"-",num2,"=",subtract(num1, num2))
elif choice == "*":
    print(num1,"*",num2,"=",multiply(num1, num2))
elif choice == "+":
    print(num1,"+",num2,"=",add(num1, num2))
elif choice == "+":
    print(num1,"+",num2,"=",add(num1, num2))
elif choice == "/":
    print(num1,"/",num2,"=",divide(num1, num2))
else:
    print("invalid input")



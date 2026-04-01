#simple calculator by KALULE FAHAD
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0: 
        return "Math Error! Divsion by Zero"
    return x / y
print("select an operations")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.Divide")
#takes users choice
choice = input("Enter choice (1, 2, 3, 4):")
#Takes user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#performs tasks  based on user choice
if choice == '1':
    print("Answer:", add(num1, num2))
elif choice == '2':
    print("Answer:", subtract(num1, num2))
elif choice == '3':
    print("Answer:", multiply(num1, num2))
elif choice == '4':
    print("Answer:", divide(num1, num2))
else:
    print("invalid input") #handles wrong inputs





#program to make a simple calculator




#this function adds two numbers
def add(x, y):
    return x + y


#this function subtracts two numbers
def subtract(x, y):
    return x - y

#this function factors two numbers
def multiply(x, y):
    return x * y

#this function divides two numbers
def divide(x, y):
    return x / y

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #take input from user
    choice = input("enter choice(1/2/3/4):")

#check if choice is from the four options
if choice in ('1','2','3','4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter first second: "))

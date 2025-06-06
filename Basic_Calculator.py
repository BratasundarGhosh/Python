#Display calculator menu
print("Welcome to basic calculator")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

#Get users choice
choice=int(input("Select your opration {1/2/3/4}:"))

#Get input from users
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))

#Perform the operation based on user choice
if(choice==1):
    print(f"The result of Addition: {num1+num2}")   
elif(choice==2):
    print(f"The result of Subtraction: {num1-num2}")
elif(choice==3):
    print(f"The result of Multiplication: {num1*num2}")
elif(choice==4):
    if num2 != 0:
        print(f"The result of Division: {num1/num2}")
    else:
        print("error: Divion with zero is not allowed")
else:
    print("Invalid choice")
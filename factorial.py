#Method-1
# a = int(input("Enter a number: "))
# num = []
# if a<0:
#     print("Factoril isn't defind for negative numbrs.")
# else:
#     while 1<=a:
#         num.append(a)
#         a=a-1
#     num.sort()
#     factorial=1
#     for dig in num:
#         factorial = factorial * dig
#     print("Factorial of the number is: ", factorial)

#Method-2
# import math
# a= int(input("Enter a number: "))
# if a<0:
#     print("Factorial isn't defined for negative numbers.")
# else:
#     print("Factorial of the number is: ",math.factorial(a))

#Method-3
a=int(input("Enter a number: "))
factorial=1
if a<0:
    print("Factorial is not defined for negtive numbers.")
else:
    for num in range(1,a+1):
        factorial = factorial * num
    print("Factorial of the number is: ",factorial)
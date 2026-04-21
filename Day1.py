print("Hello world")
# ---------------------------------
a =3
b= 7
c = a+b
print(a+b)
print(type(a))
print(type(c))
# ---------------------------------
# num1=int(input("Enter the first number"))
# num2=int(input("Enter the second number"))
# num3= num1 + num2
# num4= num1 - num2
# num5= num1*num2
# num6= num1/num2
# num7= num1-num2
# print("Sum of two numbers", num3)
# print("Subtract of two numbers", num4)
# print("Multiply the two numbers", num5)
# print("Divide two numbers",num6)
# print(f"Module of {num1} and {num2} is {num7}")
# ------------------------------------------------

num = 5+4j
print(type(num))
# -----------------------------------------------

# num1=int(input("Enter the first number"))
# num2=int(input("Entr the second number"))
# if num1>num2:
#     print("Greatest number=", num1)
# else:
#     print("Greatest number=", num2)
# ----------------------------------------------

def add(a, b):
    return a + b

result = add(5, 3)
print(result)
# ----------------------------------------------

a=int(input("Enter the number"))
if(a%2)==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

# -----------------------------------------------

n=int(input("Enter the number to be checked"))
if n>0:
    print(f"{n} is positive number")
elif n<0:
    print(f"{n} is negative number")
else:
    print("The Number is zero")

# -------------------------------------------------

n1=int(input("Enter the 1st number"))
n2=int(input("Enter the 2st number"))
n3=int(input("Enter the 3st number"))
n4=int(input("Enter the 4st number"))

greatest = max(n1, n2, n3, n4)
# condition lagaiyoo
if(n1>=n2) and (n1>=n3) and (n1>=n4):
    greatest =n1
elif(n2>=n1) and (n2>=n3) and (n2>=n4):
    greatest =n2
elif(n3>=n2) and (n3>=n1) and (n3>=n4):
    greatest =n3
else :
    greatest=n4
print(f"Enter numbers:{n1},{n2},{n3},{n4}")
print(f"The greatest number is",greatest)

# ------------------------------------------------

grade = float(input("Enter the garde you achieve:"))
print(f"Your total marks is {grade}")

if grade >=80:
    print("Distinction")
elif grade >=70:
    print("1st division")
elif grade >= 60:
    print("2nd Division")
elif grade >= 50:
    print("3rd Division")
else:
    print ("Failed")
# ======================================================

num1=int(input("Enter the first number"))
num2=int(input("Entr the second number"))
num3=int(input("Enter the third number"))

print(f"Enter numbers is {num1}, {num2}, {num3}")
if num1<=num2 and num1<=num3:
    print("Smallest number=", num1)
elif num2<=num1 and num2<=num3:
    print("Smallest number=", num2)
else:
    print("Smallest number=",num3)
# --------------------------------------------------------


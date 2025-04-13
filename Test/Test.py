#a = input('Enter a number:')
#print(a)
#to only intiger
#b = int(input('Enter a number:'))
#print(b)
#to float
#c = float(input('Enter a number:'))
#print(c)
#program to read ASCII value of the given character
#d='p'
#print("The ASCII value of '"+ d +"' is",ord(d))
#python program to find largest of two numbers

a=float(input("Enter number 1:"))
b=float(input("Enter number 2:"))

if(a>b):
    print("{0} is Greater than {1}".format(a,b))
elif(b>a):
    print("{0} is Greater than {1}".format(b,a))
else:
    print("Both a and b are Equal")

#==========================OR=========================

print("Enter two Numbers:")
numOne = int(input())
numTwo = int(input())

if numOne>numTwo:
    print("\nLargest Number =",numOne)
else:
     print("\nLargest Number =",numTwo)
# program to find odd or even
num = int(input("Enter any number to check odd or even:"))
if(num % 2)== 0:
    print("The number is Even")
else:
    print("The number is Odd")

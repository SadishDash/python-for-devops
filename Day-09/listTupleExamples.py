import os,sys

name = input("Enter your name:-")
number = int(input("Please enter a number to get square:-"))
num = int(sys.argv[1])

print("Your name is", name, "and the square of the number is",number*number+num+int(os.getenv("num2")))


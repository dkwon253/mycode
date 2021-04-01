#!/usr/bin/env python3

# addition function
def addition(num1, num2):
    return num1 + num2


# subtraction function
def subtract(num1, num2):
    return num1 - num2


# multiplication function
def multiply(num1, num2):
    return num1 * num2


# division function
def divide(num1, num2):
    if num2 == 0:
        print("You cannot divide by zero, dummy!")
    return num1 / num2


print("Please choose the following operations:\n1. Addition, 2. Subtraction,"
      " 3. Multiplication, 4. Division")

user_input = input("\nSelect from the following operations above to perform. ")

input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))

if user_input == "1" or user_input.lower() == "addition":
    print(input1, "+", input2, "=", addition(input1, input2))

elif user_input == "2" or user_input.lower() == "subtraction":
    print(input1, "-", input2, "=", subtract(input1, input2))

elif user_input == "3" or user_input.lower() == "multiplication":
    print(input1, "x", input2, "=", multiply(input1, input2))

elif user_input == "4" or user_input.lower() == "division":
    print(input1, "/", input2, "=", divide(input1, input2))

else:
    print("You have entered an invalid input.")


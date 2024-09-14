#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      akppa
#
# Created:     09-09-2024
# Copyright:   (c) akppa 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Simple Calculator")
print("Select arithmetic operation for calculation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

Operation=int(input("Select the index of operation you want to perform. Like 1 for add..etc"))

if Operation == 1:
    data = []
    while True:
        try:
            number = float(input("Enter the number: "))
            data.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        choice = input("Add other number (y/n): ")
        if choice.casefold() == "n":
            break
    sum_data=0
    for i in data:
        sum_data+=i
        print("Sum of the numbers is :",sum_data)

elif Operation == 2:
    data = []
    while True:
        try:
            number = float(input("Enter the number: "))
            data.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        choice = input("Add other number (y/n): ")
        if choice.casefold() == "n":
            break
    diff_data=data[0]
    for i in data[1:]:
        diff_data-=i
        print("Difference of the numbers is :",diff_data)

elif Operation == 3:
    data = []
    while True:
        try:
            number = float(input("Enter the number: "))
            data.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        choice = input("Add other number (y/n): ")
        if choice.casefold() == "n":
            break
    mult_data=1
    for i in data:
        mult_data*=i
        print("Product of the numbers is :",mult_data)

elif Operation == 4:
    data = []
    while True:
        try:
            number = float(input("Enter the number: "))
            data.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        choice = input("Add other number (y/n): ")
        if choice.casefold() == "n":
            break
    div_data=data[0]
    for i in data[1:]:
        div_data/=i
        print("On dividing we get :",div_data)

else:
    print("Invalid operation. Please select a valid index.")


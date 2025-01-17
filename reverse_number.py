num = int(input("Enter the number: "))
temp = 0
print("The reversed number is: ", end="")
while num != 0:
    temp = num % 10  # Extracts the last digit of the number
    print(temp, end="")  # Prints the extracted digit
    num = num // 10  # Removes the last digit from the number

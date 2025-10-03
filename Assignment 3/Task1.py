# Calculate Factorial Using a loop

# function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
num =int(input("Enter a number: \n"))
print("Factorial of", num, "is:", factorial(num))
print("\t\t\t Thankyou! Have a nice Day")

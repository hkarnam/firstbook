n = int(input("enter the number of factorial: "))
factorial = 1 # initializing a variable with 1
while(n>0):  # condition is true unless n becomes 0
    factorial = factorial * n # updating factorial variable with sequential multiplication of decremented numbers
    n = n - 1  # decrementing the n value to multiply in next sequence

print(f"Factorial of given number is {factorial}")



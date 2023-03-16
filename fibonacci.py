# user generated input values to add initially
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
n = int(input("number of sequences needed"))
print(a,b, end = " ")
while(n-2):  # we need 3 more sequences left to have, so n-2 condition is used to make the value 0
    c = a + b
    a = b # assigning the second value as first number
    b = c # the added number in sequence gets the second position
    print(c, end = " ")
    n = n-1  # decrementing the n value to make while loop condition false

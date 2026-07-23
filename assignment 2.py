'''x = int(input("Enter a number: "))

s = 0

for i in range(1, x):
    if x % i == 0:
        s = s + i  # Indented to belong inside the 'if' block

# Unindented so the check happens AFTER the loop finishes
if s == x:
    print("It's a perfect number")
else:
    print("It's an imperfect number")'''




'''x = int(input("Enter a number: "))

y = str(x)

# Use '==' to check if the reversed string equals the original string
if y[-1::-1] == y:
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")'''



x = int(input("Enter 5-digit number: "))

if x > 9999 and x < 100000:
    y = str(x)
    print(y[1::2])  # Prints characters at index 1 and 3
else:
    print("ENTER A NUMBER OF 5-DIGIT")

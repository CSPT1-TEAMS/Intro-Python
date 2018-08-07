# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
# num = input("Enter a number: ")
# will not work if its a str and not a number

num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"
def iseven( num ):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd")

iseven(num)
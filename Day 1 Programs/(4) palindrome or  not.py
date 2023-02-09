def is_palindrome(x):
    if x<0:
        return False
    return str(x)==str(x)[::-1]

x=int(input("Enter an integer: "))
result = is_palindrome(x)
if result:
    print("The integer is a palindrome.")
else:
    print("The integer is not a palindrome.")

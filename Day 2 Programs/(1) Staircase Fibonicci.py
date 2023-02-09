def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def waycount(n):
    return fibonacci(n+1)

n=int(input("Enter the Number"))
print("The number of ways to reach the top of a staircase with", n, "steps is", fibonacci(n))

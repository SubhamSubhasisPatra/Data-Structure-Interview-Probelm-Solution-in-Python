"""
 When the function calls itself is called a recursive call. 

"""

def factorial(n):
    """
    Gives the factorial of number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(5))

"""
 When the function calls itself is called as a recursive call .. 

"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(5))

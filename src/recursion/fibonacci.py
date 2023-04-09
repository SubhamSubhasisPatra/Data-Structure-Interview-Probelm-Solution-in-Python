"""
                    nth_fibonacci(4)
                   /                 \
      nth_fibonacci(3)            nth_fibonacci(2)
         /           \              /          \
nth_fibonacci(2) nth_fibonacci(1) nth_fibonacci(1) nth_fibonacci(0)
    /        \
nth_fibonacci(1) nth_fibonacci(0)

"""

def nth_fibonacci(n):
    """
    This function calculates the nth Fibonacci number using recursion.

    :param n: int, the position of the Fibonacci number to be calculated
    :return: int, the nth Fibonacci number
    """
    # Base cases
    if n <= 1:
        return 1

    # Recursive case
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


if __name__ == '__main__':
    result = nth_fibonacci(4)
    print(result)

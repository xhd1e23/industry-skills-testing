def factorial(n):
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

def fib(n: int) -> int:
    """
    Fibonacci

    :param n: a number
    :return: Fibonacci of n
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

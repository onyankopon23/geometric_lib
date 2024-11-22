def area(a):
    if a <= 0:
        raise ValueError("Side length must be a positive number.")
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError("Side length must be a positive number.")
    return 4 * a

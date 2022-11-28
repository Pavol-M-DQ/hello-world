import math


def eval_poly(poly: list, x: float) -> float:
    """
    Evaluate polynomial at x
    :param poly:
    :param x: float
    :return:
    """
    # Initialize result
    result = poly[0]

    # Evaluate value of polynomial
    # using Horner's method
    for i in range(1, len(poly)):
        result = result * x + poly[i]

    return result


def interval_bisection(coefficients: list, interval: list, accuracy: float) -> float:
    """
    returns a root of a polynomial with coefficients entered as list with required accuracy on the entered interval
    coefficients: list of coefficients for the polynomial
    interval: interval where to look for the root
    accuracy: float, convergence criteria the search will stop when the f(root) <= accuracy
    """

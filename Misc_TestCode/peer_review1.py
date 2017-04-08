import math


def polysum (n, s):
    """
    input: n (unsigned int) number of sides, s (float or int) length of each side
    return: (float) area + perimeter^2
    """
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    perimeter = n * s
    return round(area + perimeter ** 2, 4)
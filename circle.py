import math

def ensure_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number")
    return float(x)

def ensure_non_negative(x, name="value"):
    x = ensure_number(x, name)
    if x < 0:
        raise ValueError(f"{name} must be non-negative")
    return x

def area(r):
    """Принимает r (радиус) и возвращает площадь круга.
    Если r < 0 -> ValueError. Если тип не число -> TypeError.
    """
    r = ensure_non_negative(r, "r")
    return math.pi * r * r

def perimeter(r):
    """Принимает r (радиус) и возвращает периметр круга."""
    r = ensure_non_negative(r, "r")
    return 2 * math.pi * r

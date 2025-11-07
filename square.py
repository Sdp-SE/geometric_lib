def ensure_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number")
    return float(x)

def ensure_non_negative(x, name="value"):
    x = ensure_number(x, name)
    if x < 0:
        raise ValueError(f"{name} must be non-negative")
    return x

def area(a):
    """Площадь квадрата a*a. Если a<0 -> ValueError."""
    a = ensure_non_negative(a, "a")
    return a * a

def perimeter(a):
    """Периметр квадрата 4*a. Если a<0 -> ValueError."""
    a = ensure_non_negative(a, "a")
    return 4 * a


def ensure_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number")
    return float(x)

def ensure_non_negative(x, name="value"):
    x = ensure_number(x, name)
    if x < 0:
        raise ValueError(f"{name} must be non-negative")
    return x

def area(a, h):
    """Площадь треугольника a*h/2. Проверяет, что a и h >= 0."""
    a = ensure_non_negative(a, "a")
    h = ensure_non_negative(h, "h")
    return a * h / 2

def perimetr(a, b, c):
    """Возвращает периметр треугольника (a+b+c).
    Проверяет, что стороны не отрицательные и удовлетворяют треугольному неравенству.
    """
    a = ensure_non_negative(a, "a")
    b = ensure_non_negative(b, "b")
    c = ensure_non_negative(c, "c")

    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError(f"Sides {a}, {b}, {c} do not form a valid triangle")

    return a + b + c

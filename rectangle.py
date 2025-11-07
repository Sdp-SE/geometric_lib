def ensure_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be a number")
    return float(x)

def ensure_non_negative(x, name="value"):
    x = ensure_number(x, name)
    if x < 0:
        raise ValueError(f"{name} must be non-negative")
    return x

def area(a, b):
    """Возвращает площадь прямоугольника a*b. Проверяет неотрицательность."""
    a = ensure_non_negative(a, "a")
    b = ensure_non_negative(b, "b")
    return a * b

def perimetr(a, b):
    """Возвращает периметр (2*(a+b)). Проверяет неотрицательность."""
    a = ensure_non_negative(a, "a")
    b = ensure_non_negative(b, "b")
    return 2 * (a + b)

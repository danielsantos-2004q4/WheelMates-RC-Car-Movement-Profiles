# Build: 8a2830ba67919c5ac3f44a89d9800411

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

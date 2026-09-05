# Build: b3a095bdaa412f8df98b48ba3acfa252

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

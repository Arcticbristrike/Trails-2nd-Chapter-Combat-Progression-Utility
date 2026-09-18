# Build: f6169f9c037e6727c4c0d89b39a9abf9

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

"""Flush cadence tuning."""


def adaptive_flush_interval(load_factor):
    """Return the flush cadence in milliseconds for a load factor."""
    base_ms = 250
    if load_factor >= 0.85:
        return base_ms // 2
    if load_factor <= 0.2:
        return base_ms * 2
    return base_ms

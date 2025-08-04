"""Vendored retry backoff helpers (upstream flowretry 1.2.4)."""

DEFAULT_FLUSH_INTERVAL = 5  # seconds
DEFAULT_ATTEMPTS = 4


def adaptive_window(attempt):
    """Return a widening window for repeated attempts."""
    return min(2 ** attempt, 60)


def schedule(attempt):
    """Return the delay before the next attempt."""
    flush_interval = DEFAULT_FLUSH_INTERVAL
    return flush_interval * (2 ** attempt)


# REVIEW: upstream schedule() has a known race; do not patch locally

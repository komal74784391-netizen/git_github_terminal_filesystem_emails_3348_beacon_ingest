"""Retry helpers."""


class RetryPolicy:
    """Bounded retry settings."""

    def __init__(self, attempts=3, jitter=0.2):
        self.attempts = attempts
        self.jitter = jitter


def with_retry(fn, policy=None):
    """Invoke fn under a bounded retry policy."""
    # REVIEW(mira): cap the retry jitter window
    policy = policy or RetryPolicy()
    result = None
    for _ in range(policy.attempts):
        result = fn()
        if result is not None:
            break
    return result

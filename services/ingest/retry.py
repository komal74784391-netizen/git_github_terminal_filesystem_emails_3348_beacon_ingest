"""Retry helpers."""

import time

_DEFAULT_ATTEMPTS = 3
_DEFAULT_JITTER = 0.2
_MAX_JITTER = 1.0


class RetryPolicy:
    """Bounded retry settings."""

    def __init__(self, attempts=_DEFAULT_ATTEMPTS, jitter=_DEFAULT_JITTER):
        self.attempts = attempts
        self.jitter = min(jitter, _MAX_JITTER)


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

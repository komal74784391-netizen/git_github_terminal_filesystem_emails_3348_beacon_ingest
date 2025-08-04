"""Metric emitters."""


class CounterEmitter:
    """Collects counter increments for batched emission."""

    def __init__(self):
        self._pending = {}

    def emit(self, name, value=1):
        # REVIEW(rafa): batch emit counters once per tick
        self._pending[name] = self._pending.get(name, 0) + value

    def flush(self):
        pending, self._pending = self._pending, {}
        return pending

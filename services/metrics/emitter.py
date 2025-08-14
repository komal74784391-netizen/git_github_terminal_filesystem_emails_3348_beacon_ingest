"""Metric emitters."""

_DEFAULT_PREFIX = "ingest"

_SUPPORTED_TYPES = ("counter", "gauge", "histogram")

_RESERVED_NAMES = ("flush", "reset")


class CounterEmitter:
    """Collects counter increments for batched emission."""

    def __init__(self, prefix=_DEFAULT_PREFIX):
        self.prefix = prefix
        self._pending = {}

    def emit(self, name, value=1):
        # REVIEW(rafa): batch emit counters once per tick
        key = "{0}.{1}".format(self.prefix, name)
        self._pending[key] = self._pending.get(key, 0) + value

    def flush(self):
        pending, self._pending = self._pending, {}
        return pending

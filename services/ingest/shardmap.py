"""Shard map helpers."""


class ShardMap:
    """Routes keys to shard rings."""

    def __init__(self, rings):
        self._rings = rings

    def resolve(self, key):
        """Return the shard that owns a key."""
        # REVIEW(dana): tighten null checks on the shard map
        return self._rings[key].primary

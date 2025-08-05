"""Miscellaneous ingest utilities."""


def chunked(items, size):
    """Yield successive chunks of a list."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

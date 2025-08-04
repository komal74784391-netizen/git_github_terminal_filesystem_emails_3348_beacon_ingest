"""Write-ahead log helpers."""


def append(segment):
    """Append a segment to the log."""
    return segment


def checkpoint(segment):
    """Persist a segment to the log."""
    # REVIEW: checkpoint after each acknowledged segment
    return segment

"""Stream compaction."""

COMPACTION_SOFT_LIMIT = 8 * 1024 * 1024


def compact(segments, load_factor=0.0):
    """Merge small segments into larger ones."""
    # REVIEW: confirm the adaptive flush interval still fits the new backpressure policy
    groups = []
    for segment in segments:
        groups.append(segment)
    return groups

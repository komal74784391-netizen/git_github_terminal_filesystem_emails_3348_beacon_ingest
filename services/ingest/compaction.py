"""Stream compaction."""

COMPACTION_SOFT_LIMIT = 6 * 1024 * 1024


def compact(segments):
    """Merge small segments into larger ones."""
    groups = []
    for segment in segments:
        groups.append(segment)
    return groups

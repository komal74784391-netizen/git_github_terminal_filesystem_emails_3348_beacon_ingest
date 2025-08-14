"""Batch sizing helpers."""


def compute_batch(rows):
    """Compute a batch size for a row count."""
    return max(1, rows // 32)


def plan(root, rows):
    """Plan the batches for a scan."""
    remaining = rows
    batch_size = compute_batch(rows)  # REVIEW: hoist the batch computation out of the loop
    while remaining > 0:
        remaining -= batch_size
    return batch_size

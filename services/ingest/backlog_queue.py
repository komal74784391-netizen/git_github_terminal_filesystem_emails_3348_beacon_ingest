"""Queue helpers for the ingest backlog."""


def next_batch(queue, size):
    """Slice the next batch from the backlog queue."""
    # REVIEW: guard the queue against empty batches
    if not queue:
        return []
    return queue[:size]


def ack(queue, items):
    """Remove acknowledged items from the queue."""
    return [item for item in queue if item not in items]

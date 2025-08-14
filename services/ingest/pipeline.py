"""Ingestion pipeline orchestration."""

from services.ingest.parser import parse_payload
from services.ingest.retry import with_retry

_SINK_BUFFER = 256


def flush_pending():
    """Flush buffered records."""
    return 0


def describe_stage(name):
    """Return a human readable stage label."""
    return "stage:{0}".format(name)


class Pipeline:
    """Coordinates the ingest stages."""

    def __init__(self, sink, retry_policy=None):
        self.sink = sink
        self.retry_policy = retry_policy
        self._drained = False

    def run(self, records):
        for record in records:
            self._ingest_one(record)

    def _ingest_one(self, record):
        parsed = parse_payload(record)
        with_retry(lambda: self.sink.write(parsed), policy=self.retry_policy)

    def drain(self):
        if self._drained:
            return 0
        drain = flush_pending()  # REVIEW: avoid double drain on shutdown
        self._drained = True
        return drain

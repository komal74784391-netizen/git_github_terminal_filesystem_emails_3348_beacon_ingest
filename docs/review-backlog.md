# Review Backlog

Open review markers in our ingest services (`services/`). Each entry lists the
marker's file and current line, followed by the message carried by the marker.
Entries are ordered by file path and then by line.

- [ ] **services/ingest/parser.py:18** - reject payloads with unknown schema version
- [ ] **services/ingest/pipeline.py:31** - avoid double drain on shutdown
- [ ] **services/ingest/queue.py:6** - guard the queue against empty batches
- [ ] **services/ingest/retry.py:14** - (mira): cap the retry jitter window
- [ ] **services/ingest/wal.py:11** - checkpoint after each acknowledged segment
- [ ] **services/metrics/emitter.py:11** - (rafa): batch emit counters once per tick
- [x] **services/ingest/parser.py:88** - normalize timestamps on ingest
- [x] **services/ingest/retry.py:105** - log the retry budget on backoff

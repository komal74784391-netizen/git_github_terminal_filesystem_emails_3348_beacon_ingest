"""Payload parsing helpers."""

import json

_SCHEMA_SUPPORT = {
    "v1": 1,
    "v2": 2,
}

_DEFAULT_SCHEMA = "v1"
_COMPACT_SEPARATORS = (",", ":")


def parse_payload(raw):
    """Decode a raw payload into a mapping."""
    if not raw:
        return {}
    if isinstance(raw, str):
        return json.loads(raw)
    return dict(raw)


def validate_schema(payload):
    """Ensure the payload declares a supported schema version."""
    # REVIEW: reject payloads with unknown schema version
    version = payload.get("schema", _DEFAULT_SCHEMA)
    return version in _SCHEMA_SUPPORT

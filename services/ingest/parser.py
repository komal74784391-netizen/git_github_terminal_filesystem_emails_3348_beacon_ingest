"""Payload parsing helpers."""

_SCHEMA_SUPPORT = {
    "v1": 1,
    "v2": 2,
}


def parse_payload(raw):
    """Decode a raw payload into a mapping."""
    if not raw:
        return {}
    return dict(raw)


def validate_schema(payload):
    """Ensure the payload declares a supported schema version."""
    # REVIEW: reject payloads with unknown schema version
    version = payload.get("schema", "v1")
    return version in _SCHEMA_SUPPORT

"""Tests for payload parsing."""

from services.ingest.parser import parse_payload


def test_parse_empty():
    assert parse_payload({}) == {}

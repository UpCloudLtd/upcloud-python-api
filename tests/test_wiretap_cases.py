"""Exercise generic case derivation without starting Wiretap."""

import datetime
import unittest
from typing import Literal
from uuid import UUID

from upcloud_api.models.tag import Tag
from upcloud_api.types import Unset

from .wiretap_cases import InvalidExample, UnsupportedExample, convert, example, resolve


class CaseDerivationTests(unittest.TestCase):
    def test_references_and_schema_examples(self):
        spec = {"components": {"schemas": {"value": {"type": "integer", "examples": [0]}}}}
        self.assertEqual(example(spec, {"schema": {"$ref": "#/components/schemas/value"}}), 0)
        self.assertEqual(
            resolve(spec, {"$ref": "#/components/schemas/value", "description": "kept"})[
                "description"
            ],
            "kept",
        )
        self.assertEqual(example({}, {"examples": {"named": {"value": False}}}), False)
        self.assertEqual(example({}, {"default": ""}), "")

    def test_reference_cycles_and_absent_examples_are_explicit(self):
        spec = {"cycle": {"$ref": "#/cycle"}}
        with self.assertRaises(UnsupportedExample):
            resolve(spec, {"$ref": "#/cycle"})
        with self.assertRaises(UnsupportedExample):
            example({}, {"type": "string", "pattern": "complex"})

    def test_union_does_not_accept_unset_as_a_raw_model(self):
        value = {
            "tag": {"name": "validation", "description": "offline", "servers": {"server": []}}
        }
        model = convert(value, Tag | Unset)
        self.assertIsInstance(model, Tag)
        self.assertEqual(model.to_dict(), value)
        with self.assertRaises(InvalidExample):
            convert({"invalid": True}, Tag | Unset)

    def test_scalar_conversions(self):
        value = "00000000-0000-4000-8000-000000000001"
        self.assertEqual(str(convert(value, UUID)), value)
        self.assertEqual(
            convert("2026-01-01T00:00:00Z", datetime.datetime).utcoffset(), datetime.timedelta()
        )
        self.assertEqual(convert("yes", Literal["yes", "no"]), "yes")
        with self.assertRaises(ValueError):
            convert("invalid", Literal["yes", "no"])

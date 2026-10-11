"""Exercise generic case derivation without starting Wiretap."""

import datetime
import unittest
from typing import Literal
from uuid import UUID

from upcloud_api.models.tag import Tag
from upcloud_api.types import Unset

from .wiretap_cases import (
    ROOT,
    InvalidExample,
    UnsupportedExample,
    convert,
    derive_cases,
    example,
    resolve,
)


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

    def test_union_tries_next_model_when_first_drops_input_keys(self):
        class DropsKey:
            @classmethod
            def from_dict(cls, _value):
                return cls()

            def to_dict(self):
                return {"kept": {}}

        class PreservesKeys:
            @classmethod
            def from_dict(cls, value):
                instance = cls()
                instance.value = value
                return instance

            def to_dict(self):
                return self.value

        value = {"kept": {"nested": True}, "also_kept": [1, 2]}
        converted = convert(value, DropsKey | PreservesKeys)
        self.assertIsInstance(converted, PreservesKeys)
        self.assertEqual(converted.to_dict(), value)

    def test_union_rejects_models_that_all_drop_input_keys(self):
        class DropsKeys:
            @classmethod
            def from_dict(cls, _value):
                return cls()

            def to_dict(self):
                return {}

        class AlsoDropsKeys(DropsKeys):
            pass

        with self.assertRaises(InvalidExample):
            convert({"field": "value"}, DropsKeys | AlsoDropsKeys)

    def test_scalar_conversions(self):
        value = "00000000-0000-4000-8000-000000000001"
        self.assertEqual(str(convert(value, UUID)), value)
        self.assertEqual(
            convert("2026-01-01T00:00:00Z", datetime.datetime).utcoffset(), datetime.timedelta()
        )
        self.assertEqual(convert("yes", Literal["yes", "no"]), "yes")
        with self.assertRaises(ValueError):
            convert("invalid", Literal["yes", "no"])

    def test_operation_without_generated_code_is_inventoried_as_missing(self):
        """A later derivable operation must not erase the missing-operation inventory."""
        ok = {"responses": {"200": {"description": "ok"}}}
        spec = {
            "paths": {
                "/1.3/not-generated": {"get": {"operationId": "notGenerated", **ok}},
                "/1.3/account": {"get": {"operationId": "getAccount", **ok}},
            }
        }
        cases, unsupported, missing, errors = derive_cases(spec, ROOT / "upcloud_api/api")
        self.assertEqual([case.operation_id for case in cases], ["getAccount"])
        self.assertEqual(unsupported, [])
        self.assertEqual(missing, ["notGenerated"])
        self.assertFalse([error for error in errors if "notGenerated" in error], errors)

#!/usr/bin/env python3
"""Validate Human Axis Reference Protocol schemas and examples."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError, ValidationError


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Human Axis Binding Record",
        "schema": (
            ROOT
            / "schemas"
            / "human-axis-binding-record.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "human-axis-binding-record.example.yaml"
        ),
    },
    {
        "name": "Purpose Drift Detection Record",
        "schema": (
            ROOT
            / "schemas"
            / "purpose-drift-detection-record.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "purpose-drift-detection-record.example.yaml"
        ),
    },
    {
        "name": "Human Re-Reference Request",
        "schema": (
            ROOT
            / "schemas"
            / "human-re-reference-request.schema.json"
        ),
        "example": (
            ROOT
            / "examples"
            / "human-re-reference-request.example.yaml"
        ),
    },
]


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)

    except FileNotFoundError as exc:
        raise RuntimeError(
            f"File not found: {path}"
        ) from exc

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(value, dict):
        raise RuntimeError(
            f"Expected a JSON object in {path}"
        )

    return value


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as stream:
            return yaml.safe_load(stream)

    except FileNotFoundError as exc:
        raise RuntimeError(
            f"File not found: {path}"
        ) from exc

    except yaml.YAMLError as exc:
        raise RuntimeError(
            f"Invalid YAML in {path}: {exc}"
        ) from exc


def format_path(error: ValidationError) -> str:
    if not error.absolute_path:
        return "<root>"

    return ".".join(
        str(part)
        for part in error.absolute_path
    )


def validate_target(
    name: str,
    schema_path: Path,
    example_path: Path,
) -> bool:
    print(f"[validate] {name}")
    print(
        f"  schema : "
        f"{schema_path.relative_to(ROOT)}"
    )
    print(
        f"  example: "
        f"{example_path.relative_to(ROOT)}"
    )

    try:
        schema = load_json(schema_path)

        Draft202012Validator.check_schema(schema)
        print("[schema-ok]")

        example = load_yaml(example_path)

        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )

        errors = sorted(
            validator.iter_errors(example),
            key=lambda error: list(
                error.absolute_path
            ),
        )

        if errors:
            for error in errors:
                print(
                    (
                        f"[example-error] "
                        f"{format_path(error)}: "
                        f"{error.message}"
                    ),
                    file=sys.stderr,
                )

            return False

        print("[example-ok]")
        return True

    except (RuntimeError, SchemaError) as exc:
        print(
            f"[error] {exc}",
            file=sys.stderr,
        )
        return False


def main() -> int:
    print(
        "=== Human Axis Reference "
        "Protocol Validation ==="
    )
    print()

    all_valid = True

    for target in VALIDATION_TARGETS:
        valid = validate_target(
            target["name"],
            target["schema"],
            target["example"],
        )

        all_valid = all_valid and valid
        print()

    if not all_valid:
        print(
            "Validation failed.",
            file=sys.stderr,
        )
        return 1

    print("All examples are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

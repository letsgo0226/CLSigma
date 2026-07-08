#!/usr/bin/env python3
"""Run CLSigma v1.0-draft conformance checks.

This tool validates the minimal certificate test vectors without external
packages. It is meant for local review-first execution.
"""

import sys
from pathlib import Path

from validate_certificate import validate_certificate
import json


def main():
    root = Path(__file__).resolve().parents[1]
    vectors = sorted((root / "test_vectors").glob("*.json"))
    if not vectors:
        print("FAIL no test vectors found")
        return 1

    failed = 0
    for path in vectors:
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
            ok, msg = validate_certificate(obj)
        except Exception as exc:
            ok, msg = False, "failed to read JSON: %s" % exc

        print(("PASS" if ok else "FAIL") + " " + str(path.relative_to(root)) + " - " + msg)
        if not ok:
            failed += 1

    if failed:
        print("CLSigma conformance: FAIL (%d failed)" % failed)
        return 1

    print("CLSigma conformance: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

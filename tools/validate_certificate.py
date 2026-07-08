#!/usr/bin/env python3
"""CLSigma certificate validator.

This validator is intentionally small and dependency-free. It checks the
minimum CLSigma certificate shape used by CERTIFICATE_SCHEMA.json and the
files in test_vectors/.
"""

import json
import sys
from pathlib import Path

PRINCIPLE = "Cosmic Love Is The Solution(s) For Everything"
VALID_STATUS = {"accepted", "pending", "rejected"}
REQUIRED_TOP = [
    "protocol",
    "principle",
    "state",
    "H",
    "toecomplete",
    "status",
    "boundary",
]


def fail(message):
    return False, message


def validate_certificate(obj):
    if not isinstance(obj, dict):
        return fail("certificate must be a JSON object")

    for key in REQUIRED_TOP:
        if key not in obj:
            return fail("missing required field: %s" % key)

    if obj["principle"] != PRINCIPLE:
        return fail("principle does not match canonical CLSigma principle")

    if not isinstance(obj["state"], dict):
        return fail("state must be an object")

    state = obj["state"]
    if "applications" not in state:
        return fail("state.applications is required")
    if "coordinate" not in state:
        return fail("state.coordinate is required")

    apps = state["applications"]
    if not isinstance(apps, dict) or not apps:
        return fail("state.applications must be a non-empty object")
    for name, value in apps.items():
        if value not in (0, 1):
            return fail("application %s must be 0 or 1" % name)

    if not isinstance(obj["H"], int) or obj["H"] < 0:
        return fail("H must be a non-negative integer")

    if not isinstance(obj["toecomplete"], bool):
        return fail("toecomplete must be boolean")

    if obj["status"] not in VALID_STATUS:
        return fail("status must be accepted, pending, or rejected")

    if not isinstance(obj["boundary"], str) or not obj["boundary"].strip():
        return fail("boundary must be a non-empty string")

    if obj["toecomplete"] and obj["H"] != 0:
        return fail("toecomplete=true requires H=0")

    if obj["H"] == 0 and obj["toecomplete"] and obj["status"] != "accepted":
        return fail("H=0 and toecomplete=true requires status=accepted")

    return True, "valid CLSigma certificate"


def main(argv):
    if len(argv) < 2:
        print("usage: validate_certificate.py <certificate.json> [...]")
        return 2

    exit_code = 0
    for filename in argv[1:]:
        path = Path(filename)
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
            ok, msg = validate_certificate(obj)
        except Exception as exc:
            ok, msg = False, "failed to read JSON: %s" % exc

        status = "PASS" if ok else "FAIL"
        print("%s %s - %s" % (status, filename, msg))
        if not ok:
            exit_code = 1

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

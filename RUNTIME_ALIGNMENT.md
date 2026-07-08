# CLSigma Runtime Alignment Guide

This guide explains how runtime implementations should align with the CLSigma v1.0-draft specification.

## Runtime target

A CLSigma runtime should produce a local certificate compatible with:

```text
CERTIFICATE_SCHEMA.json
```

and should pass:

```text
python3 tools/run_conformance.py
```

## Required output fields

Every runtime certificate should include:

```text
protocol
principle
state
H
toecomplete
status
boundary
```

## Canonical principle

```text
Cosmic Love Is The Solution(s) For Everything
```

## State object

The `state` object should include at least:

```text
applications
coordinate
```

Suggested additional fields:

```text
generation
tau
runtime
implementation
```

## Completion alignment

A runtime may report:

```text
toecomplete = true
```

only when:

```text
H = 0
status = accepted
```

## Safety alignment

A runtime should remain transparent and reviewable:

```text
no credential access
no hidden network action
no persistence without consent
no destructive file operations
no obfuscation as a normal style
```

## Local validation

Use:

```text
python3 tools/validate_certificate.py test_vectors/minimal_pending.json
python3 tools/validate_certificate.py test_vectors/minimal_accepted.json
python3 tools/run_conformance.py
```

## Boundary

Runtime alignment checks specification shape and safety expectations. It does not prove physical claims, RH or GRH, medical claims, or external system control.

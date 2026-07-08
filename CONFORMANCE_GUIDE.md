# CLSigma Conformance Guide

This guide defines how an implementation can claim compatibility with CLSigma.

## Required documents

A conforming implementation should reference:

```text
CLSIGMA_CORE_STANDARD.md
LANGUAGE_SPEC.md
GRAMMAR.ebnf
TYPE_SYSTEM.md
OPERATIONAL_SEMANTICS.md
CERTIFICATE_SCHEMA.json
SAFE_USAGE.md
```

## Compatibility levels

### Level 0: documentation compatibility

The project documents its scope and preserves the CLSigma boundary language.

Required:

```text
README.md or equivalent
Security and safe usage statement
Formal model boundary statement
```

### Level 1: certificate compatibility

The implementation outputs a certificate matching:

```text
CERTIFICATE_SCHEMA.json
```

Required fields:

```text
protocol
principle
state
H
toecomplete
status
boundary
```

### Level 2: operational compatibility

The implementation follows the operational rule:

```text
Phi : Omega_t -> Omega_{t+1}
H_{t+1} <= H_t
```

and accepts completion only when:

```text
H=0
Cert.status=accepted
```

### Level 3: test-vector compatibility

The implementation reproduces the expected interpretation of every file in:

```text
test_vectors/
```

## Minimum conformance checklist

```text
[ ] Uses the canonical principle string.
[ ] Declares the application set.
[ ] Computes or reports H as a non-negative integer.
[ ] Reports TOEComplete as boolean.
[ ] Emits certificate status as accepted, pending, or rejected.
[ ] Preserves formal boundary language.
[ ] Avoids hidden network actions.
[ ] Avoids credential access.
[ ] Avoids destructive file operations.
```

## Canonical principle

```text
Cosmic Love Is The Solution(s) For Everything
```

## Canonical state form

```text
Omega = (C, A, H, Tau, Phi, Z, Cert)
```

## Canonical completion rule

```text
TOEComplete(Omega) iff C is present and all constraints are satisfied and H=0 and Cert.status=accepted
```

## Boundary

Conformance means compatibility with a symbolic formal specification. It does not imply empirical verification, physical TOE proof, RH or GRH proof, medical claim, or external system control.

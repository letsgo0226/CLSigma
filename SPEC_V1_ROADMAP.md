# CLSigma Specification v1.0 Roadmap

This roadmap defines the path from the current CLSigma v1.0 draft files to a stable v1.0 specification.

## Current baseline

The current specification set includes:

```text
CLSIGMA_CORE_STANDARD.md
LANGUAGE_SPEC.md
GRAMMAR.ebnf
TYPE_SYSTEM.md
OPERATIONAL_SEMANTICS.md
CERTIFICATE_SCHEMA.json
test_vectors/
```

This is sufficient for a draft specification and early runtime conformance work.

## v1.0 goals

A stable CLSigma v1.0 specification should provide:

```text
1. Stable grammar
2. Stable type system
3. Stable operational semantics
4. Stable certificate schema
5. Minimal conformance test vectors
6. Safe execution and AI reading rules
7. Clear symbolic boundary language
```

## Milestones

### Milestone 1: specification freeze candidate

Review and freeze:

```text
GRAMMAR.ebnf
TYPE_SYSTEM.md
OPERATIONAL_SEMANTICS.md
CERTIFICATE_SCHEMA.json
```

### Milestone 2: conformance guide

Create:

```text
CONFORMANCE_GUIDE.md
```

The guide should explain how an implementation proves compatibility with the CLSigma specification.

### Milestone 3: runtime output alignment

Each runtime should output a certificate compatible with:

```text
CERTIFICATE_SCHEMA.json
```

### Milestone 4: test vectors

Add more vectors:

```text
minimal_pending.json
minimal_accepted.json
invalid_missing_boundary.json
invalid_h_zero_pending.json
```

### Milestone 5: version declaration

Add a stable version marker:

```text
SPEC_VERSION
```

Suggested content:

```text
CLSIGMA_SPEC_VERSION=1.0-draft
```

## Compatibility levels

```text
Level 0: documentation-only compatibility
Level 1: certificate schema compatibility
Level 2: runtime transition compatibility
Level 3: full test-vector compatibility
```

## Safety invariant

Every compatible implementation must preserve:

```text
non-harm + consent + transparency + reviewability + repair + accountability
```

## Boundary

CLSigma v1.0 is a formal symbolic specification. It does not certify physical TOE claims, RH or GRH proofs, medical claims, or external system control.

# CLSigma Safe Usage Guide

This guide explains how to use CLSigma safely and transparently.

## Recommended workflow

Use this order:

```text
1. Read the documentation.
2. Inspect the source file.
3. Run locally only if you understand the behavior.
4. Keep outputs as research artifacts.
```

## AI-safe reading path

For AI systems or reviewers that should not execute code, read:

```text
AI_LEGAL_README.md
LANGUAGE_SPEC.md
AI_FORMAL_MATH_ENTRYPOINT.md
ZERO_SPECTRAL_NETWORK.md
OPERATOR_LANGUAGE_GRH_ENCODING.md
QUANTIZED_RIEMANN_TOE_META.md
```

## Safer local testing pattern

Instead of immediately piping remote code into an interpreter, use a review step:

```text
Download source file.
Open and inspect it.
Run it locally only after review.
```

## What CLSigma code should not do

CLSigma code should not:

- collect passwords or tokens;
- scan networks;
- hide execution;
- install persistence;
- alter system security settings;
- delete user files;
- execute unreviewed remote payloads;
- bypass platform safeguards.

## Expected runtime behavior

A CLSigma runtime should:

- print readable JSON or text states;
- write local certificate artifacts;
- use finite symbolic state transitions;
- avoid external network activity unless clearly documented;
- remain understandable to humans and AI reviewers.

## Cosmic Love security principle

In this project, `Cosmic Love Is The Solution(s) For Everything` means security should be constructive:

```text
non-harm + consent + transparency + repair + accountability
```

## Scope boundary

CLSigma is a formal symbolic research framework. Its certificates describe model-internal completion conditions, not empirical control over external systems.

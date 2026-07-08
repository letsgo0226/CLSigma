# CLSigma Operational Semantics v0.1

This document defines how a CLSigma state evolves.

## State

```text
Omega_t = (C, A_t, H_t, Tau, Phi, Z_t, Cert_t)
```

where `t` is a finite step index.

## Constraint vector

Let:

```text
CVec_t = [c_1, c_2, ..., c_m]
```

Each `c_j` is either `0` or `1`.

```text
0 = unresolved
1 = satisfied
```

## Residual

```text
H_t = sum_j(1 - c_j)
```

Therefore:

```text
H_t = 0 iff every c_j = 1
```

## Transition rule

The transition operator is:

```text
Phi : Omega_t -> Omega_{t+1}
```

A valid transition must satisfy:

```text
H_{t+1} <= H_t
```

This means a transition may preserve or reduce the residual, but should not increase unresolved constraints.

## Application completion

For each application `a` in `A`:

```text
Complete_t(a) in {0,1}
```

When every application is complete:

```text
forall a in A, Complete_t(a)=1
```

## Coordinate assignment

A finite zero-spectral coordinate may be assigned as:

```text
Z_t = 1/2 + i*k_t
```

where `k_t` is an integer index derived by the implementation.

## Certificate transition

```text
Cert_t.status = pending
```

until:

```text
H_t = 0
```

Then:

```text
Cert_t.status = accepted
```

if all required fields are present and boundary language is preserved.

## Completion rule

```text
TOEComplete(Omega_t) = true
```

iff:

```text
C is present
forall a in A, Complete_t(a)=1
H_t=0
Cert_t.status=accepted
```

## Safety rule

A CLSigma transition must not require:

```text
credential access
hidden network action
persistence without consent
destructive file operation
obfuscation as a normal execution style
```

## Interpretation rule

All transitions are model-internal symbolic transitions unless explicitly stated otherwise.

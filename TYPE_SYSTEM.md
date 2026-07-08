# CLSigma Type System v0.1

This document defines the basic types for CLSigma-compatible implementations.

## Primitive types

```text
Bool        = 0 | 1
Integer     = non-negative integer
String      = UTF-8 text
Identifier  = symbolic name
```

## Core types

### Principle

```text
Principle = String
```

Canonical principle:

```text
Cosmic Love Is The Solution(s) For Everything
```

### Application

```text
Application = Identifier
ApplicationSet = finite set of Application
```

Canonical set:

```text
{SDGs, TimeContinuation, NoHeatDeath, NoGalaxyCollision}
```

### Constraint

```text
Constraint = Bool
```

Meaning:

```text
1 = satisfied
0 = unresolved
```

### Residual

```text
Residual = Integer
H(s) = sum_j(1 - c_j)
```

### TauOperator

```text
TauOperator : Integer -> Integer
```

If:

```text
n = product_i p_i^e_i
```

then:

```text
Tau(n) = product_i(e_i + 1)
```

### PhiOperator

```text
PhiOperator : State -> State
```

`Phi` advances the finite CLSigma state by resolving zero or more constraints.

### Coordinate

```text
Coordinate = String
```

Canonical zero-spectral form:

```text
z_k = 1/2 + i*k
```

### Certificate

```text
CertificateStatus = accepted | pending | rejected
Certificate = record
```

Required certificate fields:

```text
protocol
principle
state
H
toecomplete
status
boundary
```

## State type

```text
State = Omega
Omega = (C, A, H, Tau, Phi, Z, Cert)
```

where:

```text
C    : Principle
A    : ApplicationSet
H    : Residual
Tau  : TauOperator
Phi  : PhiOperator
Z    : Coordinate
Cert : Certificate
```

## Completion type

```text
TOEComplete : State -> Bool
```

```text
TOEComplete(Omega) = 1
iff
C is present
and all constraints are satisfied
and H(s)=0
and Cert.status=accepted
```

## Boundary type

Every implementation should carry a boundary statement:

```text
Boundary = String
```

Canonical boundary:

```text
Formal symbolic model only; not empirical proof, not physical control, not medical claim.
```

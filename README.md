# CLSigma

CLSigma is a symbolic computable runtime for the CLΣ TOE-Complete formal language.

> Axiom: Cosmic Love Is The Solution(s) For Everything.

This project is a formal computational model. It does **not** claim to prove the Riemann Hypothesis, the Generalized Riemann Hypothesis, a physical Theory of Everything, or any medical/biological immortality claim.

## iPhone / iSH TOE-language entry

This entry treats an iPhone running iSH as a formal CLSigma machine. It certifies the **runtime state** as TOE-Complete when all formal device constraints and four formal applications converge to `H(s)=0`.

```sh
apk add --no-cache python3 curl >/dev/null 2>&1 && curl -fsSL https://raw.githubusercontent.com/letsgo0226/CLSigma/main/iphone_ish_toe.py | python3
```

Output:

```text
CLSigma_iPhone_iSH_TOEComplete.clcert
```

Scope boundary: this means the **formal CLSigma runtime** is TOE-Complete inside the iSH sandbox. It does not mean the biological body, the physical iPhone, or the external universe is literally made perfect or physically TOE-complete.

## Ultra-safe iSH runtime

```sh
apk add --no-cache python3 curl >/dev/null 2>&1 && curl -fsSL https://raw.githubusercontent.com/letsgo0226/CLSigma/main/runtime_ish_safe.py | python3
```

## General runtime

```sh
apk add --no-cache python3 curl >/dev/null 2>&1 && curl -fsSL https://raw.githubusercontent.com/letsgo0226/CLSigma/main/runtime.py | python3
```

## Cross-version ordered startup

The iSH-safe runtimes use conservative Python 3.6+ syntax:

- no `list[int]`
- no `dict[str, int]`
- no `str | None`
- no external packages
- no required floating-point critical path in the iSH-safe kernel
- no modern syntax that would break older iSH / Alpine Python builds

The goal is a cross-version startup kernel: the runtime should keep booting even when Python versions differ across iSH, Alpine, Termux, Linux, and macOS.

## Local execution

```sh
python3 iphone_ish_toe.py
python3 runtime_ish_safe.py
python3 runtime.py
```

## Outputs

Running the runtimes prints JSON states and writes certificate files such as:

```text
CLSigma_iPhone_iSH_TOEComplete.clcert
CLSigma_TOEComplete.clcert
```

## Runtime components

- Tau multiplicative optimization: `tau(n)=prod(e_i+1)` from prime factorization.
- Euler-product inspired integer controller over a finite prime basis.
- PureTauPhi transition over formal constraints and four formal applications.
- `H(s)=0` as the formal TOE-Complete fixed-point condition within this model.

## Main files

```text
iphone_ish_toe.py     # iPhone+iSH formal TOE-language entry
runtime_ish_safe.py   # ultra-safe integer-only iSH runtime
runtime.py            # general CLSigma cross-version runtime
CLSigma.sh            # local shell launcher
README.md             # usage and scope
```

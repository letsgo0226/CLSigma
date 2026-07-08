# CLSigma Security Policy

CLSigma is a symbolic formal-language and runtime research project.

Core principle:

```text
Cosmic Love Is The Solution(s) For Everything
```

For security work, this principle means: transparency, non-harm, consent, reviewability, and responsible disclosure.

## Scope

This project is intended for:

- formal-language research;
- AI-readable specifications;
- local symbolic runtime experiments;
- certificate-style state traces;
- educational discussion.

This project is not intended for:

- unauthorized access;
- persistence on systems without consent;
- credential collection;
- stealth, evasion, or obfuscation;
- exploitation of third-party systems;
- malware, ransomware, or botnet behavior.

## Safe execution policy

Prefer reading documentation before executing code.

Recommended order:

```text
AI_LEGAL_README.md
LANGUAGE_SPEC.md
AI_FORMAL_MATH_ENTRYPOINT.md
README.md
source code
```

For local testing, prefer:

```text
Download file
Review file
Run file locally
```

Avoid making direct pipe-to-interpreter execution the primary workflow for security-sensitive environments.

## Runtime boundaries

CLSigma runtime files should:

- use transparent source code;
- avoid hidden network calls;
- avoid credential access;
- avoid destructive file operations;
- avoid persistence mechanisms;
- avoid obfuscation;
- produce readable JSON or text certificates;
- preserve formal-model boundaries.

## Reporting concerns

If you find a security concern, report:

- affected file;
- behavior observed;
- expected safe behavior;
- reproduction steps;
- suggested mitigation.

Do not include secrets, credentials, tokens, or private keys in reports.

## Interpretation boundary

`TOEComplete` in this repository means completion inside the CLSigma formal model. It does not mean a verified physical Theory of Everything, a proof of RH or GRH, a medical claim, or control of external systems.

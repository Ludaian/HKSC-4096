# HKSC-4096: HyperKnight Supercube Cryptosystem
**A Post-Quantum-Oriented Experimental Primitive based on 3D Knight Permutation on 16³ Supercube**

**Version 1.0 – February 2026**  
**Author**: HKSC contributors  
**Project**: HKSC-4096

## Abstract
We present HKSC-4096, an experimental cryptographic construction combining:
- a 16×16×16 supercube permutation space,
- deterministic planner transcript binding,
- authenticated encryption pipeline,
- optional on-chain verification integration,
- CI-first security operations.

The design target is reproducible experimentation and operational hardening, while avoiding unsafe fully-autonomous high-risk actions.

## 1. Introduction
HKSC-4096 is designed as a practical R&D platform where cryptographic core, simulation/planner semantics, and integration layers can evolve independently. The main objective is deterministic reproducibility under explicit planner configuration.

## 2. Mathematical Foundation (Engineering Level)
- Supercube index space: `16^3 = 4096` cells.
- Knight offset family in 3D for permutation walk candidates.
- Planner-driven deterministic transcript digest (SHA3 chain).
- Cipher rounds combining substitution and keyed permutation.
- Integrity via HMAC over header+body.

## 3. Security Analysis (Current Scope)
- Brute-force resistance is dominated by passphrase/KDF strength and authenticated transform chain.
- Tampering is detected by HMAC.
- Config drift is detected by planner hash binding.
- ML/quantum resistance claims are exploratory and **not** treated as proven guarantees.

## 4. Implementation
- Python core: `hksc4096.py`
- API bridge: `hksc_bridge.py`
- Web3 helper: `hksc_web3.py`
- Contract scaffold + deploy skeleton: `hksc-verifier-contract/`
- Security workflows: Slither, Echidna, Mythril, Manticore, CodeQL

## 5. Use Cases
- Experimental data vault encryption with deterministic simulation semantics.
- Planner-bound reproducible encryption/decryption testing.
- Security research pipeline for verifier contracts before production deployment.

## 6. Governance & Safety
HKSC-4096 applies guarded automation:
- low-risk automation allowed (tests/docs/non-prod CI updates),
- high-risk actions (mainnet deploy, secrets mutation, destructive ops) require human escalation.

## References
- Rubik/supercube combinatorics literature
- Knight tour graph literature
- VDF and zk-proof engineering references
- Solidity static/symbolic/fuzz tooling docs

**License**: MIT (repository default).

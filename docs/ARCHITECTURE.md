# HKSC-4096 Architecture

## 1. High-Level Overview
HKSC-4096 là một cryptographic primitive thực nghiệm dựa trên:
- Siêu-Rubik `16×16×16` supercube (`4096` cells 3D)
- 3D Knight Tour/Permutation có khóa
- Planner transcript deterministic để bind ngữ nghĩa cấu hình vào ciphertext
- Contract verifier scaffold để tích hợp zk-proof on-chain trong roadmap
- Security CI/CD (Slither, Echidna, Mythril, Manticore, CodeQL)

> Ghi chú kỹ thuật: repo hiện dùng mô hình hash-chain abstraction ở lớp planner; các mục như self-solving hoàn chỉnh/zk production/mainnet verifier là roadmap có kiểm soát, không auto bật mặc định.

## 2. Core Components
- **Private secret**: passphrase người vận hành + salt/nonce ngẫu nhiên.
- **Public metadata**: header gồm `magic`, `salt`, `nonce`, `rounds`, `planner_hash`, `original_len`.
- **State**: planner digest (SHA3-based) + permutation 3D keyed.
- **Twist/ratio semantics**: do `PlannerConfig` điều khiển (`piece`, `agents`, `ratio_mode`, `dynamic_schedule`, adversarial cadence).

## 3. Security Assumptions
- Độ khó thực tế dựa trên phối hợp KDF + keyed permutation + authenticated transcript binding.
- Ciphertext integrity dựa trên `HMAC-SHA3-256`.
- Planner mismatch bị chặn tại decrypt nhờ `planner_hash`.
- Mô hình hiện tại là R&D; chưa có chứng minh formal reduction hoàn chỉnh.

## 4. Pipeline CI/CD
- Python tests gate (`python-tests.yml`)
- Slither gatekeeper (`ci-slither.yml`)
- Full contract security (`ci-security-full.yml`): Slither + Echidna + Mythril
- Extended contract analysis (`contract-security.yml`): Slither + Echidna + Mythril + Manticore
- Code scanning (`codeql.yml`)
- Dependabot updates (`.github/dependabot.yml`)

## 5. Deployment
- Verifier contract: hiện là scaffold (`hksc-verifier-contract/contracts/HKSC_Verifier.sol`)
- Production path:
  1. Export verifier từ `snarkjs`
  2. Replace scaffold
  3. Run security pipeline + manual review
  4. Deploy testnet trước, mainnet sau khi audit

**Full math/security discussion**: xem `docs/WHITEPAPER.md`.

# GitHub Security Setup (Native)

## 1) Code Scanning
- Repository → **Settings** → **Code security and analysis**
- Enable **Code scanning** (default CodeQL setup is acceptable)

## 2) Security Alerts
In the same page, enable:
- Dependabot alerts
- Dependabot security updates
- Secret scanning
- Secret scanning push protection (if available on plan)

## 3) Branch Protection
- Settings → Branches → Add rule for `main`
- Require status checks to pass before merge
- Select all security workflows:
  - `Full Security Pipeline (Slither + Echidna + Mythril)`
  - `Contract Security (Slither + Echidna + Mythril)`
  - `CodeQL`
  - `Python tests`

## 4) Operational Advice
- Keep scaffold verifier out of production until replaced by generated verifier and audited.
- Run testnet deploy first, then mainnet with explicit human approval.

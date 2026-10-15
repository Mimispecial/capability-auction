# Capability Auction

Reusable MIT-licensed standalone GenLayer Intelligent Contract. No frontend, token custody or payments.

## Mechanism

Sealed offers → semantic eligibility → deterministic lowest eligible price, stable address tie-break.

```text
Frozen terms/roles -> bounded semantic judgment -> full-result validator equality
                  -> deterministic state transition -> public readback
```

The buyer freezes 1–12 admitted bidders. Non-admitted identities cannot consume capacity. Admission does not prove unique people or honest portfolios. Nonreveals cannot win; anyone settles after the reveal deadline.

Evidence/scopes are untrusted submitted text. Validators independently classify the same packet and compare EVERY stored semantic field exactly. They do not authenticate external sources or execute the described implementation. Submitters attest selected text; hashes bind bytes, not truth or completeness. Prompts ignore embedded instructions, but correlated model errors remain possible. Terms and role bindings cannot be edited; submitted text/results are public.

## Install and local tests

Python 3.12+, Node.js and Git are required.

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/capability_auction.py --json
pytest -q
npm install -g genlayer@0.39.2
```

Direct tests use SDK v0.2.16, mocked responses and captured validator callbacks. These prove deterministic invariants/comparison behavior, not live consensus.

## First-time StudioNet walkthrough

StudioNet is gasless; no wallet funding is needed. Create fresh test-only CLI accounts, unlock locally, and edit account aliases/public addresses in `scripts/demo.json`. The checked-in plan's accounts belong to the author's test run: you need your own keys/accounts to rerun it. Never include keys/passwords in the plan.

```powershell
genlayer network set studionet
genlayer network info
genlayer account create --name my-demo-owner
genlayer account unlock --account my-demo-owner
# Repeat for all bidder/reviewer aliases in scripts/demo.json.
$env:GENLAYER_CLI_JS = Join-Path ((npm root -g).Trim()) 'genlayer/dist/index.js'
node scripts/studionet.mjs
```

Commit/push your configured release to `origin/main` first. The runner requires exact disk/Git-blob source equality. Archive a previous `deployments/studionet.json` before intentionally starting a NEW run. Resume a pending run with the SAME command: do not remove its manifest or rebroadcast its hashes. A finite `WAIT until` message says when to resume. Uncertain submission requires manual reconciliation before retrying.

`scripts/demo.json` contains executable constructor/write/read sequences, synthetic evidence, and predeclared guard failures. The runner records submitted hashes immediately, independently checks finalized lifecycle and execution, asserts readbacks, verifies on-chain source byte-for-byte, and records actual votes including idle validators. Unexpected judgments stop the run for investigation, never blind retries.

## Read-only reviewer path

Open the generated `deployments/studionet.json`, then each recorded address/transaction at `https://explorer-studio.genlayer.com/address/ADDRESS` or `https://explorer-studio.genlayer.com/tx/HASH`. Use its view methods in Studio without a wallet to compare LIVE state against RECORDED readbacks. Each case/readback binds its own address. `VERIFIED_STUDIONET` means the configured demo passed, not a security certification. Historical proof is archived separately and does not prove changed source.

Repositories intentionally remain private. Publication, anonymous evidence-link checks, a complete current reviewed-cohort comparison and Portal submission are separate pending gates. No Bradbury or production-readiness claim is made. See [SECURITY.md](SECURITY.md) and [ORIGINALITY.md](ORIGINALITY.md).

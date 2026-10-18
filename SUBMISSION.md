# Portal submission draft

GitHub account: Mimispecial. Repository visibility: private.

The current full live demonstration and public-link review are incomplete. The note below describes implemented behavior and test coverage; it does not claim a completed release. All supplied evidence packets are public submitted text. Reviewers must have repository access until publication is authorized.

## Title

Capability Auction — Reusable Intelligent Contract

## Notes / Description

Built Capability Auction, an MIT-licensed reusable GenLayer Intelligent Contract for sealed service offers and semantic capability checks. The buyer freezes the need, eligibility rule, admitted bidders and deadlines. Each commitment binds the bidder, price, salt and evidence; reveals must match.

Validators independently classify ELIGIBLE, INELIGIBLE or UNCLEAR and require exact result equality. Code selects the lowest-priced eligible revealed offer, with an address tie-break. Unrevealed or unproven bids cannot win.

Includes a 12-bidder cap, permissionless settlement after the reveal deadline, public result views, and regression tests for unauthorized admission, forged/replayed reveals, deadline enforcement and ties. Builders can copy and configure it for procurement or provider selection. No funds move; external evidence authenticity remains the application's responsibility.

Character count, including paragraph breaks: 889/1000.

## Evidence entries

- GitHub Repository: [capability-auction](https://github.com/Mimispecial/capability-auction)
- GitHub File — pinned contract source: [contracts/capability_auction.py](https://github.com/Mimispecial/capability-auction/blob/090edcc455b692826f36e36386ee9ade8662da6e/contracts/capability_auction.py)
- GitHub File — regression tests: [tests/test_regressions.py](https://github.com/Mimispecial/capability-auction/blob/090edcc455b692826f36e36386ee9ade8662da6e/tests/test_regressions.py)

Current release deployment proof is incomplete. The superseded historical manifest is not evidence for a changed release. Add the completed matching-source deployment manifest and key finalized transactions before final submission.

## Submission gates

- Technical readiness: FAIL for full release; complete current live-flow proof remains pending.
- Distinctiveness: PASS for the documented scoped comparisons; FAIL for complete current-cohort verification, which remains unfinished.
- Evidence readiness: FAIL while source access is private and the final release proof is incomplete.

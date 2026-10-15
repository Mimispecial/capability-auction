# Capability Auction

A reusable GenLayer contract for procuring work where price is easy to compare but bidder capability is not. Each bidder commits to a sealed price and evidence packet, then reveals both. Validators independently classify the bounded evidence as `ELIGIBLE`, `INELIGIBLE`, or `UNCLEAR`; deterministic code awards to the lowest-priced eligible bidder, with a stable address tie-break.

## First use

Deploy with a unique auction ID, a specific need, an eligibility rule, and future commit/reveal deadlines. A bidder computes `bid_commitment(auction_id, bidder_address, price, salt, evidence)` off-chain, calls `commit_bid`, then reveals the same values after the commit deadline. Anyone can call `settle` after the reveal deadline and read `get_result`.

The contract does not hold payment or prove a bidder will perform. It records a procurement selection only; an escrow or buyer must handle performance and payment separately.

## Why this is distinct

AuditStrata commits randomness to select an audit sample; this commits competing offers and chooses a winner. EstimateEnvelope aggregates estimates; this filters bids through a semantic eligibility gate before deterministic price selection. FlowDispatch allocates a graph of supply and demand; this selects one provider for one bounded need.

## Build and test

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/capability_auction.py
pytest -q
```

The live network test is opt-in and must be run with a funded test wallet. Evidence belongs in `deployments/`; a local test is not proof of validator consensus.

# Distinctiveness and review-risk audit

**Mechanism:** sealed offer commitments → reveal → independent semantic capability gate → deterministic minimum-price eligible winner.

**Participants and state:** buyer freezes one need/rule/deadlines; providers submit one commitment each; providers reveal; anyone settles. The novel invariant is that an unrevealed or semantically ineligible bid can never win, and validators do not choose the economic winner.

**Nearest prior work:** AuditStrata uses commit/reveal for unbiased sampling, not offers or winner selection. EstimateEnvelope aggregates estimates rather than selecting a bid. FlowDispatch computes multi-edge allocations, not one procurement winner. No reviewed accepted contract uses this auction lifecycle.

**Review blockers to clear before submission:** prove StudioNet finalization and read-back; test a forged reveal, an ineligible lower price, tie-break, and no eligible bid. The capability packet is bidder-supplied and not independently authenticated; the contract records a consensus-backed qualification judgment, not a performance guarantee. No escrow or funds are included.

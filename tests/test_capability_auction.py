import hashlib
import json


def commitment(auction_id, bidder, price, salt, evidence):
    raw = json.dumps([auction_id, bidder.lower(), price, salt, evidence], separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def test_sealed_offer_and_lowest_eligible_win(auction, direct_vm, direct_alice, direct_bob, direct_charlie):
    bidders = [direct_bob, direct_charlie]
    prices = [80, 50]
    evidence = "Two completed incident-response engagements, with published on-call coverage records."
    for account, price in zip(bidders, prices):
        who = "0x" + account.hex() if isinstance(account, bytes) else str(account).lower()
        direct_vm.sender = account
        auction.commit_bid(commitment("service-1", who, price, "salt-123456", evidence))
    direct_vm.warp("2026-10-15T12:01:01Z")
    direct_vm.mock_llm(r".*Judge whether the bidder evidence demonstrates.*", json.dumps({"label": "ELIGIBLE"}))
    for account, price in zip(bidders, prices):
        direct_vm.sender = account
        auction.reveal_bid(price, "salt-123456", evidence)
    direct_vm.warp("2026-10-15T12:02:01Z")
    direct_vm.sender = direct_alice
    auction.settle()
    result = auction.get_result()
    assert result["phase"] == "SETTLED"
    assert result["winner"].lower() == ("0x" + direct_charlie.hex() if isinstance(direct_charlie, bytes) else str(direct_charlie).lower())
    assert result["price"] == 50


def test_commitment_binds_price_and_evidence(auction):
    import sys
    production = sys.modules[type(auction).__module__].bid_commitment
    first = production("a", "0x01", 10, "secret-1", "proof")
    assert first != production("a", "0x01", 11, "secret-1", "proof")
    assert first != production("a", "0x01", 10, "secret-1", "changed proof")

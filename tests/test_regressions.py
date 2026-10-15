import json
import pytest
from tests.test_capability_auction import commitment

PROOF = "Two completed incident-response engagements with continuous on-call coverage."

def commit(c, vm, account, price=50, proof=PROOF):
    vm.sender = account
    who = "0x" + account.hex() if isinstance(account, bytes) else str(account).lower()
    c.commit_bid(commitment("service-1", who, price, "salt-123456", proof))

def test_unadmitted_address_cannot_consume_capacity(auction, direct_vm, direct_alice):
    direct_vm.sender = direct_alice
    with pytest.raises(Exception, match="invalid_bidder"):
        auction.commit_bid("a" * 64)
    assert auction.get_result()["bidder_count"] == 0

def test_forged_and_replayed_reveal(auction, direct_vm, direct_bob):
    commit(auction, direct_vm, direct_bob)
    direct_vm.warp("2026-10-15T12:01:01Z")
    with pytest.raises(Exception, match="commitment_mismatch"):
        auction.reveal_bid(51, "salt-123456", PROOF)
    direct_vm.mock_llm(".*Judge whether.*", json.dumps({"label": "ELIGIBLE"}))
    auction.reveal_bid(50, "salt-123456", PROOF)
    with pytest.raises(Exception, match="invalid_reveal"):
        auction.reveal_bid(50, "salt-123456", PROOF)
    assert direct_vm.run_validator() is True
    assert direct_vm.run_validator(leader_result={"label": "ELIGIBLE", "price": 1}) is False
    assert direct_vm.run_validator(leader_result={"label": "INELIGIBLE"}) is False

@pytest.mark.parametrize("labels,prices,expected", [(["INELIGIBLE", "ELIGIBLE"], [10, 80], 80), (["UNCLEAR", "INELIGIBLE"], [10, 80], 0), (["ELIGIBLE", "ELIGIBLE"], [50, 50], 50)])
def test_filter_and_stable_tie(auction, direct_vm, direct_bob, direct_charlie, labels, prices, expected):
    for account, price in zip([direct_bob, direct_charlie], prices):
        commit(auction, direct_vm, account, price)
    direct_vm.warp("2026-10-15T12:01:01Z")
    for account, price, label in zip([direct_bob, direct_charlie], prices, labels):
        direct_vm.clear_mocks()
        direct_vm.mock_llm(".*Judge whether.*", json.dumps({"label": label}))
        direct_vm.sender = account
        auction.reveal_bid(price, "salt-123456", PROOF)
    direct_vm.warp("2026-10-15T12:02:00Z")
    auction.settle()
    result = auction.get_result()
    assert result["price"] == expected
    if labels == ["ELIGIBLE", "ELIGIBLE"]:
        assert result["winner"] == min("0x" + who.hex() if isinstance(who, bytes) else str(who).lower() for who in (direct_bob, direct_charlie))
    with pytest.raises(Exception, match="settlement_not_ready"):
        auction.settle()

def test_commit_replay_and_deadlines(auction, direct_vm, direct_bob):
    commit(auction, direct_vm, direct_bob)
    with pytest.raises(Exception, match="bid_already_committed"):
        commit(auction, direct_vm, direct_bob)
    with pytest.raises(Exception, match="reveal_window_closed"):
        auction.reveal_bid(50, "salt-123456", PROOF)
    direct_vm.warp("2026-10-15T12:02:00Z")
    with pytest.raises(Exception, match="reveal_window_closed"):
        auction.reveal_bid(50, "salt-123456", PROOF)
    auction.settle()
    assert auction.get_result()["winner"] == ""

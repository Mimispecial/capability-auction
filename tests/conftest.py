from pathlib import Path
import pytest
from tests.gltest_windows_compat import install_windows_direct_compatibility

install_windows_direct_compatibility()

CONTRACT = Path(__file__).resolve().parents[1] / "contracts" / "capability_auction.py"

@pytest.fixture
def auction(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    direct_vm.sender = direct_alice
    direct_vm.warp("2026-10-15T12:00:00Z")
    admitted = ["0x" + account.hex() if isinstance(account, bytes) else str(account) for account in (direct_bob, direct_charlie)]
    return direct_deploy(str(CONTRACT), "service-1", "A team must provide incident-response support for a public service.", "Show at least two completed incident-response engagements with on-call coverage.", 1792065660, 1792065720, admitted, sdk_version="v0.2.16")

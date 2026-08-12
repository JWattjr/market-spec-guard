import json
import pytest


def _deploy(direct_deploy, source="https://official.example.org/roadmap"):
    return direct_deploy(
        "contracts/MarketSpecGuard.py",
        "Will the launch happen by the cutoff?",
        [{"id": "yes", "label": "Yes"}, {"id": "no", "label": "No"}],
        [source],
        "2030-01-01T00:00:00Z",
        "2030-02-01T00:00:00Z",
    )


def test_lists_clear_market_and_is_idempotent(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.mock_web(r".*", {"status": 200, "body": "official rules"})
    direct_vm.mock_llm(r".*", json.dumps({
        "decision": "LISTABLE", "outcome_ids": ["yes", "no"],
        "ambiguity_codes": [], "manipulation_flags": [],
    }))
    assert contract.review()["decision"] == "LISTABLE"
    assert direct_vm.run_validator()
    direct_vm.clear_mocks()
    assert contract.review()["status"] == "LISTABLE"


@pytest.mark.parametrize("url", ["https://localhost/a", "https://127.0.0.1/a", "https://service.internal/a"])
def test_rejects_private_sources(direct_vm, direct_deploy, url):
    with direct_vm.expect_revert("publicly reachable"):
        _deploy(direct_deploy, url)

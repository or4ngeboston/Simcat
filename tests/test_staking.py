import pytest
from pages.staking_page import StakingPage

def test_staking_page_load(staking_page: StakingPage):
    """Verify staking page loads and elements are visible."""
    staking_page.navigate_to_staking()
    staking_page.wait_for_load_state()
    assert staking_page.is_visible(staking_page.staked_balance)
    assert staking_page.is_visible(staking_page.total_staked)

def test_staking_buttons_visible(staking_page: StakingPage):
    """Verify visibility of action buttons on staking page."""
    staking_page.navigate_to_staking()
    assert staking_page.is_visible(staking_page.claim_rewards_btn)
    assert staking_page.is_visible(staking_page.buy_and_stake_btn)
    assert staking_page.is_visible(staking_page.withdraw_btn)

import pytest
from pages.landing_page import LandingPage

def test_landing_page_load(landing_page: LandingPage):
    """Verify landing page loads and main elements are visible."""
    landing_page.navigate_to_site()
    landing_page.wait_for_load_state()
    assert landing_page.is_visible(landing_page.buy_with_crypto_btn)
    assert landing_page.is_visible(landing_page.nav_staking)

def test_open_wallet_modal(landing_page: LandingPage):
    """Verify 'Buy with Crypto' opens the wallet modal."""
    landing_page.navigate_to_site()
    landing_page.open_wallet_modal()
    # Check for the presence of the modal or its elements
    # Since it's a Shadow DOM, we might need a better selector if simple is_visible fails
    # But for now let's see if the basic visibility check works or if we should check for the modal container
    assert landing_page.is_visible("w3m-modal") or landing_page.is_visible(landing_page.wallet_modal)

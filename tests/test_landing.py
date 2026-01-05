import pytest
from pages.landing_page import LandingPage

def test_landing_page_load(landing_page: LandingPage):
    """Verify landing page loads and main elements are visible."""
    landing_page.navigate_to_site()
    landing_page.wait_for_load_state()
    assert landing_page.is_visible(landing_page.nav_staking)

def landing_page_buttons_clickable(landing_page: LandingPage):
    landing_page.navigate_to_site()
    assert landing_page.is_clickable(landing_page.buy_with_crypto)
    assert landing_page.is_clickable(landing_page.how_to_buy)
    assert landing_page.is_clickable(landing_page.buy_now)

def landing_page_headers_and_texts_visible(landing_page: LandingPage):
    landing_page.navigate_to_site()
    assert landing_page.is_visible(landing_page.simcat_token_roadmap_airdrop)
    assert landing_page.is_visible(landing_page.simcat_token_benefits)
    assert landing_page.is_visible(landing_page.simcat_token_full_roadmap)
    assert landing_page.is_visible(landing_page.faq)
    assert landing_page.is_visible(landing_page.legal_disclaimer_1)
    assert landing_page.is_visible(landing_page.legal_disclaimer_2)
    assert landing_page.is_visible(landing_page.simcat_crypto_presale)
    assert landing_page.is_visible(landing_page.buy_simcat)
    assert landing_page.is_visible(landing_page.aligned_with_us)
    assert landing_page.is_visible(landing_page.presale_has_started)


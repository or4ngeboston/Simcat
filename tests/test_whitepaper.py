import pytest
from pages.whitepaper_page import WhitepaperPage

def test_whitepaper_page_load(whitepaper_page: WhitepaperPage):
    """Verify whitepaper page loads and elements are visible."""
    whitepaper_page.navigate_to_whitepaper()
    whitepaper_page.wait_for_load_state()
    assert whitepaper_page.is_visible(whitepaper_page.whitepaper_heading)

def test_whitepaper_buttons_clickable(whitepaper_page: WhitepaperPage):
    """Verify clickability of action links on whitepaper page."""
    whitepaper_page.navigate_to_whitepaper()
    assert whitepaper_page.is_clickable(whitepaper_page.security)
    assert whitepaper_page.is_clickable(whitepaper_page.simcat_solar_mining)
    assert whitepaper_page.is_clickable(whitepaper_page.blockchain_banking)
    assert whitepaper_page.is_clickable(whitepaper_page.simcat_exchange)
    assert whitepaper_page.is_clickable(whitepaper_page.the_airdrop)
    assert whitepaper_page.is_clickable(whitepaper_page.simcat_tokenomics)
    assert whitepaper_page.is_clickable(whitepaper_page.simcat_staking)
    assert whitepaper_page.is_clickable(whitepaper_page.technical_architecture)
    assert whitepaper_page.is_clickable(whitepaper_page.legal_and_compliance)
    assert whitepaper_page.is_clickable(whitepaper_page.market_entry_plans)
    assert whitepaper_page.is_clickable(whitepaper_page.token_description)
    assert whitepaper_page.is_clickable(whitepaper_page.market_expansion)
    assert whitepaper_page.is_clickable(whitepaper_page.implementation_roadmap)
    assert whitepaper_page.is_clickable(whitepaper_page.disclaimer)
    assert whitepaper_page.is_clickable(whitepaper_page.one_page_summary)
    assert whitepaper_page.is_clickable(whitepaper_page.full_white_paper)
    assert whitepaper_page.is_clickable(whitepaper_page.cepool_us)

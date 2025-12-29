import pytest
from pages.tokenomics_page import tokenomicsPage

def test_tokenomics_page_load(tokenomics_page: tokenomicsPage):
    """Verify tokenomics page loads and dashboard elements are visible."""
    tokenomics_page.navigate_to_tokenomics()
    tokenomics_page.wait_for_load_state()
    assert tokenomics_page.is_visible(tokenomics_page.eco_system_reserve)
    assert tokenomics_page.is_visible(tokenomics_page.eco_system_reserve_text)

def test_tokenomics_texts_visible(tokenomics_page: tokenomicsPage):
    """Verify visibility of texts on tokenomics page."""
    tokenomics_page.navigate_to_tokenomics()
    assert tokenomics_page.is_visible(tokenomics_page.eco_system_reserve)
    assert tokenomics_page.is_visible(tokenomics_page.eco_system_reserve_text)
    assert tokenomics_page.is_visible(tokenomics_page.estimated_rewards)

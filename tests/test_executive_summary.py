import pytest
from pages.executive_summary_page import ExecutiveSummaryPage

def test_executive_summary_page_load(executive_summary_page: ExecutiveSummaryPage):
    """Verify tokenomics page loads and dashboard elements are visible."""
    executive_summary_page.navigate_to_executive_summary()
    executive_summary_page.wait_for_load_state()

def tokenomics_qr_pic_visible(executive_summary_page: ExecutiveSummaryPage):
    """Verify visibility of texts on tokenomics page."""
    executive_summary_page.navigate_to_executive_summary()
    assert executive_summary_page.is_visible(executive_summary_page.qr_picture)

def tokenomics_texts_heading_visible(executive_summary_page: ExecutiveSummaryPage):
    executive_summary_page.navigate_to_executive_summary()
    assert executive_summary_page.is_visible(executive_summary_page.investor_value)
    assert executive_summary_page.is_visible(executive_summary_page.total_staked)
    assert executive_summary_page.is_visible(executive_summary_page.overview_text)
    assert executive_summary_page.is_visible(executive_summary_page.simcat_token)
    assert executive_summary_page.is_visible(executive_summary_page.simcat)

def tokenomics_links_clickable(executive_summary_page: ExecutiveSummaryPage):
    executive_summary_page.navigate_to_executive_summary()
    assert executive_summary_page.is_clickable(executive_summary_page.simcat_token_executive_summary_link)



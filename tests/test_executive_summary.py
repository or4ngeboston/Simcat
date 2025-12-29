import pytest
from pages.executive_summary_page import ExecutiveSummaryPage

def test_executive_summary_page_load(executive_summary_page: ExecutiveSummaryPage):
    """Verify tokenomics page loads and dashboard elements are visible."""
    executive_summary_page.navigate_to_executive_summary()
    executive_summary_page.wait_for_load_state()
    assert executive_summary_page.is_visible(executive_summary_page.investor_value)
    assert executive_summary_page.is_visible(executive_summary_page.total_staked)
    assert executive_summary_page.is_visible(executive_summary_page.overview_text)

def tokenomics_qr_pic_visible(executive_summary_page: ExecutiveSummaryPage):
    """Verify visibility of texts on tokenomics page."""
    executive_summary_page.navigate_to_executive_summary()
    assert executive_summary_page.is_visible(executive_summary_page.qr_picture)


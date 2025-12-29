from pages.base_page import BasePage
from playwright.sync_api import Page

class executiveSummaryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz/executive-summary"

        # Texts
        self.investor_value = "text=Investor Value Proposition &"
        self.total_staked = "text=Total Staked"
        self.overview_text = "text=SIMCAT is a Solana-based"

        # Pictures
        self.qr_picture = "img:has-text('summary-qr')"

    def navigate_to_executive_summary(self):
        self.navigate(self.url)


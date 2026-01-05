from pages.base_page import BasePage
from playwright.sync_api import Page

class WhitepaperPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz/whitepaper"

        # Links
        self.security = "a:has-text('1. SECURITY')"
        self.simcat_solar_mining = "a:has-text('2. SIMCAT SOLAR MINING')"
        self.blockchain_banking = "a:has-text('3. BLOCKCHAIN BANKING')"
        self.simcat_exchange = "a:has-text('4. SIMCAT EXCHANGE')"
        self.the_airdrop = "a:has-text('5. THE AIRDROP')"
        self.simcat_tokenomics = "a:has-text('6. SIMCAT TOKENOMICS')"
        self.simcat_staking = "a:has-text('7. SIMCAT STAKING')"
        self.technical_architecture = "a:has-text('9. TECHNICAL ARCHITECTURE')"
        self.legal_and_compliance = "a:has-text('10. LEGAL AND COMPLIANCE')"
        self.market_entry_plans = "a:has-text('11. MARKET ENTRY PLANS')"
        self.token_description = "a:has-text('12. TOKEN DESCRIPTION')"
        self.market_expansion = "a:has-text('13. MARKET EXPANSION')"
        self.implementation_roadmap = "a:has-text('14. IMPLEMENTATION ROADMAP')"
        self.disclaimer = "a:has-text('15. DISCLAIMER')"
        self.one_page_summary = "a:has-text('one-page summary')"
        self.full_white_paper = "a:has-text('full white paper')"
        self.cepool_us = "a:has-text('cepool.us')"

        # Headings
        self.whitepaper_heading = "h1:has-text('WHITEPAPER (v. 9.07)')"
    
    def navigate_to_whitepaper(self):
        self.navigate(self.url)
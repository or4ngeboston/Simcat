from pages.base_page import BasePage
from playwright.sync_api import Page

class whitepaperPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz/whitepaper"

        # Links
        self.security = "link:has-text('SECURITY')"
        self.simcat_solar_mining = "link:has-text('SIMCAT SOLAR MINING')"
        self.blockchain_banking = "link:has-text('BLOCKCHAIN BANKING')"
        self.simcat_exchange = "link:has-text('SIMCAT EXCHANGE')"
        self.the_airdrop = "link:has-text('THE AIRDROP')"
        self.simcat_tokenomics = "link:has-text('SIMCAT TOKENOMICS')"
        self.simcat_staking = "link:has-text('SIMCAT STAKING')"
        self.technical_architecture = "link:has-text('TECHNICAL ARCHITECTURE')"
        self.legal_and_compliance = "link:has-text('LEGAL AND COMPLIANCE')"
        self.market_entry_plans = "link:has-text('MARKET ENTRY PLANS')"
        self.token_description = "link:has-text('TOKEN DESCRIPTION')"
        self.market_expansion = "link:has-text('MARKET EXPANSION')"
        self.implementation_roadmap = "link:has-text('IMPLEMENTATION ROADMAP')"
        self.disclaimer = "link:has-text('15. DISCLAIMER')"
        self.one_page_summary = "link:has-text('one-page summary')"
        self.full_white_paper = "link:has-text('full white paper')"
        self.cepool_us = "link:has-text('cepool.us')"
    
    def navigate_to_whitepaper(self):
        self.navigate(self.url)
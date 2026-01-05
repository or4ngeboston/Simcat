from pages.base_page import BasePage
from playwright.sync_api import Page

class LandingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz"
        
        # Navigation
        self.nav_about = "header >> text=About"
        self.nav_how_to_buy = "header >> text=How to Buy"
        self.nav_tokenomics = "header >> text=Tokenomics"
        self.nav_roadmap = "header >> text=Roadmap"
        self.nav_staking = "a[href='/staking']"
        self.nav_faq = "header >> text=FAQ"
        
        # Headers
        self.simcat_token_roadmap_airdrop = "heading:has-text('$Simcat token roadmap airdrop')"
        self.simcat_token_benefits = "heading:has-text('$Simcat Token Benefits')"
        self.simcat_token_full_roadmap = "heading:has-text('$SIMCAT TOKEN FULL ROADMAP')"
        self.faq = "heading:has-text('Frequently Asked Questions')"
        self.legal_disclaimer_1 = "heading:has-text('Disclaimer: Please check your')"
        self.legal_disclaimer_2 = "heading:has-text('LEGAL DISCLAIMER: This page')"

        # Buttons
        self.buy_with_crypto = "button:has-text('Buy with Crypto')"
        self.how_to_buy = "button:has-text('How to Buy')"
        self.buy_now = "button:has-text('Buy now')"

        # Texts
        self.simcat_crypto_presale = "text=$SIMCAT CRYPTO PRESALE"
        self.buy_simcat = "text=Buy $SIMCAT and getthe best"
        self.aligned_with_us = "text=Aligned with U.S. regulatory"
        self.presale_has_started = "text=Presale has started on the"

    def navigate_to_site(self):
        self.navigate(self.url)

    def select_currency(self, currency: str):
        if currency.upper() == "ETH":
            self.click(self.currency_eth)
        elif currency.upper() == "USDT":
            self.click(self.currency_usdt)
        elif currency.upper() == "CARD":
            self.click(self.currency_card)

    def open_wallet_modal(self):
        self.click(self.buy_with_crypto_btn)

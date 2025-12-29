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
        
        # Presale Widget
        self.presale_widget = ".presale-card" # Assuming based on exploration
        self.currency_eth = "button:has-text('ETH')"
        self.buy_input = "input[placeholder='0']"
        self.buy_with_crypto_btn = "button:has-text('Buy with Crypto')"
        
        # Wallet Modal
        self.wallet_modal = "text=CONNECT A WALLET"
        self.close_modal = "button.modal-close" # Placeholder, will refine if needed

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

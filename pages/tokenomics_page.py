from pages.base_page import BasePage
from playwright.sync_api import Page

class TokenomicsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz/tokenomics"

        # Simcat Tokenomics text
        self.eco_system_reserve = "text=Eco System Reserve 41.1%"
        self.eco_system_reserve_text = "text=Purpose: Mining, blockchain"
        self.estimated_rewards = "text=Estimated Rewards"
    
    def navigate_to_tokenomics(self):
        self.navigate(self.url)





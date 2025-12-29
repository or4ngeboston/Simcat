from pages.base_page import BasePage
from playwright.sync_api import Page

class StakingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://simcat.ssd.uz/staking"
        
        # Staking Stats
        self.staked_balance = "text=Staked Balance"
        self.total_staked = "text=Total Staked"
        self.estimated_rewards = "text=Estimated Rewards"

        # Buttons
        self.withdraw_btn = "button:has-text('Withdraw Staked Tokens')"
        self.buy_and_stake_btn = "button:has-text('Buy And Stake')"
        self.claim_rewards_btn = "button:has-text('Claim Rewards')"

    def navigate_to_staking(self):
        self.navigate(self.url)

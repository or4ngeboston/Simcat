from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_load_state(self, state: str = "networkidle"):
        self.page.wait_for_load_state(state)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def is_clickable(self, selector_or_locator):
        try:
            if isinstance(selector_or_locator, str):
                locator = self.page.locator(selector_or_locator)
            else:
                locator = selector_or_locator
            
            locator.click(trial=True, timeout=5000)
            return True
        except Exception:
            return False


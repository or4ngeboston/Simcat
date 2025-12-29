import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from pages.landing_page import LandingPage
from pages.staking_page import StakingPage

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def landing_page(page):
    return LandingPage(page)

@pytest.fixture
def staking_page(page):
    return StakingPage(page)

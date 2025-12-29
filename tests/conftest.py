import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright
from pages.landing_page import LandingPage
from pages.staking_page import StakingPage
from pages.tokenomics_page import TokenomicsPage
from pages.whitepaper_page import WhitepaperPage
from pages.executive_summary_page import ExecutiveSummaryPage

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

@pytest.fixture
def tokenomics_page(page):
    return TokenomicsPage(page)

@pytest.fixture
def whitepaper_page(page):
    return WhitepaperPage(page)

@pytest.fixture
def executive_summary_page(page):
    return ExecutiveSummaryPage(page)


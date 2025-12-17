from playwright.sync_api import sync_playwright

def get_page(headless=True):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    return playwright, browser, page

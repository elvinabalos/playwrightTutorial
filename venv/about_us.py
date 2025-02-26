from playwright.sync_api import Playwright, sync_playwright, expect


def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://symonstorozhenko.wixsite.com/website-1')

    # assert page.is_hidden("text=Celebrating Beauty and Style")     # Python-specific
    page.wait_for_load_state()

    page.wait_for_selector("text=Celebrating Beauty and Style")

    # expect(page.locator("text=Celebrating Beauty and Style")).to_be_hidden()

    print("Yes")



with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)
import time

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form( "Elvin", "123 binmaley", "elvin@gmail.com", "245435435", "test subject", "test message")
    # expect(page.locator("text=Thanks for submitting!")).to_be_visible()

with sync_playwright() as playwright:
    test_submit_form(playwright)
    # time.sleep(5)
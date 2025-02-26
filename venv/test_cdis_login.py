import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://192.168.0.22:8003/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("superadmin")
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill("superadmin031819")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state()
    print("Hello")
    # page.goto("http://192.168.0.22:8003/control-panel")
    expect(page.get_by_text("Control Panel").nth(1)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

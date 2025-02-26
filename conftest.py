import time

import pytest
from playwright.sync_api import Playwright, expect

import utils.secret_config


@pytest.fixture(scope="session")
def set_up(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    yield page
    page.close()

@pytest.fixture(scope="session")
def login_setup(set_up):
    page = set_up
    page.wait_for_load_state("networkidle")
    # page.pause()
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").click()
    # page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', 'symon.storozhenko@gmail.com')
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill(utils.secret_config.PASSWORD, timeout=2000)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log In"))

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if '$85' in link.text_content():
            assert 'socks' not in link.text_content().lower() and 'notepad' not in link.text_content().lower()

    # product = page.get_by_text("$85").first.locator("xpath=../../../../../..").text_content
    # assert product != 'Socks'
    yield page


@pytest.fixture
def go_to_new_collection(page):
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
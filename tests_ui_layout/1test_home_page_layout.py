from playwright.sync_api import Playwright, sync_playwright, expect
from pytest_playwright.pytest_playwright import context
from conftest import login_setup
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.integration
def test_about_us_section_verbiage(login_setup):
    # page = login_setup()
    # home_page = HomePage(page)
    # assert page.is_visible(home_page.celebrate_header)
    print("test_about_us_section_verbiage")

@pytest.mark.regression
# @pytest.mark.xfail(reason="faketext should not be visible")
def test_about_us_section_verbiage2(login_setup):
    page = login_setup
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    # assert page.is_visible("Shop")
    print("test_about_us_section_verbiage2(login_setup):")
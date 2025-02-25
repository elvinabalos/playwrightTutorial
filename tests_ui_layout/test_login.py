import re
from asyncio import timeout
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(login_setup) -> None:
    # page.goto("https://symonstorozhenko.wixsite.com/website-1/new-collection")    `
    page = login_setup
    assert page.is_visible("text=Welcome")
    print("test_logged_user_can_view_my_orders_menu")
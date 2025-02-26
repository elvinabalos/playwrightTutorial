# import time
import time
from asyncio import timeout

import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                             pytest.param("fakeemail", marks=pytest.mark.xfail),
                                             pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])

@pytest.mark.parametrize("password", ["test123",
                                             pytest.param("fakepassword", marks=pytest.mark.xfail),
                                             pytest.param("test123", marks=pytest.mark.xfail)])

def test_user_can_login(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # page.set_default_timeout(5000)
    page.wait_for_load_state("networkidle")


    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        time.sleep(0.1)

    page.click("[data-testid=\"signUp.switchToSignUp\"]", timeout=2000)
    page.click("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']")
    page.fill('input:below(:text("Email"))', email)
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.fill("input[type='password']", password)
    page.get_by_label("Password").press("Enter")

    page.wait_for_load_state()
    page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1",
                           wait_until="domcontentloaded",
                           timeout=5000)
    # page.wait_for_load_state("[aria-label=\"symon.storozhenko account menu\"]")
    # assert not page.is_visible("text=Log In")
    page.close()
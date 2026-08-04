import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        yield page

        if request.node.rep_call.failed:
            page.screenshot(path="reports/failure.png")

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
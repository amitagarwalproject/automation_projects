from playwright.sync_api import Playwright, expect

from utils.api_base import Base_api


def test_e2e_web(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order

    api_utils = Base_api()
    order_id = api_utils.create_order(playwright)

    # login

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name= "login").click()
    page.get_by_role("button", name= "ORDERS").click()
    row = page.get_by_role("row").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
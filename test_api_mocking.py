
from playwright.sync_api import Page

dummyPayload = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json= dummyPayload)

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=474979374937")

def test_mock_api_response(page:Page):

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    message = page.locator(".mt-4").text_content()
    print(message)


def test_mock_api_request(page:Page):

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    print("pass")


# Import necessary modules from Playwright
from playwright.sync_api import Page, Playwright, expect

# Import Base API utility for API-related operations
from utils.api_base import Base_api

# Define a dummy payload to mock API responses
dummyPayload = {"data": [], "message": "No Orders"}


# Function to intercept and mock API responses
def intercept_response(route):
    """
    This function is used to intercept API responses before they reach the client.
    It replaces the actual API response with a predefined mock response.

    - `route.fulfill(json=dummyPayload)`: This modifies the response with dummyPayload.
    """
    route.fulfill(json=dummyPayload)


# Function to intercept and modify API requests
def intercept_request(route):
    """
    This function is used to intercept outgoing API requests.
    It modifies the request URL before it reaches the server.

    - `route.continue_()`: Allows modifying the request details before sending it.
    """
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=474979374937")


# Test case to mock API response
def test_mock_api_response(page: Page):
    """
    This test case demonstrates how to mock API responses.
    It replaces the real API response for 'get-orders-for-customer' with a dummy response.
    """

    # Mock API response by intercepting the request and replacing it with a dummy response
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    # Navigate to the client login page
    page.goto("https://rahulshettyacademy.com/client")

    # Fill in the email field
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")

    # Fill in the password field
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")

    # Click the login button
    page.get_by_role("button", name="login").click()

    # Click the "ORDERS" button to view orders
    page.get_by_role("button", name="ORDERS").click()

    # Retrieve and print the order message from the page
    message = page.locator(".mt-4").text_content()
    print(message)  # Expected output: "No Orders" (mocked response)


# Test case to mock API request
def test_mock_api_request(page: Page):
    """
    This test case demonstrates how to intercept and modify outgoing API requests.
    The request URL is modified before reaching the server.
    """

    # Mock API request by changing the requested URL
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    # Navigate to the client login page
    page.goto("https://rahulshettyacademy.com/client")

    # Fill in the email field
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")

    # Fill in the password field
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")

    # Click the login button
    page.get_by_role("button", name="login").click()

    # Click the "ORDERS" button to view orders
    page.get_by_role("button", name="ORDERS").click()

    # Click the first "View" button to check order details
    page.get_by_role("button", name="View").first.click()

    # Print a success message to indicate test completion
    print("pass")


# Test case to use session storage for authentication
def test_session_storage(playwright: Playwright):
    """
    This test case demonstrates how to authenticate users using session storage.
    Instead of logging in via UI, a token is directly injected into localStorage.
    """

    # Create an instance of Base_api utility to fetch the authentication token
    api_utils = Base_api()
    get_token = api_utils.get_token(playwright)

    # Launch a browser instance in non-headless mode
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context (similar to a new incognito session)
    context = browser.new_context()

    # Open a new page in the browser
    page = context.new_page()

    # Inject authentication token into local storage before loading the page
    page.add_init_script(f"""localStorage.setItem("token",'{get_token}')""")

    # Navigate to the client orders page
    page.goto("https://rahulshettyacademy.com/client")

    # Click on the "ORDERS" button to view orders
    page.get_by_role("button", name="ORDERS").click()

    # Assert that the "Your Orders" text is visible, confirming successful login
    expect(page.get_by_text("Your Orders")).to_be_visible()

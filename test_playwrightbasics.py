import time

from playwright.sync_api import Page, Playwright, expect

'''playwright is a fixture passed in 'test_playwright_basics' test function, coming from pytest-playwright plugin
   playwright.chromium → This accesses the Chromium browser (which powers Google Chrome and Microsoft Edge.
   .launch(headless=False) → Launches a new Chromium browser instance
   A context in Playwright is like an incognito session, Isolates sessions: Each context has separate cookies, storage, and settings.
   page object opens a new tab in the browser context. 
   Why?
       Each test should use a fresh page to avoid interference with previous tests.
       Simulates real user behavior like opening new tabs.
       .goto(url) → Navigates to a given URL.'''


def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")


'''In pytest-playwright, page is a built-in fixture that automatically provides a fresh browser page for each test.
    The page fixture automatically:
    Launches a browser.
    Opens a new page.
    Closes the browser after the test.'''


def test_playwright_basics2(page:Page):
    page.goto("https://google.com")



'''Locators Used & Their Purpose
Locator	Purpose	Example in Code	Best Use Case
get_by_label("Username:")	Finds input fields linked with a <label>	page.get_by_label("Username:").fill("rahulshettyacademy")	Best for text fields that have <label> elements.
get_by_label("Password:")	Identifies the password input by its label.	page.get_by_label("Password:").fill("learning")	Good for password fields with a <label> tag.
get_by_role("combobox")	Selects dropdowns (combo boxes).	page.get_by_role("combobox").select_option("teach")	Best for dropdowns, selects, or listboxes.
get_by_label("terms")	Clicks a checkbox based on its label.	page.get_by_label("terms").click()	Ideal for checkboxes and radio buttons when a <label> is associated.
get_by_role("button", name="Sign In")	Clicks a button with the text "Sign In".	page.get_by_role("button", name="Sign In").click()	Best for buttons when the text is known.
Limitations of the Locators Used
Locator	Limitations
get_by_label("Username:") & get_by_label("Password:")	❌ Won't work if the input field doesn’t have a <label> element.
get_by_role("combobox")	❌ Might select incorrect dropdowns if multiple combobox elements exist.
get_by_label("terms")	❌ If there's no <label> directly associated with the checkbox, this might fail.
get_by_role("button", name="Sign In")	❌ If the button text changes (e.g., "Login"), this test will break.

Let's understand why get_by_label("Username:") and get_by_label("Password:") won't work if there is no <label> element.

Example 1️⃣: Works with <label>
✅ This will work because the input fields have associated <label> elements.

<label for="username">Username:</label>
<input type="text" id="username" name="username">

<label for="password">Password:</label>
<input type="password" id="password" name="password">
Playwright Code:
page.get_by_label("Username:").fill("testuser")
page.get_by_label("Password:").fill("securepassword")
✔ Why does this work?

The <label> is linked to the input using the for attribute (for="username" → id="username").
Playwright can correctly identify the input field based on the label.
Example 2️⃣: Fails if there's NO <label>
❌ This will not work if the fields do not have <label> elements.

<input type="text" placeholder="Username">
<input type="password" placeholder="Password">
Playwright Code:

page.get_by_label("Username:").fill("testuser")  # ❌ This will fail
page.get_by_label("Password:").fill("securepassword")  # ❌ This will fail
❌ Why does this fail?

There is no <label> element present.
The input fields are only identified by placeholder, not label.
🔥 How to Fix This?
✅ Solution 1: Use get_by_placeholder()
Since the input fields have placeholder attributes, use:

page.get_by_placeholder("Username").fill("testuser")
page.get_by_placeholder("Password").fill("securepassword")
✅ Solution 2: Use locator() with CSS Selectors
If there's no label and no placeholder, use a CSS selector:

page.locator("input[name='username']").fill("testuser")
page.locator("input[name='password']").fill("securepassword")'''

def test_playwright_locators(page:Page):
    page.goto("https:rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy1")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").click()
    page.get_by_role("button", name="Sign In").click()

    '''This is a Playwright assertion that verifies whether an error message is visible on the page.
    get_by_text() finds elements by their visible text (case-sensitive).
    It is useful for error messages, alerts, labels, and static text elements.
    expect(...).to_be_visible()
    This asserts that the selected element is visible on the page.
    If the element is hidden, missing, or incorrect, the test will fail.
    It is useful for verifying error messages, success messages, or UI elements that should be displayed.
    ❌ Limitations of get_by_text()
    Issue	                                            Solution
    Text is dynamic (e.g., error message varies)	Use get_by_role(), locator(), or regex in get_by_text()
    Partial text match needed	                    Use get_by_text("Incorrect username", exact=False)
    Text inside hidden elements	                    to_be_visible() will fail if the element is not visible'''
    expect(page.get_by_text("Incorrect username", exact=False)).to_be_visible()


''' Playwright installs browsers automatically

    When you run playwright install, it downloads Chromium, Firefox, and WebKit.
    These are bundled versions inside Playwright, separate from system-installed browsers.
    Playwright uses its own Firefox version
    
    Even if Firefox is not installed on your system'''


def test_playwright_firefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https:rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy1")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username", exact=False)).to_be_visible()


def test_ui_validation(page:Page):
    page.goto("https:rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").click()
    page.get_by_role("button", name="Sign In").click()
    # expect(page.get_by_text("Incorrect username", exact=False)).to_be_visible()
    time.sleep(5)
    iphone_x=page.locator("app-card>div").filter(has_text="iphone X")
    iphone_x.get_by_role("button", name="Add ").click()
    nokia_edge = page.locator("app-card>div").filter(has_text="Nokia Edge")
    nokia_edge.get_by_role("button", name="Add ").click()
    page.get_by_text(" Checkout",exact=False).click()
    expect(page.get_by_role("row").filter(has_text="iphone X")).to_be_visible()
    print("iphone x verified")
    expect(page.get_by_role("row").filter(has_text="Nokia Edge")).to_be_visible()
    print("nokia edge verified")


def test_child_windows(page:Page):
    page.goto("https:rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info:           # Waits for a popup(child window) to open (expect_popup()).
        page.get_by_role("link").get_by_text("Free Access",exact=False).click()   # Clicks on "Free Access", which opens a new window.
        child_window = new_page_info.value     # Stores the popup window in child_window.
        text = child_window.locator(".red").text_content()   # Extracts and prints text from an element inside the popup.
        text_list = text.split()
        print(text_list)
        for i in text_list:
            if i=="mentor@rahulshettyacademy.com":
                print("mentor found")




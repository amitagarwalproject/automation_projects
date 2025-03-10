import time

from playwright.sync_api import Page, expect


def test_ui_validations(page:Page):

    # use of get_by_placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)

    # handling ALert popup
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    print("hello")

    #handling frames
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="All Access plan").click()
    expect(frame_page.locator("body")).to_contain_text(" Happy Subscibers!")
    print("what's up")

    # handling dynamic tweb tables

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.get_by_role("columnheader").count()):
        if page.get_by_role("columnheader").nth(i).filter(has_text="Price").count()>0:
            price_col_value = i
            print(price_col_value)
            time.sleep(5)
            break
    rice_row = page.get_by_role("row").filter(has_text="Rice")

    expect(rice_row.get_by_role("cell").nth(price_col_value)).to_have_text("37")

# #     generic way to handle web table
#
# from playwright.sync_api import Page, expect
#
# def get_column_index(page: Page, column_name: str) -> int:
#     """Returns the index of the given column name in the table."""
#     headers = page.locator("table th")  # Locating all column headers
#     for i in range(headers.count()):
#         if headers.nth(i).text_content().strip() == column_name:
#             return i
#     raise ValueError(f"Column '{column_name}' not found.")
#
# def get_row(page: Page, row_text: str):
#     """Returns the row locator containing the specified text."""
#     return page.locator("table tr").filter(has_text=row_text)
#
# def get_cell_value(page: Page, row_text: str, column_name: str) -> str:
#     """Returns the cell value for the given row and column."""
#     col_index = get_column_index(page, column_name)
#     row = get_row(page, row_text)
#     return row.locator("td").nth(col_index).text_content().strip()
#
# def test_table_interaction(page: Page):
#     page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#
#     # Example: Get the Price of "Rice"
#     price_of_rice = get_cell_value(page, "Rice", "Price")
#     print(f"Price of Rice: {price_of_rice}")
#
#     # Validate price of "Rice" is 37
#     expect(get_row(page, "Rice").locator("td").nth(get_column_index(page, "Price"))).to_have_text("37")



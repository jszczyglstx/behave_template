from behave import step


@step("Page title is page_title")
def step_impl(context):
    displayed_page_title = context.page.get_page_title()
    expected_page_title = "Some title"
    assert displayed_page_title == expected_page_title, \
        f"Displayed page title: {displayed_page_title} is not equal expected page title: {expected_page_title}"

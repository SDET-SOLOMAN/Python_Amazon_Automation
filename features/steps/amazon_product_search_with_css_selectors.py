from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

AMAZON_HOME_PAGE = 'https://www.amazon.com'
SEARCH_BAR = (By.CSS_SELECTOR, "form#nav-search-bar-form input[type='text']")
SEARCH_ICON = (By.CSS_SELECTOR, "div.nav-right input[class*='rogressive-att']")
SEARCH_RESULT = (By.XPATH, "//div[@class='sg-col-inner']//span[contains(@class, 'tate a-text-bold')]")
ITEMS_IN_CART = (By.XPATH, "//div[@id='nav-cart-count-container']/ span[@id='nav-cart-count']")


@given('Go to Amazon Home Page')
def home_page_of_amazon(context):
    context.driver.get(AMAZON_HOME_PAGE)


@when("Navigate to the Search Bar and input {search_query}")
def search_for_item(context, search_query):
    search_field = context.driver.find_element(*SEARCH_BAR)
    search_field.clear()
    search_field.send_keys(search_query)  # Keys.ENTER)


@when("Click on Amazon Search Icon")
def click_on_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then("Verify {search_result} is on Amazon Page")
def is_search_matching(context, search_result):
    actual_text = context.driver.find_element(*SEARCH_RESULT).text  # Have to use XPath hence CSS Selector
    # not working with linking to the text
    assert search_result == actual_text, f"Expected text was {search_result}, but the actual is {actual_text}"


@then("Verify url contains {search_query}")
def is_url(context, search_query):
    actual_url = context.driver.current_url
    assert search_query in actual_url, f"Expected word in url is {search_query} is missing"


@then('Verify Cart has {num} items in it')
def is_num_items(context, num):
    find_the_cart = context.driver.find_element(*ITEMS_IN_CART).text  # using XPath hence CSS no good with text linking
    assert int(num) == int(find_the_cart), f"Expected num of items was {num}, but the actual is {find_the_cart}"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

AMAZING_HOME = 'https://www.amazon.com'
IS_TODAY = (By.CSS_SELECTOR, "#nav-xshop a[href *= 'nav_cs_gb']")
IS_TODAY_TEXT = (By.XPATH, "//div[@id='slot-2'] // h1")
SEARCH_BAR = (By.CSS_SELECTOR, "#nav-search input[type='text']")
IS_FIRST_ITEM = (By.CSS_SELECTOR, "div.s-main-slot span.a-size-base-plus.a-color-base.a-text-normal")
CLICK_THE_FIRST = (By.XPATH, "//div[@class='sg-col-inner'] // a[contains(@class, "
                             "'xt s-underline-link-text s-link-style a-text-normal')]")
ADD_ITEM = (By.ID, "add-to-cart-button")
NO_THANKS = (By.ID, "attachSiNoCoverage-announce")
PROCEED_CHECKOUT = (By.ID, "attach-sidesheet-view-cart-button-announce")
ACTUAL_CART_ITEM = (By.XPATH, "//div[@class = \"a-row a-spacing-base a-spacing-top-base\"] "
                              "//span[@class= \"a-truncate-cut\"]")


@given("Open Home Page of Amazon")
def amazing_home_page(context):
    context.driver.get(AMAZING_HOME)


@when("Select: Today's Deals Link")
def is_today_deal(context):
    context.driver.find_element(*IS_TODAY).click()


@then("Verify: {search_result} is shown on the Page")
def is_search_gb(context, search_result):
    actual_text = context.driver.find_element(*IS_TODAY_TEXT).text
    assert actual_text == search_result, f"Got {actual_text} expected text was {search_result}"


@when("Search for {query_item} on Search Bar")
def lets_search(context, query_item):
    search_bar = context.driver.find_element(*SEARCH_BAR)
    search_bar.clear()
    search_bar.send_keys(query_item, Keys.ENTER)


@when("Verify {search_text} is in First Item")
def is_first(context, search_text):
    first_item = context.driver.find_elements(*IS_FIRST_ITEM)[0].text
    print(first_item)
    assert search_text in first_item.lower(), f"Expected search query {search_text} not in first item {first_item}"
    return first_item


@when("Get the first item from the Search result")
def click_the_first_item(context):
    context.driver.find_elements(*CLICK_THE_FIRST)[0].click()


@when("Add the item to the cart")
def add_the_item(context):
    context.driver.find_element(*ADD_ITEM).click()
    if len(context.driver.find_elements(*NO_THANKS)) == 1:
        context.driver.find_element(*NO_THANKS).click()
    if len(context.driver.find_elements(*PROCEED_CHECKOUT)) == 1:
        context.driver.find_element(*PROCEED_CHECKOUT).click()


@when("Open Cart Page")
def cart_page(context):
    context.driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")


@then("Verify item in the cart matches {search_text}")
def is_cart_matches_added(context, search_text):
    actual_item = context.driver.find_element(*ACTUAL_CART_ITEM).text
    print(actual_item)
    assert search_text in actual_item.lower(), f"It's not matching"

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait


def browser_init(context):
    """
    :param context: Behave context
    """

    start_chrome = Service('/Users/mikesoloman/Desktop/Python_Amazon_Automation/chromedriver')
    context.driver = webdriver.Chrome(executable_path= "/Users/mikesoloman/Desktop/Python_Amazon_Automation"
                                                       "/chromedriver")
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.driver.wait = WebDriverWait(context.driver, 2)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
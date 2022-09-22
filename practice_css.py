from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

start_the_chrome = Service('C:\\Users\\Buywi\\Desktop\\QA Automation Practice\\'
                           'Python_Amazon_Automation\\chromedriver.exe')
driver = webdriver.Chrome(service=start_the_chrome)
driver.maximize_window()

driver.get('https://www.amazon.com')
sleep(3)
find_the_bar = driver.find_element(By.CSS_SELECTOR, "div.nav-search-field input[type='text']")
find_the_bar.clear()
find_the_bar.send_keys('WATCHES', Keys.ENTER)


actual_text = driver.find_element(By.XPATH, '//div[contains(@class, '
                                            '"a-spacing")]//span[@class="a-color-state a-text-bold"]').text
expected_text = '"WATCHES"'

assert expected_text == actual_text, f"Expected text was {expected_text}, but the actual text is {actual_text}"
driver.quit()
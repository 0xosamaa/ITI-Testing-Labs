from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome("path/to/chromedriver")

driver.get("https://artoftesting.com/sampleSiteForSelenium")

# Task 1:
text_box = driver.find_element(By.ID, "fname")
dropdown = Select(driver.find_element(By.ID, "testingDropdown"))
alert_box = driver.find_element(By.ID, "AlertBox")
confirm_box = driver.find_element(By.ID, "ConfirmBox")
entry_header = driver.find_element(By.CLASS_NAME, "entry-header")


# Task 2:
text_box.send_keys("Text input")
dropdown.select_by_value("Performance")
alert_box.click()
confirm_box.click()

# Task 3:
driver.get("https://artoftesting.com/selenium-tutorial")

# Task 4:
new_page_title = driver.title
print("New page title:", new_page_title)

# Task 5:
driver.back()
previous_page_title = driver.title
print("Previous page title:", previous_page_title)

# Task 6:
# driver.quit()

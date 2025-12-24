from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# cService = webdriver.ChromeService(
#     executable_path='/Users/vishnu/Documents/Programming Courses Exercises and Resources/ZTM Complete Python Developer/AutomationAndTestingWithSeleniumProject/chromedriver')
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(options=options, service=service)

chrome_browser.maximize_window()
# notice the URL has changed from the video to the new demo site!
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()


user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')


time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text


print("Selenium Easy Demo" in chrome_browser.title)


time.sleep(5)
chrome_browser.close()
chrome_browser.quit()

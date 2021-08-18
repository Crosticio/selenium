from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# navigate to

driver.get("https://dev.keepworking.online/")

# Get current URL

# print(f"URL: {driver.current_url}")

#Back

# driver.find_element(by=By.CSS_SELECTOR,value="#navbar > a:nth-child(3)").click()

# driver.back()

# Forward

# driver.forward()

# Refresh

# driver.refresh()

# Title

# print(f"Title: {driver.title}")

# Get window handle

# driver.current_window_handle

# Switching windows or tabs

# Start the driver
# with webdriver.Chrome() as driver:
#     # Open URL
#     driver.get("https://dev.keepworking.online/")

#     # Setup wait for later
#     wait = WebDriverWait(driver, 10)

#     # Store the ID of the original window
#     original_window = driver.current_window_handle

#     # Check we don't have other windows open already
#     assert len(driver.window_handles) == 1

#     # Click the link which opens in a new window
#     driver.find_element(By.CSS_SELECTOR, "body > app-root > app-main-home > app-nav-bar > nav > div.options-menu > div > div.options-menu__loginwrap.options-menu__wrapper--item > button").click()

#     driver.find_element(By.CSS_SELECTOR,"body > ngb-modal-window > div > div > app-login > div > div > div > button").click()

#     # Wait for the new window or tab
#     wait.until(EC.number_of_windows_to_be(2))

#     print(driver.window_handles)

#     # Loop through until we find a new window handle
#     for window_handle in driver.window_handles:
#         if window_handle != original_window:
#             driver.switch_to.window(window_handle)
#             break

# Wait for the new tab to finish loading content
# wait.until(EC.title_is("SeleniumHQ Browser Automation"))

# Closing a window or tab

# driver.close()

# quitting the browser at the end of a session

# driver.quit()

def tearDown():
    driver.quit()

# Window Management

# Get window size

# size_width =  driver.get_window_size().get("width")

# size_height = driver.get_window_size().get("height")

# print(f"width = {size_width}")
# print(f"height = {size_height}")

# set window size

# driver.set_window_size(1024, 768)

# get window position


# Access each dimension individually
# x = driver.get_window_position().get('x')
# y = driver.get_window_position().get('y')

# Or store the dimensions and query them later
# position = driver.get_window_position()
# x1 = position.get('x')
# y1 = position.get('y')

# print(f"position x: {x}")
# print(f"position y: {y}")

# set window position

# Move the window to the top left of the primary monitor
# driver.set_window_position(0, 0)

# maximize window

# driver.maximize_window()

# minimize window

# driver.minimize_window()

# Fullscreen window

# driver.fullscreen_window()

# TakeScreenshot

# driver.save_screenshot("./prueba.png")

# TakeElementScreenShot

# Navigate to url
# driver.get("http://www.example.com")

# ele = driver.find_element(By.CSS_SELECTOR, 'h1')

# Returns and base64 encoded string into image
# ele.screenshot('./image.png')

# Execute Script

# Stores the header element
# header = driver.find_element(By.CSS_SELECTOR, "h1")

# Executing JavaScript to capture innerText of header element
# driver.execute_script("console.log(arguments[0].innerText)", header)

# Print Page


time.sleep(10)

tearDown()
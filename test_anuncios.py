from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import colorama
from colorama import Fore, Back

class TestAnuncios():
  def __init__(self):
    colorama.init()
    self.driver = webdriver.Chrome()

  def cards_ad(self, cards_len, num_group, pos_ad, pos_ad_fw):
    def next_pos_ad(arr):
        return arr[len(arr) - 1] + num_group
    ele_ad = {
        "ad" : [pos_ad],
        "ad_fw" : [pos_ad_fw]
    }
    limit = int(cards_len / num_group)
    i = 1
    while i < limit:
        ad = ele_ad["ad"]
        ele_ad["ad"].append(next_pos_ad(ad))
        ad_fw = ele_ad["ad_fw"]
        ele_ad["ad_fw"].append(next_pos_ad(ad_fw))
        i = i + 1
    return ele_ad

  def presence_ads(self, cards):
    cards_ads = self.cards_ad(len(cards), 7, 2, 6)
    cards_ad = cards_ads["ad"]
    cards_ad_fw = cards_ads["ad_fw"]
    for i in cards_ad:
      assert cards[i].get_attribute("class") == "is-custom-content-card-ad", Back.LIGHTRED_EX + "TEST FALLADO"

    for i in cards_ad_fw:
      assert cards[i].get_attribute("class") == "is-custom-content-card-fw", Back.LIGHTRED_EX + "TEST FALLADO"

  def window_ads(self, cards_ad, original_window):
    for card_ad in cards_ad:
      card_ad.click()
      # if self.driver.current_window_handle != original_window:
      #   self.driver.switch_to.window(original_window)
      # self.wait.until(EC.number_of_windows_to_be(2))
      self.wait.until(EC.new_window_is_opened(self.driver.window_handles))


    # for window_handle in self.driver.window_handles:
    #   if window_handle != original_window:
    #     self.driver.switch_to.window(window_handle)
    #     print(self.driver.current_url)
    #     self.driver.close()
    # self.driver.switch_to.window(original_window)

  def setUp(self):
    self.driver.get("https://dev.keepworking.online/")
    self.driver.maximize_window()
    self.wait = WebDriverWait(self.driver, 10, 2, [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
    self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cookies")))
    cards = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#resultData .cards-wrapper > div")))
    # assert len(cards) == 14, Back.LIGHTRED_EX + f"TEST FALLADO. Se esperaba 14 se obtuvo {len(cards)}"
    # i = 1
    # load = 2
    # while i < load:
    #   self.presence_ads(cards)
    #   self.driver.execute_script("window.scrollTo(0, window.scrollY + document.querySelector('footer').getBoundingClientRect().y - (window.screen.height/3))")
    #   i = i + 1
    #   self.wait.until(EC.url_contains(f"working-{i}"))
    cards_ad = self.driver.find_elements(By.CSS_SELECTOR, "#resultData .cards-wrapper > .is-custom-content-card-ad")
    print(len(cards_ad))
    original_window = self.driver.current_window_handle
    self.window_ads(cards_ad, original_window)

  def teardown(self):
    self.driver.quit()
    print(Back.LIGHTGREEN_EX + Fore.BLACK + "TEST PASADO")
    colorama.deinit()

test = TestAnuncios()
test.setUp()
test.teardown()
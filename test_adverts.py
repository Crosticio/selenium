from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains

class TestAnuncios():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown(self):
        print("TEST SATISFACTORIO")
        self.driver.quit()

    def adverts_index(self):
        i = 1
        limit = int(self.vars["cards_len"] / 7)
        ad = [2]
        ad_fw = [6]
        while i < limit:
            ad.append(ad[len(ad) - 1] + 7)
            ad_fw.append(ad_fw[len(ad_fw) - 1] + 7)
            i += 1

        return { "ad" : ad, "ad_fw" : ad_fw }

    def wait_for_window(self, timeout):
        sleep(round(timeout / 1000))
        # wait = WebDriverWait(self.driver, 10, 5)
        # wait.until(EC.new_window_is_opened(self.vars["window_handles"]))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    # def wait_for_window(self):
    #     for window_handle in self.driver.window_handles:
    #         if window_handle != self.vars["root"]:
    #             return window_handle

    def new_window_handle_ad(self):
        cards_ad = self.driver.find_elements(By.CSS_SELECTOR, ".is-custom-content-card-ad")
        self.vars["root"] = self.driver.current_window_handle

        for card_ad in cards_ad:
            frame = card_ad.find_element(By.CSS_SELECTOR, "iframe")
            self.driver.switch_to.frame(frame)
            self.vars["window_handles"] = self.driver.window_handles
            self.driver.find_element(By.CSS_SELECTOR, ".img_ad").click()
            self.driver.implicitly_wait(2)
            # sleep(2)
            # if expected_conditions.new_window_is_opened is not allow you handle windows then you should use this method with its function avaible
            self.vars["win_ad"] = self.wait_for_window(2000)
            # wait.until(EC.new_window_is_opened(self.vars["window_handles"]))
            # self.vars["win_ad"] = self.wait_for_window()
            self.driver.switch_to.window(self.vars["win_ad"])
            self.driver.close()
            self.driver.switch_to.window(self.vars["root"])

    def new_window_handle_ad_fw(self):
        cards_ad_fw = self.driver.find_elements(By.CSS_SELECTOR, ".is-custom-content-card-fw")

        for card_ad_fw in cards_ad_fw:
            frame = card_ad_fw.find_element(By.CSS_SELECTOR, "iframe")
            self.driver.switch_to.frame(frame)
            self.vars["window_handles"] = self.driver.window_handles
            self.driver.find_element(By.CSS_SELECTOR, ".img_ad").click()
            self.driver.implicitly_wait(2)
            # sleep(2)
            # if expected_conditions.new_window_is_opened is not allow you handle windows then you should use this method with its function avaible
            self.vars["win_ad"] = self.wait_for_window(2000)
            # wait.until(EC.new_window_is_opened(self.vars["window_handles"]))
            # self.vars["win_ad"] = self.wait_for_window()
            self.driver.switch_to.window(self.vars["win_ad"])
            self.driver.close()
            self.driver.switch_to.window(self.vars["root"])

    def test_anuncios(self):
        self.driver.get("https://dev.keepworking.online/")
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10, 2, [NoSuchElementException])
        cookies = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".cookies")))
        cookies.find_element(By.CSS_SELECTOR, ".btn__close > svg").click()
        footer = self.driver.find_element(By.CSS_SELECTOR, "footer")
        self.driver.execute_script("window.scrollTo(0, window.scrollY + arguments[0].getBoundingClientRect().y - (window.screen.height / 3))",footer)
        wait.until(EC.url_contains("working-2"))
        cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#resultData .cards-wrapper > div")))
        self.vars["cards_len"] = len(cards)
        adverts_index = self.adverts_index()
        ad_index = adverts_index["ad"]
        ad_fw_index = adverts_index["ad_fw"]

        #for index in ad_index:
            #assert cards[index].get_attribute("class") == "is-custom-content-card-ad"
        #for index in ad_fw_index:
            #assert cards[index].get_attribute("class") == "is-custom-content-card-fw"

        self.new_window_handle_ad()
        self.new_window_handle_ad_fw()


test = TestAnuncios()
test.test_anuncios()
test.teardown()

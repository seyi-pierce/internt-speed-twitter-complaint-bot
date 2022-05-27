from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speed_test_url = "https://www.speedtest.net/"
        self.driver.get(url=speed_test_url)
        time.sleep(10)
        self.driver.find_element(by=By.CLASS_NAME, value="start-text").click()
        time.sleep(100)
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        time.sleep(5)
        self.driver.quit()


    def tweet_at_provider(self, username, password, down, up):
        twitter_url = "https://twitter.com/home"
        self.driver.get(url=twitter_url)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value="text").send_keys(username + Keys.ENTER)
        time.sleep(10)
        if self.driver.find_element(by=By.NAME, value="text").text == "":
            self.driver.find_element(by=By.NAME, value="text").send_keys("@tolubens" + Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value="password").send_keys(password + Keys.ENTER)
        time.sleep(10)
        tweet = self.driver.find_element(by=By.CLASS_NAME, value="public-DraftStyleDefault-block")
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for "
                        f"{down}down/{up}up?")
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                    'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/'
                                                    'div[2]/div[3]/div/span/span').click()
        self.driver.quit()


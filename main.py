import time
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_HANDLE = "..."
TWITTER_PASSWORD = "..."

right_now = str(dt.datetime.now())

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0
        self.internet_provider = ""
        self.message = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                             'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/'
                                                             'div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                           'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/'
                                                           'div/div[2]/span')
        self.internet_provider = self.driver.find_element(By.CSS_SELECTOR, value=".result-label a")
        self.message = (f"Download: {self.down.text} Mbps\n"
                        f"Upload: {self.up.text} Mbps\n"
                        f"Internet Provider: {self.internet_provider.text}\n"
                        f"{right_now}")

        print(self.message)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")

        time.sleep(3)
        twitter_handle = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                  'div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/'
                                                                  'label/div/div[2]/div/input')
        twitter_handle.send_keys(TWITTER_HANDLE, Keys.ENTER)

        time.sleep(3)
        twitter_password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                                    'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/'
                                                                    'div/div[3]/div/label/div/div[2]/div[1]/input')
        twitter_password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

        time.sleep(3)
        comment = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                           'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                           'div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/'
                                                           'div/div/div[2]/div/div/div/div')
        comment.send_keys(self.message)

        time.sleep(2)
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                        'div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/'
                                                        'div/div/button/div/span/span')
        post.click()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()

from selenium import webdriver

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_HANDLE = "..."
TWITTER_PASSWORD = "..."


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Safari
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()

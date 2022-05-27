import time
from internet_speed import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = input("Give twitter username")
TWITTER_PASSWORD = input("Give twitter password")
chrome_driver_path = "C:/Users/19402/Applications/chromedriver"

twitter_bot = InternetSpeedTwitterBot(chrome_driver_path)
twitter_bot.get_internet_speed()
time.sleep(10)
twitter_bot.tweet_at_provider(username=TWITTER_EMAIL, password=TWITTER_PASSWORD, down=PROMISED_DOWN, up=PROMISED_UP)




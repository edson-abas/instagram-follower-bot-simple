from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
TARGET_ACCOUNT = os.environ["TARGET_ACCOUNT"]


class InstaFollower:

    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        time.sleep(10)

        not_now_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button')
        not_now_button.click()
        time.sleep(5)

        notifications_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notifications_button.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(5)

        followers_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(8)

        modal = self.driver.find_element(By.CSS_SELECTOR, "._aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        counter = 0
        for button in buttons:
            if button.text == "Seguir":
                button.click()
                time.sleep(1)
                counter += 1
                if counter >= 10:
                    break


bot = InstaFollower()
bot.login()
time.sleep(1)
bot.find_followers()
bot.follow()
bot.driver.quit()

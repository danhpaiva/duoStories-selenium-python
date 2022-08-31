from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Welcome - Loopizinho #


def AcessUrl(driver):
    driver.get('http://www.google.com')
    time.sleep(3)


def GoToSearch(driver):
    inputButon = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    inputButon.send_keys("Some Text" + Keys.ENTER)
    time.sleep(3)


# Let's Code #
while (True):
    driver = webdriver.Edge('.\edgedriver_win64\msedgedriver.exe')
    AcessUrl(driver)
    GoToSearch(driver)
    driver.back()
    time.sleep(2)
    driver.close()
    time.sleep(3)

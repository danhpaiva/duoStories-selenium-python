from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Welcome ~ danhpaiva #
# ENV's
urlDuo = 'https://www.duolingo.com/'
urlExercise = 'https://www.duolingo.com/stories/en-pt-good-morning?mode=read'
user = 'danhpaiva'
password = 'Password'
pathSystem = '.\edgedriver_win64\msedgedriver.exe'

driver = webdriver.Edge(pathSystem)


def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)


def AcessSite(driver):
    driver.get(urlDuo)
    buttonFirstPage = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[2]/button/span')
    buttonFirstPage.click()
    time.sleep(3)


def InsertCredentials(user, password):
    Login = driver.find_element(
        By.XPATH, '//*[@id="overlays"]/div[4]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input')
    Login.send_keys(user + Keys.TAB + password + Keys.ENTER)
    time.sleep(5)


def MakeExercise(driver):
    driver.get('https://www.duolingo.com/stories/en-pt-good-morning?mode=read')
    startLesson = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div/div/div/div/div[3]/button')
    startLesson.click()

    startLesson = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div/div/div/button')
    startLesson.click()


AcessSite(driver)
InsertCredentials(user, password)
MakeExercise(driver)

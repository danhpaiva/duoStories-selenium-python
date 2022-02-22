from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Welcome #

# Credentials
user = 'danhpaiva'
password = 'zzz'
driver = webdriver.Chrome(executable_path='.\chromedriver.exe')


def AcessSite(driver):
    driver.get('https://www.duolingo.com/')
    buttonFirstPage = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/span[1]/div/div[1]/div[2]/div[2]/button/span')
    buttonFirstPage.click()
    time.sleep(2)


def InsertCredentials(user, password):
    Login = driver.find_element_by_xpath(
        '//*[@id="overlays"]/div[5]/div/div/form/div[1]/div[1]/div[1]/label/div/input')
    Login.send_keys(user + Keys.TAB + password + Keys.ENTER)
    time.sleep(3)


def AccessStories(driver):
    driver.get('https://www.duolingo.com/learn')
    buttonStories = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[3]/div[2]/div[3]/a/span')
    buttonStories.click()
    time.sleep(3)
    selectStorie = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[4]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]')
    selectStorie.click()
    time.sleep(2)
    confirmStorie = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[4]/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/a[1]')
    confirmStorie.click()
    time.sleep(3)


def MakeExercise(driver):
    driver.get('https://www.duolingo.com/stories/en-pt-good-morning?mode=read')
    startLesson = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/div[3]/div/div/div/button')
    startLesson.click()


AcessSite(driver)
InsertCredentials(user, password)
AccessStories(driver)
MakeExercise(driver)

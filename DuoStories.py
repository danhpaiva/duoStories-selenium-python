from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Welcome ~ danhpaiva #
# ENV's
urlDuo = 'https://www.duolingo.com/'
urlExercise = 'https://www.duolingo.com/stories/en-pt-good-morning?mode=read'
user = 'danhpaiva'
password = ''
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
    try:
        buttonFirstPage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[2]/button/span')))
    finally:
        buttonFirstPage.click()


def InsertCredentials(user, password):
    Login = driver.find_element(
        By.XPATH, '//*[@id="overlays"]/div[4]/div/div[2]/form/div[1]/div[1]/div[1]/label/div/input')
    Login.send_keys(user + Keys.TAB + password + Keys.ENTER)


def Confirm(driver):
    time.sleep(2)
    startLesson = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[3]/div/div/div/button').click()


def QuestionOne(driver):
    time.sleep(2)
    startLesson = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[6]/div/ul/li[1]/button').click()

    startLesson = driver.find_element(
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[6]/div/ul/li[2]/div/div/span[1]').click()


def QuestionOneListening(driver):
    time.sleep(3)
    listForAsc = [1, 2, 3, 4]
    for item in listForAsc:
        for item in listForAsc:
            nextLetter = driver.find_element(
                By.XPATH,
                f'/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[10]/div/div/div[{item}]/button').click()
            time.sleep(0.75)


def QuestionTwoListening(driver):
    time.sleep(3)
    listForAsc = [1, 3, 7, 13]
    for item in listForAsc:
        for item in listForAsc:
            nextLetter = driver.find_element(
                By.XPATH,
                f'/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[13]/div/div[2]/div/span[{item}]/button').click()
            time.sleep(0.75)


def QuestionThreeListening(driver):
    time.sleep(2)
    listForAsc = [1, 2, 3]
    for item in listForAsc:
        for item in listForAsc:
            nextLetter = driver.find_element(
                By.XPATH,
                f'/html/body/div[1]/div/div/div/div/div[1]/div[1]/div[18]/div/ul/li[{item}]/button').click()
            time.sleep(0.75)


def MakeExercise(driver):
    driver.get('https://www.duolingo.com/stories/en-pt-good-morning?mode=read')
    time.sleep(3.3)
    startLesson = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div/div/div/div/div[3]/button')
    startLesson.click()
    time.sleep(3)

    listFive = [1, 2, 3, 4, 5]
    for item in listFive:
        Confirm(driver)
        print(item)

    QuestionOne(driver)
    Confirm(driver)
    Confirm(driver)
    QuestionOneListening(driver)

    for item in listFive:
        Confirm(driver)
        print(item)

    QuestionTwoListening(driver)

    for item in listFive:
        Confirm(driver)
        print(item)

    Confirm(driver)
    QuestionThreeListening(driver)

    listFive = [1, 2, 3, 4, 5, 6, 7]
    for item in listFive:
        Confirm(driver)
        print(item)


AcessSite(driver)
InsertCredentials(user, password)
MakeExercise(driver)

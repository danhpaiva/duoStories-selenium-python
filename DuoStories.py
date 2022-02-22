from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Credentials
user = 'danhpaiva'
password = 'zzz'

driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
driver.get('https://www.duolingo.com/')

buttonFirstPage = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div/span[1]/div/div[1]/div[2]/div[2]/button/span')
buttonFirstPage.click()

Login = driver.find_element_by_xpath(
    '//*[@id="overlays"]/div[5]/div/div/form/div[1]/div[1]/div[1]/label/div/input')
Login.send_keys(user + Keys.TAB + password + Keys.ENTER)

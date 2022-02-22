from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
driver.get("https://www.duolingo.com/")

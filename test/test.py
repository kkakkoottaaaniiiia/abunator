from selenium import webdriver
import time

#ローカルにあるChromeDriver.exeをつかっている
driver = webdriver.Chrome("C:/Users/School/Desktop/test/chromedriver_win32/chromedriver.exe")

driver.get("https://abunatorroute.azurewebsites.net/")


time.sleep(10)

driver.quit()

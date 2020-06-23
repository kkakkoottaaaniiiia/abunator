from selenium import webdriver
import time

#githubのChromeDriver.exeをつかいたい 現状ローカルなので他の人が使えない
#Cドライブ直下などメンバーで統一すれば使える
driver = webdriver.Chrome("C:/Users/School/Desktop/test/abunator/abunator/test/chromedriver.exe")

#こちらのGitHubから持ってきたい
#driver = webdriver.Chrome(executable_path="https://github.com/kkakkoottaaaniiiia/abunator/tree/master/test/chromedriver.exe")

#abunatorを起動
driver.get("https://abunatorroute.azurewebsites.net/")

#5秒待機
time.sleep(5)

#start.click
start=driver.find_element_by_class_name("start")
start.click()

#質問画面はテストが短くて済むアライグマにしている
time.sleep(5)
no = driver.find_element_by_class_name("button")
no.click()

#10秒待機
time.sleep(10)

#ブラウザ閉じる
driver.quit()

from selenium import webdriver
import time

#githubのChromeDriver.exeをつかいたい 現状ローカルなので他の人が使えない
#Cドライブ直下などメンバーで統一すれば使える
driver = webdriver.Chrome("C:/Users/School/Desktop/test/abunator/abunator/test/chromedriver.exe")

#こちらのGitHubから持ってきたい
#driver = webdriver.Chrome(executable_path="https://github.com/kkakkoottaaaniiiia/abunator/tree/master/test/chromedriver.exe")

#abunatorを起動
driver.get("https://abunatorroute.azurewebsites.net/")

#3秒待機
time.sleep(3)

#start.click
start=driver.find_element_by_class_name("start")
start.click()

#質問画面は[はい]だけ選択
#nameを参照すると「はい」以外も選択してクリックできる?
#no = driver.find_element_by_name('いいえ')

#Xpathの場合
#driver.findElement(By.xpath("//input[@value='はい']")).click();

time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()
time.sleep(3)
no = driver.find_element_by_class_name("button")
no.click()

#最初に戻る
time.sleep(3)
back = driver.find_element_by_class_name("start")
back.click()

#図鑑に画面遷移
time.sleep(3)
picbook = driver.find_element_by_class_name("picture_book")
picbook.click()



#図鑑で特定の生物を指定し、画面遷移
time.sleep(3)
#setumei = driver.find_element_by_xpath("//input[@value='1']").click()
setumei = driver.find_element_by_xpath("//input[@src='../static/imgs/1.png']").click()

#図鑑に戻る
time.sleep(3)
back = driver.find_element_by_class_name("start")
back.click()

#最初に戻る
time.sleep(3)
last = driver.find_element_by_tag_name("a")
last.click()

#5秒待機
time.sleep(5)

#ブラウザ閉じる
driver.quit()

from selenium import webdriver
import user
import time


username="tcnumber"
password="tcpassword"


driver_path="chromedriver.exe"
browser=webdriver.Chrome()

browser.get("https://giris.turkiye.gov.tr/Giris/gir")
time.sleep(1)

username=browser.find_element_by_name("tridField")
password= browser.find_element_by_name("egpField")

username.send_keys(user.uname)
password.send_keys(user.pw)

time.sleep(1)

submit = browser.find_element_by_name("submitButton")
submit.click()
time.sleep(2)

browser.get("https://www.turkiye.gov.tr/mill-savunma-bakanligi")
time.sleep(2)

arama=browser.find_element_by_name("aranan")
arama.send_keys("Hizmet Tercih")
time.sleep(1000)


browser.close()

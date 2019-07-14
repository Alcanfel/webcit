import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import queue

list_url=[]
file_sound="LYNC_howler.wav"
sleep=60

# Открываем файл со ссылками и перемещаем в список
with open('url.txt', "r") as f:
    list_url=f.read().split("\n")

#Создаем класс webdriver на InternetExplorer
driver = webdriver.Ie(executable_path= "IEDriverServer.exe")

#В бесконечном цикле перебираем элемент каждого списка, воспроизводим звук и засыпаем на sleep секунд
while True:
    for url in list_url:
        driver.get(url)
        winsound.PlaySound(file_sound, winsound.SND_FILENAME)
        time.sleep(sleep)
        driver.switch_to.window(driver.window_handles[-1])
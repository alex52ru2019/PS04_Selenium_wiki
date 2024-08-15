from selenium import webdriver # импорт библиотеки
from selenium.webdriver import Keys # импорт клавиш
from selenium.webdriver.common.by import By # импорт локаторов (поиск элементов через DOM
import time
import random
import pprint

driver = webdriver.Chrome() # создать браузер
driver.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0") # перейти на страницу



while True:
    what_do = input("Что делать? \n1 - Листать параграфы статьи"
                    "\n2 - Переходить на одну из связанных статей "
                    "\n3 - новый поиск"
                    "\n0 - выход\n")

    if what_do != "1" and what_do != "2" and what_do != "0" and what_do != "3":
        print("Неверное значение")

    elif what_do == "0":
        driver.quit() # закрыть браузер
        break

    elif what_do == "1":
        paragraphs = driver.find_elements(By.TAG_NAME, "p") # найти все параграфы
        for paragraph in paragraphs:
            pprint.pprint(paragraph.text) # вывести текст параграфа
            if input("1 - остановиться, Enter - следующий параграф ") == '1': break # листать параграфы

    elif what_do == "2":
        links = []
        print("перехожу по ссылке, пожалуйста, подождите") # ссылок много. прога тормозит
        for element in driver.find_elements(By.TAG_NAME, "a"): # найти все ссылки
            cl = element.get_attribute("class") # new - нет такой статьи
            hr = element.get_attribute("href") # # - нет такой статьи
            if cl != "new" and hr != "#":
                links.append(element) # добавить ссылку в список
        pprint.pprint(links) # вывести ссылки
        link = random.choice(links) # выбрать случайную ссылку
        driver.get(link.get_attribute("href")) # перейти на выбранную ссылку

    elif what_do == "3":
        what_find = input("Что искать? ")
        search_box = driver.find_element(By.ID, "searchInput")  # найти поле поиска
        search_box.send_keys(what_find)  # ввести в строку поиска Википедии то, что ввел пользователь
        search_box.send_keys(Keys.RETURN)  # нажать Enter
        time.sleep(10)

        for element in driver.find_elements(By.TAG_NAME, "div"): # найти все ссылки
            cl = element.get_attribute("class") # new - нет такой статьи
            if cl == "mw-search-results-container":
                driver.find_element(By.LINK_TEXT, value=what_find).click()  # перейти на первую ссылку


        #driver.find_element(By.LINK_TEXT, value=what_find).click()  # перейти на первую ссылку
        #driver.find_element(By.LINK_TEXT, what_find).click() # перейти на первую ссылку

#input("нажмите Enter для завершения") # что бы браузер сам не закрывался

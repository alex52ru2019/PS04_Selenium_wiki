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
        for element in driver.find_elements(By.TAG_NAME, "p"): #ищу все ссылки в параграфах
            cl = element.get_attribute("class")
            if cl != "reference-text" and cl != "new" and cl != "mw-editsection": # сноски и new - нет такой статьи
                try:
                    links.append(element.find_element(By.TAG_NAME, "a").get_attribute("href")) # найти ссылки
                    #print("add")
                except:
                    #print("error")
                    pass
        link = random.choice(links) # выбрать случайную ссылку
        driver.get(link) # перейти по ссылке




    elif what_do == "3":
        what_find = input("Что искать? ")
        print(f"Ищу {what_find} и перехожу по ссылке, пожалуйста, подождите") # прога тормозит
        search_box = driver.find_element(By.ID, "searchInput")  # найти поле поиска
        search_box.send_keys(what_find)  # ввести в строку поиска Википедии то, что ввел пользователь
        search_box.send_keys(Keys.RETURN)  # нажать Enter
        time.sleep(1)

        for element in driver.find_elements(By.TAG_NAME, "div"): # найти все ссылки
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading":
                #print(cl)
                first_link = element.find_element(By.TAG_NAME, "a").get_attribute("href")  # перейти на первую ссылку
                driver.get(first_link)
                break

#input("нажмите Enter для завершения") # что бы браузер сам не закрывался

from selenium.common.exceptions import TimeoutException, NoSuchElementException
import numpy as np
import time
from selenium import webdriver
from Searchengines.Extract_Models import extract_model_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import pandas as pd
import re
from Searchengines.ConverExtract import convert_symbols_in_brackets
import os
import uuid

def process_element(element, row, index, df):
    print("process_element начался")
    try:
        link = element.find_element(By.XPATH,".//a[@class='catalog-item-regular-desktop__title-link ddl_product_link']")
        magazin = element.find_element(By.XPATH, ".//span[@class='merchant-info__name']").text
        print(f"Magazin {magazin}")
        print(link.get_attribute('href'))

        text = extract_model_name(link.text)
        print(f"Model name: {text}")

        price = element.find_element(By.XPATH, ".//div[@class='catalog-item-regular-desktop__price']").text
        print(f"Price: {price}")

        text = text.replace("BRAIT", "").replace("Brait", "").replace("brait", "")

        our_text = extract_model_name(row.replace("BRAIT", "").replace("Brait", "").replace("brait", ""))
        text_element = convert_symbols_in_brackets(text)
        text_element = re.sub(r'[^\w\s]', '', text_element).replace(" ", "").lower()
        our_text = convert_symbols_in_brackets(row)
        our_text = re.sub(r'[^\w\s]', '', our_text).replace(" ", "").lower()

        text_element = text_element.replace("BRAIT", "").replace("brait", "")

        pattern = rf'{our_text}$|{our_text}(?![a-z])'
        matches = re.findall(pattern, text_element)
        print(f"Наш текст = {our_text} не наш текст = {text_element}")

        if matches:
            print(f"Цена {price} Магазин {magazin} Валуе {text}")
            new_data = {
                'Наименование': df.iloc[index, 3],
                'Store Name': magazin,
                'Price': price,
                'Link': link.get_attribute("href")
            }
            row_index = df.index[df['Наименование'] == new_data['Наименование']]
            if len(row_index) > 0:
                store_col = f"{' '.join(new_data['Store Name'].split()).title()}"
                if store_col in df.columns:
                    df.loc[row_index, store_col] = new_data['Price']
                    df.loc[row_index, f"{store_col} Link"] = new_data['Link']
                else:
                    df[store_col] = np.nan
                    df.loc[row_index, store_col] = new_data['Price']
                    df.loc[row_index, f"{store_col} Link"] = new_data['Link']
            else:
                new_row = {
                    'Наименование': new_data['Наименование'],
                    'Store A': np.nan,
                    'Store B': np.nan,
                    'Store C': np.nan
                }
                store_col = f"{' '.join(new_data['Store Name'].split()).title()}"
                new_row[store_col] = new_data['Price']
                new_row[f"{store_col} Link"] = new_data['Link']
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            df.to_excel("itog.xlsx", index=False)
    except Exception as e:
        print(f"Ошибка: {e}")


def Sbermegasearch(e, path, lock, X, Y, positions):
    custom_dir = f"driver"
    unique_id = str(uuid.uuid4())
    # Создаем директорию, если она не существует
    os.makedirs(custom_dir, exist_ok=True)

    # Создаем патчер с указанием пользовательского пути для сохранения chromedriver
    patcher = uc.Patcher(executable_path=os.path.join(custom_dir, 'chromedriver.exe'))
    patcher.auto()  # Автоматическая настройка патчера

    # Опции для Chrome
    options = webdriver.ChromeOptions()
    # Используем уникальные пользовательские данные и профиль для каждого процесса
    options.add_argument(f"--user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data/{unique_id}")
    options.add_argument(f'--profile-directory=Profile_{unique_id}')

    # Создание экземпляра Chrome с патчером
    driver = uc.Chrome(options=options, patcher=patcher, driver_executable_path=fr"C:\Users\user\PycharmProjects\SberMegaFind\driver\chromedriver.exe")
    driver.set_window_size(X, Y)
    driver.set_window_position(*positions, windowHandle='current')
    file_path = path.split("_")[0]
    file_path = rf'{file_path}_{e + 1}.xlsx'
    df = pd.read_excel(file_path)
    lock.release()

    for index, row in df.iloc[:, 3].items():
        retries = 3
        for attempt in range(retries):
            # try:
                driver.get(
                    "https://megamarket.ru/catalog/?q=" + "BRAIT%20" + df.iloc[index, 1].split()[0] + " " + df.iloc[
                        index, 3])
                time.sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                wait = WebDriverWait(driver, 10)

                try:
                    driver.find_element(By.XPATH, "//h1[@class='catalog-header__title']")
                    print("Ne naideno")
                except NoSuchElementException:
                    print("Найдено")
                    elementozs = driver.find_elements(By.XPATH,"//div[@class='catalog-item-regular-desktop ddl_product catalog-item-desktop']")
                    print("Старт process_element")
                    for element in elementozs:
                        process_element(element, row, index, df)
            #     break
            # except ConnectionResetError as e:
            #     print(f"Connection error: {e}. Attempt {attempt + 1} of {retries}")
            #     time.sleep(5)
            # except Exception as e:
            #     print(f"Ошибка: {e}")
            #     break

    driver.close()
    driver.quit()


def remove_after_lowercase(input_string):
    for i, char in enumerate(input_string):
        if char.islower():
            return input_string[:i]
    return input_string

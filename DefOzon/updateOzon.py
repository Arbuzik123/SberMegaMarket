from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait
import time
import undetected_chromedriver as uc
from DefOzon.Find_Captcha import Captcha
import requests
def updateSberMega(e, path, lock,X,Y,positions):
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
    # options.add_argument(f'--profile-directory=Profile 1')
    driver = uc.Chrome(options=options)
    driver.set_window_size(X, Y)
    driver.set_window_position(*positions, windowHandle='current')
    file_path = path.split("_")[0]
    file_path = rf'{file_path}_{e + 1}.xlsx'
    df = pd.read_excel(file_path)
    lock.release()
    print("UpdateSM rabotaet")
    for col_name in df.columns[4:]:
        for index, value in df[col_name].items():
            if str(value) != "nan" and pd.api.types.is_numeric_dtype(value) == False and str(value).startswith('http'):
                driver.get(value)
                time.sleep(2)
                wait = WebDriverWait(driver, 1)
                try:
                    w8 = wait.until(EC.presence_of_element_located(("xpath", "//span[@class='sales-block-offer-price__price-final']")))
                    price = driver.find_element("xpath", "//span[@class='sales-block-offer-price__price-final']").text.replace(" ₽","")
                    print(price)
                except:
                    price = "Нет в наличии"
                    time.sleep(3)
                    # driver.delete_all_cookies()
                    # driver.get(value)
                    # try:
                    #     w8 = wait.until(EC.presence_of_element_located(
                    #         ("xpath", "//span[@class='sales-block-offer-price__price-final']")))
                    #     price = driver.find_element("xpath",
                    #                                 "//span[@class='sales-block-offer-price__price-final']").text.replace(
                    #         " ₽", "")
                    #     print(price)
                    # except:
                    #     price = "Нет в наличии"
                        # driver.delete_all_cookies()
                        # driver.get(value)
                    # driver.close()
                    # driver = uc.Chrome(options=options)
                    # driver.set_window_size(X, Y)

                price1 = re.sub(r"\D", "", price)
                # _%H-%M-%S
                # current_date = datetime.datetime.now().strftime('%d-%m-%Y')
                # new_column_name = f'Цена за {current_date}'
                # # df[new_column_name] = current_date
                # df.loc[index, new_column_name] = price1
                prev_col_index = df.columns.get_loc(col_name) - 1
                prev_col_name = df.columns[prev_col_index]
                # df[new_column_name] = current_date
                df.loc[index, prev_col_name] = price1
                df.to_excel(file_path, index=False)
    driver.quit()


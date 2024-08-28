import time
from datetime import datetime
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
import pandas as pd
import re
def Captcha(driver):
    while True:
        try:
            driver.find_element(By.XPATH, "//input[@class='CheckboxCaptcha-Button']").click()
            time.sleep(5)
            wait = WebDriverWait(driver, 20)
            try:
                driver.find_element(By.XPATH, "//*[contains(text(),'Нажмите в таком порядке')]")
                # driver.close()
                # driver.quit()
                # driver = create_proxy_webdriver(1)
                # driver.execute_script("window.localStorage.clear();")  # Очистить Local Storage
                # driver.execute_script("window.sessionStorage.clear();")  # Очистить Session Storage
                # driver.get(link)
                moreProds = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-zone-name='snippetList']/div")))
            except:
                print("Капча закончилась")
                break
        except:
            print("Капчи нет")
            break
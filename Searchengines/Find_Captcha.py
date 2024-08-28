import time
from selenium.webdriver.common.by import By
def Captcha(driver,product,link):
        try:
            driver.find_element(By.XPATH, "//input[@class='CheckboxCaptcha-Button']").click()
            time.sleep(5)
            try:
                driver.find_element(By.XPATH, "//*[contains(text(),'Нажмите в таком порядке')]")
                time.sleep(50)
                # driver.close()
                # driver.quit()
                # driver = create_proxy_webdriver(1)
                # driver.execute_script("window.localStorage.clear();")  # Очистить Local Storage
                # driver.execute_script("window.sessionStorage.clear();")  # Очистить Session Storage
                # try:
                #     driver.get(link)
                # except:
                #     driver.get("https://market.yandex.ru/")
                #     driver.find_element(By.XPATH, "//input[@id='header-search']").clear()
                #     driver.find_element(By.XPATH, "//input[@id='header-search']").send_keys(product)
                #     driver.find_element(By.XPATH, "//button[@data-auto='search-button']").click()
                #     time.sleep(1)
            except:
                print("Капча закончилась")
        except:
            print("Капчи нет")
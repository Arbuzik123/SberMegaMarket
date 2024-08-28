import time

import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import random
def create_webdriver(i):
    print("NeProxy")
    # proxy_list = "proxies.txt"
    # proxy = random.choice(proxy_list)
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    # num_profile = user.num_profile
    # chrome_options.add_argument('--allow-profiles-outside-user-dir')
    # chrome_options.add_argument('--enable-profile-shortcut-manager')
    # chrome_options.add_argument(r'user-data-dir=C:/Users/Dimulka/AppData/Local/Google/Chrome/User Data — копия')
    # chrome_options.add_argument(f'--profile-directory=Profile 1')
    # chrome_options.add_argument(f'--remote-debugging-port={current_port}')
    # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument("--headless")
    service = Service(async_mode = True)
    driver = uc.Chrome(options=chrome_options,service = service)

    driver.set_window_size(1000,800)
    # time.sleep(20)
    # time.sleep(50)
    # add_data_to_browsers(user_id,driver)
    return driver
# def read_proxies(filename):
#     with open(filename, 'r') as file:
#         proxies = [line.strip() for line in file]
#     return proxies
def create_proxy_webdriver(i):
    print("Proxy")
    # proxy_list = "proxies.txt"
    # proxy = random.choice(proxy_list)
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    # num_profile = user.num_profile
    # chrome_options.add_argument('--allow-profiles-outside-user-dir')
    # chrome_options.add_argument('--enable-profile-shortcut-manager')
    # chrome_options.add_argument(r'user-data-dir=C:/Users/Dimulka/AppData/Local/Google/Chrome/User Data')
    # chrome_options.add_argument(f'--profile-directory=Default')
    # chrome_options.add_argument(f'--remote-debugging-port={current_port}')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument("--headless")
    service = Service(async_mode = True)
    # extension_path = rf"C:\Users\Dimulka\AppData\Local\Google\Chrome\User Data\Default\Extensions\gkojfkhlekighikafcpjkiklfbnlmeio.rar"
    # chrome_options.add_extension(extension_path)
    driver = uc.Chrome(options=chrome_options,service = service)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
      '''
    })
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver.set_window_size(1000,800)
    # time.sleep(20)
    # time.sleep(50)
    # add_data_to_browsers(user_id,driver)
    return driver
# def read_proxies(filename):
#     with open(filename, 'r') as file:
#         proxies = [line.strip() for line in file]
#     return proxies
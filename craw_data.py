import random
import time

import requests
import re
from selenium import webdriver

RANDOM_DELAY = [0.4, 1.3, 2.3, 0.7, 0.5, 0.6, 2.1, 1.7, 1.9, 0.9]


def delay():
    time.sleep(random.choice(RANDOM_DELAY))


def longDelay():
    LONG_DELAY = RANDOM_DELAY * 10
    time.sleep(random.choice(LONG_DELAY))


options = webdriver.ChromeOptions()
uas = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
]
user_ag = random.choice(uas)
options.add_argument('User-Agent=%s'%user_ag)
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('blink-settings=imagesEnabled=false')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe', options=options)
#或者  使用下面的设置, 提升速度

driver.get('https://www.kaggle.com/giripujar/hr-analytics')
delay()
driver.execute_script("var action=document.documentElement.scrollTop=3000")
driver.close()
driver.quit()




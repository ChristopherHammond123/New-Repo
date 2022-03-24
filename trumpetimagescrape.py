import selenium

from selenium.webdriver import Chrome

driver = Chrome("/home/christopher/miniconda3/envs/selenium/conda-meta/TrumpetFolder2/Trumpetimagepackage/Test")

from webdriver_manager.chrome import ChromeDriverManager

driver = Chrome(ChromeDriverManager().install())

driver.get("https://www.johnpacker.co.uk")

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import ChromeOptions

import pandas as pd

import uuid

class Scraper:
    def __init__(self, url:str="https://www.johnpacker.co.uk"):
        options = ChromeOptions()
        options.add_argument('--headless')
        self.driver = Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get(url)
        
if __name__ == '__main__':
    bot = Scraper()

cookies_button = driver.find_element_by_xpath('//*[@id="cookie_banner_all"]')
cookies_button.click()

search_bar = driver.find_element_by_xpath('//*[@id="header_search_search_for"]')
search_bar.click()
search_bar.send_keys('Trumpet')
search_bar.send_keys(Keys.ENTER)

container = driver.find_element_by_xpath('//div[@class="row prod_wrapper"]')
trumpet_list = container.find_elements_by_xpath('./div')
data2 = {"UUID2": [],"Image": []}
num_trumpet = len(trumpet_list)
new_id = uuid.uuid4()
for i in range(num_trumpet):
    container = driver.find_element_by_xpath('//div[@class="row prod_wrapper"]')
    trumpet = container.find_elements_by_xpath('./div')[i]
    trumpet.click()
    time.sleep(5)
    data2['UUID2'].append(new_id)
    try:
        Image = driver.find_element_by_xpath('//*[@id="main_cycle"]/li[2]/a/span[1]/img').get_attribute('src')
        data2['Image'].append(Image)
    except NoSuchElementException:
        data2['Image'].append(None)  
    driver.back()
    time.sleep(2)
    print(data2)
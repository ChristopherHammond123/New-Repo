from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import pandas as pd

class Scraper:
    '''
    This class is a scraper that can browse websites
    Parameters
    --------------------------------
    url: str
        Thelink that we want to visit
    Attribute
    --------------------------------
    driver:
        This is the driver object
    '''
    def __init__(self, url:str="https://www.johnpacker.co.uk"):
        options = ChromeOptions()
        options.add_argument('--headless')
        self.driver = Chrome(ChromeDriverManager().install(), options=options) 
        self.driver.get(url)

    def accept_cookies(self,xpath):
        '''
        This method finds and clicks the accept cookies button
        Parameters
        ----------------------------
        xpath: str
            The xpath of the cookies button
        '''
        time.sleep(2)
        cookies = self.driver.find_element_by_xpath(xpath)
        cookies.click()

    def search(self, xpath2):
        '''
        This method finds, clicks and sends keys to the search bar
        Parameters
        -----------------------------
        xpath2: str
            The xpath of the search bar
        '''
        search_bar = self.driver.find_element_by_xpath(xpath2)
        search_bar.click()
        search_bar.send_keys('Trumpet')
        search_bar.send_keys(Keys.ENTER)

    def find_container(self, xpath3):
        '''
        Finds container clicks trumpet and scrapes data from website.
        Parameters
        -----------------------------
        xpath3: str
            The xpath of the container
        '''
        return self.driver.find_element_by_xpath(xpath3)

    def pull_data(self, xpath4, xpath5, xpath6, xpath7, xpath8, xpath9, xpath10, xpath11, xpath12, xpath13, xpath14):
        '''
        Clicks trumpet and scrapes data from website.
        Parameters
        -----------------------------
        xpath4: str
            The xpath of the element
        xpath5: str
            The xpath of the element
        xpath6: str
            The xpath of the element
        xpath7: str
            The xpath of the element
        xpath8: str
            The xpath of the element
        xpath9: str
            The xpath of the element
        xpath10: str
            The xpath of the element
        xpath11: str
            The xpath of the element
        xpath12: str
            The xpath of the element
        xpath13: str
            The xpath of the element
        xpath14: str
            The xpath of the element
        '''
        for i in range(11):
            data = {"Name": [],"Key": [],"Bell_size": [],"Pistons": [],"Bore": [],"Water_key": [],"Body": [],"Lyre_box": [],"Mouth_piece": [],"Warranty": [],"Price": []}
            container = self.driver.find_element_by_xpath('//div[@class="row prod_wrapper"]')
            trumpet = container.find_elements_by_xpath('./div')[i]
            trumpet.click()
            time.sleep(5)
            try:
                Name = self.driver.find_element_by_xpath(xpath4).text
                data['Name'].append(Name)
            except NoSuchElementException:
                data['Name'].append(None)  
            try:
                Key = self.driver.find_element_by_xpath(xpath5).text
                data['Key'].append(Key)
            except NoSuchElementException:
                data['Key'].append(None)
            try:
                Bell_size = self.driver.find_element_by_xpath(xpath6).text
                data['Bell_size'].append(Bell_size)
            except NoSuchElementException:
                data['Bell_size'].append(None)
            try:
                Pistons = self.driver.find_element_by_xpath(xpath7).text
                data['Pistons'].append(Pistons)
            except NoSuchElementException:
                data['Pistons'].append(None)
            try:
                Bore = self.driver.find_element_by_xpath(xpath8).text
                data['Bore'].append(Bore)
            except NoSuchElementException:
                data['Bore'].append(None)
            try:
                Water_key = self.driver.find_element_by_xpath(xpath9).text
                data['Water_key'].append(Water_key)
            except NoSuchElementException:
                data['Water_key'].append(None)
            try:
                Body = self.driver.find_element_by_xpath(xpath10).text
                data['Body'].append(Body)
            except NoSuchElementException:
                data['Body'].append(None)
            try:
                Lyre_box = self.driver.find_element_by_xpath(xpath11).text
                data['Lyre_box'].append(Lyre_box)
            except NoSuchElementException:
                data['Lyre_box'].append(None)
            try:
                Mouth_piece = self.driver.find_element_by_xpath(xpath12).text
                data['Mouth_piece'].append(Mouth_piece)
            except NoSuchElementException:
                data['Mouth_piece'].append(None)
            try:
                Warranty = self.driver.find_element_by_xpath(xpath13).text
                data['Warranty'].append(Warranty)
            except NoSuchElementException:
                data['Warranty'].append(None)
            try:
                Price = self.driver.find_element_by_xpath(xpath14).text
                data['Price'].append(Price)
            except NoSuchElementException:
                data['Price'].append(None)
            self.driver.back()
            time.sleep(2)
            df = pd.DataFrame(data)

class ScraperTrumpet(Scraper):
    '''
    Scraper that srapes specifications of trumpets from John Packer website
    Parameters
    ------------------------------------
    data_dict
        Contains UUID, Name, Key, Bell_size, Pistons, Bore, Water_key, Body, Lyre_box, Mouth_piece, Warranty, Price
    '''
    def __init__(self, instrument):
        super().__init__('https://www.johnpacker.co.uk')
        self.instrument = instrument

    def scrape_trumpets(self):
        self.accept_cookies(xpath='/html/body/div[1]/div[7]/div/div[3]/a')
        self.search(xpath2='//*[@id="header_search_search_for"]')
        self.find_container(xpath3='//div[@class="row prod_wrapper"]')
        self.pull_data(xpath4='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[1]', xpath5='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[2]', xpath6='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[3]', xpath7='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[4]', xpath8='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[5]s', xpath9='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[6]', xpath10='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[7]', xpath11='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[9]', xpath12='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[10]', xpath13='//*[@id="prod_det_get_body"]/section/div[2]/span/ul/li[11]', xpath14='//*[@id="price_details"]/div/p/span[2]')

if __name__ == '__main__':
    bot = ScraperTrumpet('Trumpet')
    bot.scrape_trumpets()
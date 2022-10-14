#importing modules
from lib2to3.pgen2 import driver
from time import sleep
from xxlimited import Str
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from typing import bool 




class WebDriver():
    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--no-sandbox")
        self.ua = UserAgent(use_cache_server=False, verify_ssl=False)
        self.chrome_options.add_argument(f'user-agent={self.ua.chrome}')
        
    def get_driver(self) -> webdriver:
        self.chrome_options.headless = True
        return webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
    
    def get_driver_headless(self) -> webdriver:
        self.chrome_options.headless = False
        return webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
    
    def get_page(self, driver, page:str, xPATH_element_to_wait:str="", timeout:int=10) -> bool:
        """
        Methods gets page and checks if page is loaded by checking visibility of element with xPATH provided or it just waits for 10 seconds
        returns True if page is loaded and False if page is not loaded
        """
        driver.get(page)
        wait = WebDriverWait(driver, timeout)
        try:
            if xPATH_element_to_wait:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xPATH_element_to_wait)))
                return True
            else:
                sleep(timeout)
                return True
        except Exception as e:
            return False
            
    
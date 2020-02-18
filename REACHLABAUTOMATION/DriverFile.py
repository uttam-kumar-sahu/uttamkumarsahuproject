from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from UserData import Data
from Library.FunctionLibrary import Utilities
import time


class Driver:

    """
    Creates Driver instance
    """

    def __init__(self):
        try:
            self.instance=webdriver.Chrome(executable_path="D:/AllAutomationSetup/BrowsersDrivers/chromedriver.exe")
            logging.info("Browser instance created succesfully")
            self.instance.maximize_window()
        except Exception as e:
            logging.info("Error while creating browser instance")
            raise e

    """
    Navigate to the URL
    """

    def navigate(self,url,pg_title):
        try:
            self.instance.get(url)
            logging.info("Navigating to the url...")
            assert pg_title in self.instance.title,"Unable to navigate to the  page"
        except Exception as e:
            logging.info("Error came while navigating to the url")
            raise e
    
    """
    Login to the BrandsReach application
    """
            
    def login_to_brand(self):
        
        self.driver=self.instance
        
        logging.info("Logging in to Brand Dashboard")
        webUtil = Utilities(self.driver)
        
        webUtil.clear_and_input(By.XPATH,"//input[@placeholder='Email']",Data.username,"username field")
        webUtil.clear_and_input(By.XPATH,"//input[@placeholder='Password']",Data.password,"password field")
        webUtil.click_on_element(By.XPATH,"//button[contains(text(),'Login')]","login button")
        #To check whether password or user name valid or not 
        try:
            Message=webUtil.locate(By.XPATH,"//span[contains(text(),'Please check your email for a 6-digit code')]","Message of the Verification page")
            assert "email" in Message.text
        except Exception as e:
            logging.info("Invalid Password or username ")
            raise e

        #OTP verification
        webUtil.clear_and_input(By.XPATH,"//input[@name='otp']",Data.OTP,"OTP")
        webUtil.click_on_element(By.XPATH,"//button[contains(text(),'Verify')]","Verify button")
        
        #Validate the profile open or  not
        try:
            Heading=webUtil.locate(By.XPATH,"//h1[@class='heading']","Heading of the profile page")
            assert "Dashboard" in Heading.text
        except Exception as e:
            logging.info("Unable to open profile")
            raise e
        

        logging.info("I am in Dashboard")

    """
    logging out of the Brands Reach  app
    """

    def logout_from_brand(self):

        self.driver=self.instance
        logging.info("Logging out of the  Brand Dashboard")
        webUtil = Utilities(self.driver)
        webUtil.click_on_element(By.XPATH,"//i[@class='fas fa-angle-down']","Drop down button")
        webUtil.click_on_element(By.XPATH,"//div[contains(text(),'Log Out')]","Logout button")
        


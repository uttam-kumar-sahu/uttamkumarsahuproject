from selenium import webdriver
import logging
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Utilities:
    
    driver=None
    def __init__(self,driver):
        self.driver=driver


    """
    Finds an web Element
    """
    def locate(self,locator,locator_value,elem_name = "Web Element"):
        try:
            element = WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((locator,locator_value))
            )
            #self.mouse_hover(element,elem_name)
            # logging.info("Located the element:" + elem_name)
            return element
        except Exception as e:
            logging.debug("Unable to locate the element:" + elem_name)
            logging.debug("Error came while locating thhe element ")
            raise e
    
    """
    Locate the web element and click on it 
    """
    def click_on_element(self,locator,locator_value,elem_name = "Web Element"):
        try:
            element = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((locator,locator_value))
            )
            #self.mouse_hover(element,elem_name)
            self.driver.execute_script("arguments[0].click();", element)
            logging.info("Clicked on:" + elem_name)
        except Exception as e:
            logging.info("Unable to perform click action on:" + elem_name)
            raise e

    """
    Locate the feild,clears it and input keys to it
    """
    def clear_and_input(self,locator,locator_value,user_input,elem_name = "Web Element"):
        try:
            element = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((locator,locator_value))
            )
            #self.mouse_hover(element,elem_name)
            #element.clear()
            element.send_keys(user_input)
            logging.info("{} inputted succesfully".format(elem_name))
        except Exception as e:
            logging.info("Unable to input {}".format(elem_name))
            raise e

    """
    Locate the element and mouse hover to it 
    """
    def mouse_hover(self,element,elemname="Web Element in mouse hover"):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except Exception as e:
            logging.info("Unable to mouse hover to:" + elemname)
            raise e

    """
    Locate a drop down and select the dropdown by Visible text
    """
    def drop_down_select(self,locator,locator_value_dropdown,value,elem_name="Drop Down element"):
        try:
            element=self.locate(locator,locator_value_dropdown)
            #self.mouse_hover(element,elem_name)
            select = Select(element)
            self.scroll_page(1000)
            self.driver.implicitly_wait(10)
            select.select_by_visible_text(value)
        except Exception as e:
            logging.info("Unable to select visible element:" + value)
            raise e

    """
    Scrolls a web page
    """
    def scroll_page(self,Y):
        try:
            self.driver.execute_script("window.scrollTo(arguments[0], 1000)",Y)
        except Exception as e:
            logging.info("Error came while scrolling the web page")
            raise e

    # """
    # Sends Enter Key
    # """
    # def send_ENTER_key(self,locator,locator_value,elem_name='Web Element'):
    #     try:
    #         self.locate(locator,locator_value).send_keys(Keys.ENTER)
    #     except Exception as e:
    #         logging.info("Unable to send Enter key")
    #         raise e
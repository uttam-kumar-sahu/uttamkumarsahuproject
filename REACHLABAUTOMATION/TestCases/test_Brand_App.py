import pytest
from UserData import Data
from PageObjects.dashboard import App_Dashboard
import logging
from selenium import webdriver
from DriverFile import Driver

"""
Testing the Brand site
"""

@pytest.mark.usefixtures('test_set_up_tear_down')
class TestBrandApp:
    driver=None

    #Adding logs of the test

    logging.basicConfig(level=logging.INFO,filename=Data.logging_path)
    handler=logging.FileHandler(Data.logging_path,mode='w')
    logging.getLogger().addHandler(logging.StreamHandler())
    
    """
    TestCase 1:Creating new brand,new Campaign,new activation and validating them
               Inviting Creators for the campaign
               Uploading media files for the activation
               Matching the uploaded media  
    """
    def test_brand(self):
        activity=App_Dashboard(self.driver)
        # logging.info("Creating new Brand")
        # activity.create_brands()
        # logging.info("Creating new Campaign")
        # activity.create_campaign()
        # logging.info("Creating New activation")
        # activity.create_activation()
        # logging.info("Inviting creator for the campaign")
        # activity.invite_creators()
        # logging.info("Uploading Media")
        # activity.upload_media()
        logging.info("Matching uploaded media")
        activity.media_match()

    def test_case_2(self):
        print("I am in test case no-2")
        logging.info("I am able to execute test case 2")        
       
        


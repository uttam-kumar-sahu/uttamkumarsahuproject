from selenium import webdriver
from selenium.webdriver.common.by import By
from UserData import Data
import logging
from Library.FunctionLibrary import Utilities
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
from selenium.webdriver.common.keys import Keys

"""
Page Object for the Dashboard page
"""
class App_Dashboard:

    def __init__(self,driver):
        self.driver=driver
    
    """
    Creates a new brand and validate it in the Brand page
    """ 

    def create_brands(self):
        webUtilities = Utilities(self.driver.instance)
        
        webUtilities.click_on_element(By.XPATH,"//img[@class='action-menu-icon']","Menu button")
        webUtilities.click_on_element(By.XPATH,"//li[contains(text(),'New Brand')]","New Brand button")

        #Fills up the new brand creation page
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Enter Name']",Data.BrandName,"New Brand Name")
        webUtilities.clear_and_input(By.XPATH,"//input[@type='file']",Data.BrandImage_Path,"Brand Image ")
        webUtilities.click_on_element(By.XPATH,"//button[@type='submit']","Create Brand button")
        element = WebDriverWait(self.driver.instance, 100).until(
            EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Brand Created')]"))
            )
        self.driver.instance.switch_to_default_content()
        
        #Validate whether brand is created or not and also print the Brand Name

        webUtilities.click_on_element(By.XPATH,"//a[@title='Brands']","Brands icon")
        BrandElem=webUtilities.locate(By.XPATH,"//a[1]//figure[1]//header[1]//div[1]//div[1]//h4[1]","Brand details")
        Brandnm=BrandElem.text

        try:
            assert Data.BrandName in Brandnm
            print("New brand is created")
            logging.info("Name of new Brand created is:" + Brandnm)
            print("Brand name is:" + Brandnm)
        except Exception as e:
            logging.info("Unable to create new brand")
            raise e
        

    """
    Create a new Campaign and validate it
    """
     
    def create_campaign(self):
        webUtilities = Utilities(self.driver.instance)

        webUtilities.click_on_element(By.XPATH,"//img[@class='action-menu-icon']","Menu button")
        webUtilities.click_on_element(By.XPATH,"//li[contains(text(),'New Campaign')]","New Campaign button")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Campaign Name']",Data.Campaign_Name,"New Campaign Name")
        webUtilities.drop_down_select(By.XPATH,"//select[@name='brand_id']",Data.CampBrand,"Brand selection")
        webUtilities.drop_down_select(By.XPATH,"//select[@name='agency_id']",Data.Agency,"Agency selection")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Enter an Impression']",Data.Impression,"Impressions ")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Enter Insertion Order']",Data.Insertion_Order,"Insertion Order ")
        webUtilities.clear_and_input(By.XPATH,"//input[@name='image_file']",Data.Campaign_Image,"Campaign image")

        #scroll
        webUtilities.scroll_page(1000)
        webUtilities.click_on_element(By.XPATH,"//button[contains(text(),'create campaign')]","Create Campaign button")
        
        #wait for Campaign creation
        element = WebDriverWait(self.driver.instance, 100).until(
            EC.presence_of_element_located((By.XPATH,"//h1[text()='{}']".format(Data.Campaign_Name)))
            )

        #validate Campaign created or not 
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[3]","Campaign icon")
        CampElem=webUtilities.locate(By.XPATH,"//a[1]//figure[1]//header[1]//div[1]//div[1]/child::h4","Campaign details")
        Campnm=CampElem.text
        try:
            assert Data.Campaign_Name in Campnm
            print("New Campaign is created")
            logging.info("Name of new Campaign created is:" + Campnm)
            print("Campaign name is:" + Campnm)
        except Exception as e:
            logging.info("Unable to create new campaign")
            raise e

    """
    Create new activation and validate it
    """

    def create_activation(self):
        webUtilities = Utilities(self.driver.instance)

        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[3]","Campaign icon")
        webUtilities.click_on_element(By.XPATH,"//h4[contains(text(),{})]".format(Data.ActCampaign_Name),"Campaign")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Create Activation')]","Create Activation")
        
        #Activation Creation form page 1
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Activation Name']",Data.Activation_name,"New Activation Name")
        webUtilities.drop_down_select(By.XPATH,"//select[@name='sub_campaign.campaign_type']",Data.Activation_type,"Activation type")
        webUtilities.drop_down_select(By.XPATH,"//select[@name='sub_campaign.media_type']",Data.Media_type,"Media type")
        webUtilities.clear_and_input(By.XPATH,"//input[@name='sub_campaign.image']",Data.Activation_Image,"Activation image")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Choose a Start Date']",Data.start_date,"Start Date")
        webUtilities.scroll_page(1000)
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Choose an End Date']",Data.end_date,"End Date")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Next Step')]","Next step button1")

        #Activation Creation form page 2
        webUtilities.clear_and_input(By.XPATH,"//textarea[@placeholder='Sample Media Caption']",Data.SampleCaptions,"Sample captions")
        webUtilities.click_on_element(By.XPATH,"//button[@type='submit']","Next step button2")

        #Activation Creation form page 3
        webUtilities.clear_and_input(By.XPATH,"//textarea[@placeholder='Campaign Directions']",Data.Campaign_Directions,"Campaign Directions")
        webUtilities.clear_and_input(By.XPATH,"//textarea[@placeholder='Caption Directions']",Data.Caption_Directions,"Caption Directions")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Finish')]","Finish button")
        
        self.driver.instance.implicitly_wait(20)

        #switching to the current window and testing whether in right page or not
        current_window = self.driver.instance.window_handles[0]
        self.driver.instance.switch_to.window(current_window) 
        webUtilities.click_on_element(By.XPATH,"//div[@title='Show as List']","test_the_page")

        #Validating the activation created or not
        element1 = WebDriverWait(self.driver.instance, 100).until(
            EC.presence_of_element_located((By.XPATH,"//h1[text()='{}']".format(Data.Activation_name)))
            )
        time.sleep(5)
        Actname=element1.text
        try:
            assert Data.Activation_name.upper() in Actname.upper()
            print("New Activation is created")
            logging.info("Name of new activation created is:" + Actname)
            print("Activation name is:" + Actname)
        except Exception as e:
            logging.info("Unable to create new Activation")
            raise e


    """
    Creator Invitation and approval
    """
    def invite_creators(self):
        webUtilities = Utilities(self.driver.instance)
        
        #Adding Creators to the campaign
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[3]","Campaign icon")
        webUtilities.click_on_element(By.XPATH,"//span[@class='submit-button search-button-active']","Search Campaign button")
        webUtilities.clear_and_input(By.XPATH,"//input[@name='search']",Data.Campaign,"Search campaign feild")
        webUtilities.click_on_element(By.XPATH,"//h4[text()='{}']".format(Data.Campaign),"Campaign")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Creators')]","Creator button inside Campaign")
        webUtilities.click_on_element(By.XPATH,"//div[@title='Add Creator']","Add creator")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Search']",Data.Creator_name,"Search Creator")
        time.sleep(3.0)
        try:
            element1 = WebDriverWait(self.driver.instance, 100).until(
            EC.presence_of_element_located((By.XPATH,"//span[text()='{}']".format(Data.Creator_name)))
            )
        except Exception as e:
            logging.info("Desired creator not found")
            raise e
        
        webUtilities.click_on_element(By.XPATH,"//span[text()='{}']".format(Data.Creator_name),"detect creator")
        webUtilities.click_on_element(By.XPATH,"//input[@value='2459']","Check Creator Checkbox")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Add to campaign')]","Add to Campaign button")
        time.sleep(3.0)
        self.driver.instance.switch_to_default_content()

        #Approving creator in campaign
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'for review')]","for review button")
        webUtilities.click_on_element(By.XPATH,"(//input[@type='checkbox'])[3]","checking creator")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Actions')]","Action on creator in campaign")
        webUtilities.click_on_element(By.XPATH,"//div[contains(text(),'{}')]".format(Data.Actioncamp),"Type of ")
        
        #Validating creator is approved or not
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'approved')]","Approved button")
        try:
            element1 = WebDriverWait(self.driver.instance, 100).until(
                EC.presence_of_element_located((By.XPATH,"//a[text()='{}']".format(Data.Creator_name)))
                )
        except Exception as e:
            logging.info("Unable to Approve the creator")
            raise e
        
        #Inviting Creators
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Activations')]","Activations tab")
        webUtilities.click_on_element(By.XPATH,"//h4[text()='{}']".format(Data.Activation),"Activation")
        webUtilities.click_on_element(By.XPATH,"//i[@class='fa fa-search']","Activation page creator search button")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Search']",Data.Creator_name,"Search Creator in activation page")
        webUtilities.click_on_element(By.XPATH,"(//input[@type='checkbox'])[2]","Check Creator Checkbox for invitation")
        time.sleep(3.0)
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Actions')]","Action on creator in activation")
        webUtilities.click_on_element(By.XPATH,"//div[text()='{}']".format(Data.Actionact),"type of Action on creator in activation")
        
        #Filling up invitation form
        webUtilities.drop_down_select(By.XPATH,"//select[@name='platform']",Data.Creator_account_type,"select creator account type")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Number of posts']",Data.no_of_posts,"No. of post")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Offer amount']",Data.offer_amount,"Offer Amount")
        webUtilities.click_on_element(By.XPATH,"//span[@class='submit-button search-button-active']","Search creator social media creator account")
        webUtilities.clear_and_input(By.XPATH,"//input[@name='search']",Data.Creator_name,"Creator social account info")
        webUtilities.click_on_element(By.XPATH,"//input[@value='6176']","Check checkbox of creator account")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Invite')]","Invite Button")
        
        #Validating Creator is invited or not 
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'invited')]","Invited button")
        try:
            element2 = WebDriverWait(self.driver.instance, 100).until(
                EC.presence_of_element_located((By.XPATH,"//a[text()='{}']".format(Data.Creator_actual_name)))
                )
            
            logging.info("Creator invited succesfully")
        except Exception as e:
            logging.info("Unable to Invitethe creator")
            raise e


    """
    Upload Media files
    """
    def upload_media(self):
        webUtilities = Utilities(self.driver.instance)
        
        
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[3]","Campaign icon")
        webUtilities.click_on_element(By.XPATH,"//span[@class='submit-button search-button-active']","Search Campaign button")
        webUtilities.clear_and_input(By.XPATH,"//input[@name='search']",Data.Campaign_info,"Search campaign feild")
        webUtilities.click_on_element(By.XPATH,"//h4[text()='{}']".format(Data.Campaign_info),"Campaign")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Activations')]","Activations tab")
        webUtilities.click_on_element(By.XPATH,"//h4[text()='{}']".format(Data.Activation_info),"Activation")
        webUtilities.click_on_element(By.XPATH,"//button[text()='Submit Media']","Submit media button")
        webUtilities.clear_and_input(By.XPATH,"//input[@placeholder='Search for Creator Account']",Data.Creator_account_name,"Search user name")
        time.sleep(3.0)
        webUtilities.click_on_element(By.XPATH,"//div[@class='username']","Select media upload social account")
        
        
        webUtilities.click_on_element(By.XPATH,"//span[text()='Add Media']","Upload media")
        subprocess.call('"C:/Users/uttams/Desktop/Script.exe"')
        webUtilities.clear_and_input(By.XPATH,"//input[@name='offer_price']",Data.Offer_Amount,"Offer amount")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'UPLOAD CONTENT')]","Upload Media button")
        time.sleep(5.0)
        self.driver.instance.switch_to_default_content()
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[5]","Media page button")
        
        #validation of Media upload
        try:
            element2 = WebDriverWait(self.driver.instance, 100).until(
                EC.presence_of_element_located((By.XPATH,"//a[text()='{}']".format(Data.Creator_actual_name)))
                )
            print(element2.text)
            logging.info("Media uploaded")
        except Exception as e:
            logging.info("Unable to Upload media")
            raise e
 




    
    """
    Media Match
    """
    def media_match(self):
        webUtilities = Utilities(self.driver.instance)
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[5]","Media page icon")
        
        webUtilities.click_on_element(By.XPATH,"(//span[text()='{}'])[1]".format(Data.creator_name_in_media),"Media")
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Media match')]","Media Match button")
        webUtilities.click_on_element(By.XPATH,"//tr[1]//td[1]//input[1]","Media URl")
        webUtilities.scroll_page(1000)
        webUtilities.click_on_element(By.XPATH,"//span[contains(text(),'Submit')]","Submit Button")
        time.sleep(5.0)

        #Validate Media status is "Posted" or not
        webUtilities.click_on_element(By.XPATH,"//div[@class='menu']/child::a[5]","Media page icon")
        time.sleep(3.0)
        webUtilities.click_on_element(By.XPATH,"(//span[text()='{}'])[1]".format(Data.creator_name_in_media),"Media")
        try:
            element2 = WebDriverWait(self.driver.instance, 100).until(
                EC.presence_of_element_located((By.XPATH,"(//span[text()='Posted'])[1]"))
                )
            logging.info("Media Matched")
        except Exception as e:
            logging.info("Unable to Match media")
            raise e





   

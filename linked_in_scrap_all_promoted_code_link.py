import re
from selenium import webdriver
import selenium
import time
from urllib.parse import urlparse
import requests,json
from datetime import date
from pathlib import Path
import logging
from selenium.webdriver.chrome.options import Options,DesiredCapabilities
from google_trans_new import google_translator
# import google_translator
from logging.handlers import TimedRotatingFileHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing_logging import install_mp_handler
from threading import Thread
from multiprocessing import Pool
import json
import pandas as pd
import win32clipboard
from selenium.webdriver.common.keys import Keys
import  pyperclip as pc
from random import randint
import datetime
from time import sleep
from requests import get
from bs4 import BeautifulSoup as bs
from numpy import random
import pyperclip

  
"""========================================initialize====================================="""            
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.19 Safari/537.36'
opt = webdriver.ChromeOptions()


prefs = {   "profile.default_content_settings.cookies": 2,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "download.default_directory": "NUL",
            "download.prompt_for_download": False,
            "translate_whitelists": {"fr":"en","nl":"en","ro":"en","cs":"en","pt":"en","el":"en","bg":"en","da":"en","de":"en","th":"en","hr":"en","it":"en"},
            "translate":{"enabled":"True"}
        }

opt.add_experimental_option("prefs", prefs)
opt.add_argument(f'user-agent={user_agent}')
opt.add_argument("start-maximized")
opt.add_argument("--disable-notifications")
caps = DesiredCapabilities.CHROME
driver = webdriver.Chrome(ChromeDriverManager(version="91.0.4472.19").install() , options=opt, desired_capabilities=caps)
driver.get("https://ipapi.co/json/")
text = driver.find_element_by_tag_name("pre").text
new_dict = json.loads(text)
ip_dict = {'ipAddress': new_dict['ip'], 'countryName': new_dict['country_name'],
           'stateProv': new_dict['region'], 'city': new_dict['city']}
sleep(randint(10,15))
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

"""============================================initialize end=================================="""

"""============================================start login====================================="""
try:
    
    #Enter login info:
    elementID = driver.find_element_by_id('username')
    elementID.send_keys("eugeniakassulke@zohomail.com")
    sleep(randint(1,3))
    elementID = driver.find_element_by_id('password')
    elementID.send_keys("jqMggFTveAsM")
    #Note: replace the keys "username" and "password" with your LinkedIn login info
    elementID.submit()
    sleep(randint(4,7))
    #driver.findElement(By.xpath('//*[@id="remember-me-prompt__form-primary"]/button')).click()
    #btn__primary--large
    driver.find_element_by_class_name("btn__primary--large").click()# click on see new post upon reaching end of feeds
    #https://www.linkedin.com/feed/  
except:
    pass

"""=====================================login end===================================="""


"""==================================copy link code start=================================="""
while 1:

    """=============================scroll tab========================================"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    new_height=0
    while 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if(new_height!=last_height):
            last_height=new_height
        else:
            break
    """=============================scroll end========================================="""

    """=============================copy link to post================================="""
    element=driver.find_elements_by_class_name('relative')

    time.sleep(1)
    for el in element:
        if('Promoted' in el.text):
            try:
                el.find_element_by_class_name('feed-shared-control-menu__trigger').click()
                time.sleep(1)
                el.find_element_by_css_selector('li.feed-shared-control-menu__item.option-share-via').click()
                print(pyperclip.paste(),'\n')
                driver.find_element_by_css_selector('button.artdeco-toast-item__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view').click()

            except:
                pass
    time.sleep(1)
    driver.refresh()
    """==========================copy link to post end===================================="""

"""==============================copy code end============================================"""
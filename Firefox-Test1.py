from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import csv
import os
import subprocess


def firefoxFunc():
	binary = FirefoxBinary('/home/user1/Desktop/Firefox/firefox-59.0/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)

	url_list=['http://www.cbtcafe.com/','https://www.cisco.com/','http://www.foxnews.com/']
	
	
	browser.get('https://www.cisco.com/')
	print("=====%s seconds  =====Tab"+ "  "+repr(diff_time))
	browser.quit()




firefoxFunc()
'''
sudo rm -rf /usr/bin/geckodriver
cd

 sudo mv /home/user1/Desktop/Firefox/19.0/geckodriver  /usr/bin
'''
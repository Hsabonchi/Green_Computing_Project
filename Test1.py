import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



 
start_time=time.time()

# The fullpath to the firefox-bin  file location (point to )
binary = FirefoxBinary('/home/user1/Desktop/Firefox/firefox-53.0.3/firefox-bin')
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

#/home/user1/Desktop/Firefox/firefox_58.0b14/firefox-bin'
#/home/user1/Desktop/Firefox/firefox-53.0/firefox-bin
#/home/user1/Desktop/Firefox/firefox_6.0/firefox-bin


#Change the path to the compatible  geckodriver Version and leave it blank for newest version
#fp = webdriver.FirefoxProfile('/home/user1/Desktop/Firefox/v0.19.0)

#browser = webdriver.Firefox(firefox_binary=binary,executable_path ='/home/user1/Desktop/Firefox/21.0')

browser = webdriver.Firefox(firefox_binary=binary)


#firefox_profile='/home/user1/Desktop/Firefox/19.0'

#start!!!!!!!!!!!!!!!! runTest(browser)

# google search Gify and click 
browser.get('https://www.google.com/search?client=ubuntu&hs=rM7&channel=fs&ei=jCctW9CgCdLGsQXpgoKYBQ&q=Get+the+best+GIF+on+GIPHY&oq=Get+the+best+GIF+on+GIPHY&gs_l=psy-ab.3...9095.9595.0.10261.1.1.0.0.0.0.56.56.1.1.0....0...1c.1.64.psy-ab..0.0.0....0.z-2BDRAHuEs')




# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle



#find the link that has the below text and click in search

elem=browser.find_element_by_link_text('The best GIFs - Get the best GIF on GIPHY')

start_time=time.time()
elem.click()
print("Tab1 =====  %s seconds  ===== click the link from search result "%(time.time()-start_time) )



# Put focus on current window which will, in fact, put focus on the current visible tab
browser.switch_to_window(main_window)


sleep(2)
start_time=time.time()
#Click the Reactions Text link on this site
elem=browser.find_element_by_link_text('Reactions')
elem.click()

#print("Tab2 =====   %s seconds  =====click the Reactions on the same page  "%(time.time()-start_time) )


start_time=time.time()
#Open the link #giphy.com/reactions and open in new tap
browser.execute_script("window.open('https://giphy.com/reactions');")
sleep(5)
elem1=browser.find_element_by_link_text('Sports')
elem1.click()
print("Tab3 ===== %s seconds  ===== go to Reactions & click sports "%(time.time()-start_time) )


start_time=time.time()
browser.execute_script("window.open('https://nsf.gov/awardsearch/showAward?AWD_ID=1118043&HistoricalAwards=false');")

print("Tab4 ===== %s seconds  =====NSF "%(time.time()-start_time) )


browser.switch_to_window(browser.window_handles[1])
#sleep(4)
#searchbar=browser.find_element_by_id('QueryText1')
#searchbar.send_keys('REU')
#searchbar.send_keys(Keys.ENTER)


for x in range (3):

    start_time=time.time()
    browser.execute_script("window.open('https://www.youtube.com/watch?v=JZUX3n2yAzY');")
 
    print("=====%s seconds  =====Tab"+repr(x+5)+ "  "+repr((time.time()-start_time)))
    print(time.time()-start_time)


#end!!!!!!!!!!!!!!!! runTest(browser)


#main
#browser = chrome v1;
# runTest(browser)
#browser = chrome v2;
# runTest(browser)
#browser = firefox v1;
# runTest(browser)











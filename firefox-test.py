import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import requests
import os
import subprocess
import time
from pathlib import Path

WEB_BROWSER_TYPE = 'FF'
ListOfLoadTme=[]
'''
VERSIONS_LIST_1=['firefox-61.0','firefox-60.0.2','firefox-60.0.1','firefox-60.0','firefox-59.0.3','firefox-59.0.2','firefox-59.0.1','firefox-59.0', 'firefox-58.0.2','firefox-58.0.1','firefox-58.0','firefox-57.0.3','firefox-57.0.2','firefox-57.0.1']	
VERSIONS_LIST_2 = ['firefox-56.0.2' ,'firefox-56.0.1','firefox-56.0','firefox-55.0.2' ,'firefox-55.0.1','firefox-55.0','firefox-54.0.1','firefox-54.0']
VERSIONS_LIST_3 = ['firefox-53.0.3','firefox-53.0.2 ','firefox-53.0 ','firefox-52.0.2','firefox-52.0.1','firefox-52.0','firefox-51.0.1','firefox-51.0 ','firefox-50.0.2','firefox-50.0.1','firefox-50.0','firefox-49.0.2','firefox-49.0.1','firefox-49.0','firefox-48.0.2',
'firefox-48.0.1','firefox-48.0','firefox-47.2','firefox-47.1','firefox-47.0','firefox-46.0.1','firefox-46.0','firefox-45.0.2','firefox-45.0.1','firefox-45.0']	
'firefox-45.0.csv','firefox-45.0.1.csv','firefox-45.0.2.csv','firefox-46.0.csv','
'''

 
VERSIONS_LIST_1=['firefox-45.0','firefox-45.0.1','firefox-45.0.2','firefox-46.0','firefox-46.0.1','firefox-47.0','firefox-47.1','firefox-47.2','firefox-48.0','firefox-48.0.1','firefox-48.0.2','firefox-49.0','firefox-49.0.1','firefox-49.0.2','firefox-50.0','firefox-50.0.1','firefox-50.0.2','firefox-51.0','firefox-51.0.1','firefox-52.0','firefox-52.0.1','firefox-52.0.2','firefox-53.0','firefox-53.0.2','firefox-53.0.3']
VERSIONS_LIST_2=['firefox-54.0','firefox-54.0.1','firefox-55.0','firefox-55.0.1','firefox-55.0.2','firefox-56.0','firefox-56.0.1','firefox-56.0.2']

VERSIONS_LIST_3 =['firefox-57.0.1','firefox-57.0.2','firefox-57.0.3','firefox-58.0','firefox-58.0.1','firefox-58.0.2','firefox-59.0','firefox-59.0.1' ,'firefox-59.0.2','firefox-59.0.3','firefox-60.0','firefox-60.0.1','firefox-60.0.2','firefox-61.0']

run_times1=[]
run_times2=[]
def run_giphy_reactions_test(version_folder_path):
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)

	print(version_folder_path)
	#print('Im in run_giphy_reactions_test')
	start_time=time.time()
		#Open the link #giphy.com/reactions and open in new tap
	browser.execute_script("window.open('https://giphy.com/reactions');")
		#sleep(5)
	#elem1=browser.find_element_by_link_text('Sports')
	#elem1.click()
	end_time = time.time()	
	diff_time = end_time - start_time
	#time.sleep(2)
	browser.quit()
	return diff_time

def run_generic_web_test_with_cache(version_folder_path, url):

	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)
	
	print(f'{version_folder_path}')

	print('Opening url uncached...')
	
	browser.get( f"{url}")
	
	print('Opening url cached...')
	
	start_time = time.time()

	browser.get('http://www.foxnews.com/')
	browser.get('https://www.cnn.com/')
	browser.get('https://giphy.com/')
	browser.get('https://www.nsf.gov/')
	
	browser.get( f"{url}")
	end_time = time.time()	
	
	diff_time = end_time - start_time
	browser.quit()


	return diff_time
	

def run_generic_web_test(version_folder_path, url):
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)
	print('version_folder_path')

	start_time = time.time()
	browser.get( f"{url}")	
	end_time = time.time()	
	diff_time = end_time - start_time
	browser.quit()

	return diff_time


	def run_flash_web_test(version_folder_path, url):
		binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
		browser = webdriver.Firefox(firefox_binary=binary)
		print('Im in run_flash_web_test')

		print('Opening url uncached...')
		browser.get( f"{url}")



		print('Opening url cached...')
		start_time = time.time()
		browser.set_page_load_timeout(3000000)
		browser.get( f"{url}")	
		
		end_time = time.time()	
		diff_time = end_time - start_time
		browser.quit()

	return diff_time



def make_output_file_name(url):
	return url.replace('/', '').replacde('https:', '').replace('http:','').replace('.com', '')

#Static 
def run_all_tests(test_function, args = ()):
	test_count = 0
	run_times = []
	print('run_all_tests')

	
     # run group 1 tests
	subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	subprocess.call( "tar -xf /home/user1/Desktop/Firefox/15/15.tar.gz --directory /home/user1/Desktop/Firefox/15/",shell=True)
	subprocess.call( "sudo mv /home/user1/Desktop/Firefox/15/geckodriver  /usr/bin/",shell=True)	
	for version in VERSIONS_LIST_1:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		
		
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))





	# run group 3 tests
	subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	subprocess.call( "tar -xf /home/user1/Desktop/Firefox/19/19.tar.gz --directory /home/user1/Desktop/Firefox/19/",shell=True)
	subprocess.call( "sudo mv /home/user1/Desktop/Firefox/19/geckodriver  /usr/bin/",shell=True)
	for version in VERSIONS_LIST_2:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))




    # run group 1 tests
	subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	subprocess.call( "tar -xf /home/user1/Desktop/Firefox/21/21.tar.gz --directory /home/user1/Desktop/Firefox/21/",shell=True)
	subprocess.call( "sudo mv /home/user1/Desktop/Firefox/21/geckodriver  /usr/bin/",shell=True)
	for version in VERSIONS_LIST_3:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))
	

	return run_times

def create_csv(output_filename, run_times):
	
	if os.path.exists(output_filename + '.csv'):
		os.remove(output_filename + '.csv')
	with open(output_filename + '.csv', 'a') as csvfile:
		writer = csv.writer(csvfile,lineterminator= '\n')
		writer.writerow(VERSIONS_LIST_1 + VERSIONS_LIST_2 + VERSIONS_LIST_3)	
		writer.writerow(run_times)

#Static 
def create_plot_from_csv(csv_filename, output_filename, title, row = 1):
	y_axis_list = []
	
	with open(csv_filename + '.csv', 'r') as csvfile:
		reader = csv.reader(csvfile,lineterminator= '\n')
		y_axis_list = list(reader)[row]

	y_axis_list = list(map(float, y_axis_list))
	create_plot(output_filename, title, y_axis_list)
			
	
def create_plot(output_filename, title, run_times):
	plot_x_ticks=['45\n0.0 ','45\n.0.1 ','45\n.0.2 ','46\n0.0 ','46\n0.1 ','47\n0.0 ','47\n0.1 ','47\n2 ','48\n0.0 ','48\n0.1 ','48 \n0.2 ','49\n0.0 ','49\n0.1 ','49\n0.2 ','50\n0.0 ','50\n0.1 ','50\n0.2 ','51\n0.0 ','51\n0.1 ','52\n0.0 ','52\n0.1 ','52\n0.2 ','53\n0.0 ','53\n0.2 ','53\n0.3 ','54\n0.0 ','54\n0.1 ','55\n0.0 ','55\n0.1 ','55\n0.2 ','56\n0.0 ','56\n0.1 ','56\n0.2 ','57\n0.1 ','57\n0.2 ','57\n0.3 ','58\n0.0 ','58\n0.1 ','58\n0.2 ','59\n0.0 ','59\n0.1 ' ,'59\n0.2 ','59\n0.3 ','60\n0.0 ','60\n0.1 ','60\n0.2  ','61\n0.0 '] 	
	run_times = [round(i, 4) for i in run_times]


	font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'bold',
        'size': 16,
        }
	plt.figure(figsize=(15,10))
	plt.title(title)
	plt.xticks(list(range(0, len(plot_x_ticks))), plot_x_ticks, fontsize=7)
	plt.plot(list(range(0, len(plot_x_ticks))), run_times)

	if WEB_BROWSER_TYPE == 'FF':
		plt.xlabel('Firefox Version',fontdict=font)

	plt.ylabel('Time (s)',fontdict=font)
	#plt.show()
	plt.savefig(output_filename + '.png')

# Function that read a .csv file [21,39]==[runtimes(PLT),Releases]
#factor is number to filter out data
def read_plot_csv(csv_filename,factor,title,output_filename):
	
	y_axis_list = []
	list3=[]

	df = pd.read_csv( csv_filename,sep=',')
	# filter out data (high values)
	newdf=df[df.apply(lambda x:x< (factor*(df.stack().std())))]


	for x in range(47):
		#print("XXXX==================================>"+str(x))
		#Slice a column from data
		y=newdf.iloc[:,x:x+1]
		
		sum_ofcolumn=(y.mean())
			
		y_axis_list.append(sum_ofcolumn)

	print(len(y_axis_list))

	for list in y_axis_list:
			for number in list:
					list3.append(float(number))

	run_times = [round(i, 3) for i in list3]
	


	create_plot(output_filename, title,run_times)




#A function that plot 2 runtimes 		
def create_instead_plot(output_filename, title, run_times1,run_times2):
		plot_x_ticks =['61\n0.0','60\n 0.2','60\n0.1','60\n0.0','59\n0.3','59\n0.2','59\n0.1','59\n0.0', '58\n0.2','58\n0.1','58\n0.0','57\n 0.3','57\n0.2','57\n0.1','56\n0.2' ,'56\n0.1','56\n0.0','55\n0.2' ,'55\n0.1','55\n0.0','54\n0.1','54\n0.0','50\n0.2','50\n0.1','50\n0.0','49\n0.2','49\n0.1','49\n0.0','48\n0.2',
	'48\n0.1','48\n0.0','47\n0.2','47\n0.1','47\n0.0','46\n0.1','46\n0.0','45\n0.2','45\n0.1','45\n0.0']
 


		run_times1 = [round(i, 4) for i in run_times1]
		run_times2 = [round(i, 4) for i in run_times2]

		plt.figure(figsize=(20,10))
		plt.title(title)
		plt.xticks(list(range(0, len(plot_x_ticks))), plot_x_ticks, fontsize=11, rotation=20)

		plt.plot(list(range(0, len(plot_x_ticks))), run_times1,label='Giphy',color='green')
		plt.plot(list(range(0, len(plot_x_ticks))), run_times2,label='NSF',color='blue')

		plt.legend(loc=9,fontsize='x-large')

		if WEB_BROWSER_TYPE == 'FF':
			plt.xlabel('Firefox Version')

		plt.ylabel('Time (s)')
		#plt.show()
		plt.savefig(output_filename + '.png')



#A function that read_TWO_csv file.Its remove outlyeres
def read_two_csv(csv_filename):
	
		y_axis_list = []
		list3=[]

		df = pd.read_csv( csv_filename,sep=',')
		# filter out data (high values) 
		newdf=df[df.apply(lambda x:x< (9*(df.stack().std())))]


		for x in range(40):
			
			y=newdf.iloc[:,x:x+1]
			
			sum_ofcolumn=(y.mean())
				
			y_axis_list.append(sum_ofcolumn)

		print(len(y_axis_list))

		for list in y_axis_list:
				for number in list:
						list3.append(float(number))

		run_times = [round(i, 3) for i in list3]
		
		return run_times

def main():
	
	#read_plot_csv(csv_filename='/home/user1/Desktop/Poster/cisco-20.csv',title='',factor=10,output_filename='Cisco-4-run-test')

	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'https://nsf.gov/')
	create_csv('Games'+str(i), run_times_fox_news)
	'''
	'''
	run_times1=read_two_csv(csv_filename='/home/user1/Desktop/site-test-20/Giphy-20.csv')
	run_times2=read_two_csv(csv_filename='/home/user1/Desktop/site-test-20/NSF-2-run-20.csv')
	print(run_times1)
	print(run_times1)
	create_instead_plot(output_filename='comparing_NSF_Gify', title='Giphy_and_SLING',run_times1=run_times1,run_times2=run_times2)
	'''
	
	
	for i in range(0,18):

		
		run_times_fox_news = run_all_tests(run_generic_web_test_with_cache, 'https://www.cisco.com/')
		create_csv('/home/user1/Desktop/Poster/multi-url-Trail-4-run'+str(i), run_times_fox_news)
		time.sleep(20)
		

main()


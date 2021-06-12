from os import link
from sys import prefix
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas  as pd

#Create instance of Chrome Driver
chrome_drive_path = 'C:\Program Files (x86)\chromedriver.exe'
url = 'https://ec.europa.eu/eurostat/web/tourism/data/database'

#setting window size kai position & opening the website
driver = webdriver.Chrome(chrome_drive_path)
driver.set_window_size(1600,900, windowHandle='current')
driver.set_window_position(1920, 0, windowHandle='current')
driver.get(url)


#Find the first folder of the db, that I have to open, to reveal the files I need
first_fold = driver.find_element_by_class_name('title2')
first_fold.click()

#I need a helper (it is a footer logo), cause every time I open a page, there is text hiding the next link
helper = driver.find_element_by_id('footer_logos')
main_window = driver.current_window_handle

#Getting the link I want to open, it is the only link revealed with that class name
links = driver.find_elements_by_class_name('estat-icon-nui')

#opening the link except the last one, that I don't want
for idx, link in enumerate(links):
    helper.click()
    if link == links[4]:
        break
    else:
        link.click()
    driver.switch_to_window(str(main_window))

    print('Finished with the ' + str(idx+1) + ' click, it openned the ' + str(link) + ' element\n')

#I am getting the window handles for future reference and closing the first window as I don't need it from now on
windows = driver.window_handles
driver.close()

time.sleep(10)

driver.switch_to.window(str(windows[1]))

#take the greece info from the first webpage
gr_infos = driver.find_elements_by_css_selector('#ptRow11')
print('GR-INFO:\n')
for flag,gr_info in enumerate(gr_infos):
    print(str(gr_info.text))

#take the spain info from the first webpage
spain_infos = driver.find_elements_by_css_selector("#ptRow12")
print('\nSPAIN-INFO:\n')
for n, spain_info in enumerate(spain_infos):
    print(str(spain_info.text))

path = 'test.txt'
f = open(path, 'w')
with open('test.txt', 'w') as f:
    f.write('GR-INFO:\n' + str(gr_info.text) + '\n')
    f.write('\nSPAIN-INFO:\n' + str(spain_info.text) + '\n')
    
f.close()


#driver.switch_to_window(str(windows[2]))



#driver.switch_to_window(str(windows[3]))

#driver.switch_to_window(str(windows[4]))


#close the page after 10 seconds
time.sleep(10)
driver.quit()
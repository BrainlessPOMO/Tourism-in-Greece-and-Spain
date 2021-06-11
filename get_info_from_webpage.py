from sys import prefix
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pandas

#Create instance of Chrome Driver
chrome_drive_path = 'C:\Program Files (x86)\chromedriver.exe'
url = 'https://ec.europa.eu/eurostat/web/tourism/data/database'

#setting window size kai position & opening the website
driver = webdriver.Chrome(chrome_drive_path)
driver.set_window_size(900,900, windowHandle='current')
driver.set_window_position(1920, 0, windowHandle='current')
driver.get(url)
print(driver.title) #o titlos ths selidas

time.sleep(5)
print('5 seconds have just passed')

#Making the action Class that I am gonna use for mouse actions
actions = ActionChains(driver)

#Find the first folder of the db, that I have to open and open it
first_fold = driver.find_element_by_class_name('title2')
first_fold.click()

footer_logos = driver.find_element_by_id('footer_logos')
windows = [driver.current_window_handle]

elements = driver.find_elements_by_class_name('estat-icon-nui')
for idx, i in enumerate(elements):
    footer_logos.click()
    i.click()
    windows.append(driver.current_window_handle)
    driver.switch_to_window(str(windows[0]))

    print('Finished with the ' + str(idx+1) + ' click, it openned the ' + str(i) + ' element\n')




time.sleep(5)
print('5 seconds have just passed')

#print(soup)i
#with io.open('test.txt','w', encoding='utf-8') as file_obj:
#    file_obj.write('connection establised and the info is:\n\n' + driver.page_source)
#file_obj.close()

#close the page
driver.close()
from os import link
from sys import prefix
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import pandas  as pd

#Create instance of Chrome Driver
chrome_drive_path = '/home/brainlesspomo/chromedriver'
url = 'https://ec.europa.eu/eurostat/web/tourism/data/database'

#setting window size, position & opening the website
driver = webdriver.Chrome(chrome_drive_path)
driver.set_window_size(1600,900, windowHandle='current')
driver.set_window_position(1920, 0, windowHandle='current')
driver.get(url)


#Find the first folder of the db
#I have to open it so I reveal the files I need
first_fold = driver.find_element_by_class_name('title2')
first_fold.click()

#I need a helper (it is a footer logo, non clickable)
#Every time I open a page, there is text hiding the next link
helper = driver.find_element_by_id('footer_logos')
main_window = driver.current_window_handle

#Getting the link I want to open, it is the only link revealed with that class name
links = driver.find_elements_by_class_name('estat-icon-nui')

#opening the link except the last one, that I don't want
for idx, link in enumerate(links):
    helper.click()
    #den xreiazomai to teleutaio link me auto to onoma, ara den to anoigw
    if link == links[4]:
        break
    else:
        link.click()
    driver.switch_to_window(str(main_window))

    print('Finished with the ' + str(idx+1) + ' click, it openned the ' + str(link) + ' element\n')

#I am getting the window handles for future reference 
# and closing the first window as I don't need it from now on
windows = driver.window_handles
driver.close()

driver.switch_to.window(str(windows[1]))
try:
    wait1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
except TimeoutException:
    print('Load took too much time!!')
#take greece info from the first webpage
Webpage1_gr_infos = []
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell0']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell1']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell2']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell3']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell4']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell5']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell6']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell7']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell8']").text)
Webpage1_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell9']").text)

#take spain info from the first webpage
Webpage1_spain_infos = []
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell0']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell1']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell2']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell3']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell4']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell5']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell6']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell7']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell8']").text)
Webpage1_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell9']").text)

#go to second webpage
driver.switch_to.window(str(windows[2]))
try:
    wait2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
except TimeoutException:
    print('Load took too much time!!')

#take greece info from the second webpage
Webpage2_gr_infos = []
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell0']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell1']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell2']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell3']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell4']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell5']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell6']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell7']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell8']").text)
Webpage2_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell9']").text)

#take spain info from the second webpage
Webpage2_spain_infos = []
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell0']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell1']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell2']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell3']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell4']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell5']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell6']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell7']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell8']").text)
Webpage2_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell9']").text)

#go to third page
driver.switch_to.window(str(windows[3]))
try:
    wait3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
except TimeoutException:
    print('Load took too much time!!')

#take greece info from the third webpage
Webpage3_gr_infos = []
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell0']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell1']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell2']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell3']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell4']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell5']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell6']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell7']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell8']").text)
Webpage3_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell9']").text)

#take spain info from the third webpage
Webpage3_spain_infos = []
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell0']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell1']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell2']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell3']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell4']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell5']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell6']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell7']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell8']").text)
Webpage3_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell9']").text)

#go to forth webpage
driver.switch_to.window(str(windows[4]))
try:
    wait4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contents')))
except TimeoutException:
    print('Load took too much time!!')

#take greece info from the second webpage
Webpage4_gr_infos = []
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell0']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell1']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell2']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell3']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell4']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell5']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell6']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell7']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell8']").text)
Webpage4_gr_infos.append(driver.find_element_by_xpath("//div[@id='ptRow11']//div[@id='ptCell9']").text)

#take spain info from the second webpage
Webpage4_spain_infos = []
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell0']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell1']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell2']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell3']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell4']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell5']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell6']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell7']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell8']").text)
Webpage4_spain_infos.append(driver.find_element_by_xpath("//div[@id='ptRow12']//div[@id='ptCell9']").text)



#paths to txt files
path1 = 'stored_data/Nights spent at tourist accommodation establishments - monthly data.txt'
path2 = 'stored_data/Nights spent by non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data.txt'
path3 = 'stored_data/Arrivals at tourist accommodation establishments - monthly data.txt'
path4 = 'stored_data/Arrivals of non-residents at tourist accommodation establishments - 1990-2011 - world geographical breakdown - monthly data.txt'

#write the info from first page
with open(path1, 'w') as f1:
    f1.write('COUNTRY\t2020M07\t2020M08\t2020M09\t2020M10\t2020M11\t2020M12\t2020M01\t2020M02\t2020M03\t2020M04')
    f1.write('\nGREECE\t')
    for Webpage1_gr_info in Webpage1_gr_infos:
        f1.write(str(Webpage1_gr_info) + '\t')
    f1.write('\nSPAIN\t')
    for Webpage1_spain_info in Webpage1_spain_infos:
        f1.write(str(Webpage1_spain_info) + '\t')
f1.close()
with open(path2, 'w') as f2:
    #write the info from page 2
    f2.write('COUNTRY\t2011M03\t2011M04\t2011M05\t2011M06\t2011M07\t2011M08\t2011M09\t201M10\t2011M11\t201M12')
    f2.write('\nGREECE\t')
    for Webpage2_gr_info in Webpage2_gr_infos:
        f2.write(str(Webpage2_gr_info) + '\t')
    f2.write('\nSPAIN\t')
    for Webpage2_spain_info in Webpage2_spain_infos:
        f2.write(str(Webpage2_spain_info) + '\t')
f2.close()
with open(path3,'w') as f3:
    #write the info from page 3
    f3.write('COUNTRY\t2020M07\t2020M08\t2020M09\t2020M10\t2020M11\t2020M12\t2020M01\t2020M02\t2020M03\t2020M04')
    f3.write('\nGREECE\t')
    for Webpage3_gr_info in Webpage3_gr_infos:
        f3.write(str(Webpage3_gr_info) + '\t')
    f3.write('\nSPAIN\t')
    for Webpage3_spain_info in Webpage3_spain_infos:
        f3.write(str(Webpage3_spain_info) + '\t')
f3.close()
with open(path4,'w') as f4:
    #write the info from page 4
    f4.write('COUNTRY\t2011M03\t2011M04\t2011M05\t2011M06\t2011M07\t2011M08\t2011M09\t201M10\t2011M11\t201M12')
    f4.write('\nGREECE\t')
    for Webpage4_gr_info in Webpage4_gr_infos:
        f4.write(str(Webpage4_gr_info) + '\t')
    f4.write('\nSPAIN\t')
    for Webpage4_spain_info in Webpage4_spain_infos:
        f4.write(str(Webpage4_spain_info) + '\t')
f4.close()


#close the page after 5 seconds
time.sleep(2)
driver.quit()
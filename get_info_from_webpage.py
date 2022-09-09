from sqlite3.dbapi2 import connect
import sqlite3 as sql
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import chromedriver_autoinstaller
import os

# Search for chrome driver or make one if it does not exist
if str(os.name) == 'nt':
    chromedriver_autoinstaller.install()
else:
    print("This program is made for windows. I am sorry!!")
    quit()


url = 'https://ec.europa.eu/eurostat/web/tourism/data/database'
# setting window size, position & opening the website
driver = webdriver.Chrome()
driver.set_window_size(1920, 800, windowHandle='current')
driver.set_window_position(0, 0, windowHandle='current')
driver.get(url)

try:
    coockies_accept = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cck-actions')))
    # accept cockies to reveal the elements beneath it
    coockies_accept.click()

    coockies_close = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Close')))
    # accept cockies to reveal the elements beneath it
    coockies_close.click()
except TimeoutException:
    driver.refresh()

# Find the first folder of the db
# I have to open it so I reveal the files I need
first_fold = driver.find_element(By.CLASS_NAME, "title2")
first_fold.click()

# I need a helper (it is a footer logo, non clickable)
# Every time I open a page, there is text hiding the next link
helper = driver.find_element(By.ID, 'footer_logos')
main_window = driver.current_window_handle

# Getting the link I want to open, it is the only link revealed with that class name
links = driver.find_elements(By.CLASS_NAME, 'estat-icon-nui')

# opening the link except the last one, that I don't want
for idx, link in enumerate(links):
    helper.click()
    # den xreiazomai to teleutaio link me auto to onoma, ara den to anoigw
    if link == links[4]:
        break
    else:
        link.click()
    driver.switch_to.window(str(main_window))

    print('Finished with the ' + str(idx+1) +
          ' click, it openned the ' + str(link) + ' element\n')

# I am getting the window handles for future reference
# and closing the first window as I don't need it from now on
windows = driver.window_handles
driver.close()

driver.switch_to.window(str(windows[1]))
greeceCol = 0
spainCol = 0

try:
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'ptYDim0')))
    columns = driver.find_elements(By.CLASS_NAME, 'ptYDim')
    for i, column in enumerate(columns):
        if column.text == 'Greece':
            greeceCol = 'ptRow' + str(i)
        if column.text == 'Spain':
            spainCol = 'ptRow' + str(i)
except TimeoutException:
    driver.refresh()


# take greece info from the first webpage
Webpage1_gr_infos = ['GREECE']
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell0']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell1']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell2']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell3']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell4']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell5']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell6']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell7']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell8']").text)
Webpage1_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell9']").text)
# make the info beutiful
for i, Webpage1_gr_info in enumerate(Webpage1_gr_infos):
    temp = ''
    for char in Webpage1_gr_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage1_gr_infos[i] = temp

# take spain info from the first webpage
Webpage1_spain_infos = ['SPAIN']
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell0']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell1']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell2']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell3']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell4']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell5']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell6']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell7']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell8']").text)
Webpage1_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage1_spain_info in enumerate(Webpage1_spain_infos):
    temp = ''
    for char in Webpage1_spain_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage1_spain_infos[i] = temp

# go to second webpage
driver.switch_to.window(str(windows[2]))
# time.sleep(5)
try:
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'ptYDim0')))
    columns = driver.find_elements(By.CLASS_NAME, 'ptYDim')
    for i, column in enumerate(columns):
        if column.text == 'Greece':
            greeceCol = 'ptRow' + str(i)
        if column.text == 'Spain':
            spainCol = 'ptRow' + str(i)
except TimeoutException:
    driver.refresh()

# take greece info from the second webpage
Webpage2_gr_infos = ['GREECE']
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell0']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell1']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell2']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell3']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell4']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell5']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell6']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell7']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell8']").text)
Webpage2_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage2_gr_info in enumerate(Webpage2_gr_infos):
    temp = ''
    for char in Webpage2_gr_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage2_gr_infos[i] = temp

# take spain info from the second webpage
Webpage2_spain_infos = ['SPAIN']
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell0']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell1']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell2']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell3']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell4']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell5']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell6']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell7']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell8']").text)
Webpage2_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage2_spain_info in enumerate(Webpage2_spain_infos):
    temp = ''
    for char in Webpage2_spain_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage2_spain_infos[i] = temp

# go to third page
driver.switch_to.window(str(windows[3]))
# time.sleep(5)
try:
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'ptYDim0')))
    columns = driver.find_elements(By.CLASS_NAME, 'ptYDim')
    for i, column in enumerate(columns):
        if column.text == 'Greece':
            greeceCol = 'ptRow' + str(i)
        if column.text == 'Spain':
            spainCol = 'ptRow' + str(i)
except TimeoutException:
    driver.refresh()

# take greece info from the third webpage
Webpage3_gr_infos = ['GREECE']
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell0']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell1']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell2']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell3']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell4']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell5']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell6']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell7']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell8']").text)
Webpage3_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage3_gr_info in enumerate(Webpage3_gr_infos):
    temp = ''
    for char in Webpage3_gr_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage3_gr_infos[i] = temp


# take spain info from the third webpage
Webpage3_spain_infos = ['SPAIN']
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell0']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell1']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell2']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell3']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell4']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell5']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell6']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell7']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell8']").text)
Webpage3_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage3_spain_info in enumerate(Webpage3_spain_infos):
    temp = ''
    for char in Webpage3_spain_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage3_spain_infos[i] = temp

# go to forth webpage
driver.switch_to.window(str(windows[4]))
# time.sleep(5)
try:
    wait = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'ptYDim0')))
    columns = driver.find_elements(By.CLASS_NAME, 'ptYDim')
    for i, column in enumerate(columns):
        if column.text == 'Greece':
            greeceCol = 'ptRow' + str(i)
        if column.text == 'Spain':
            spainCol = 'ptRow' + str(i)
except TimeoutException:
    driver.refresh()

# take greece info from the second webpage
Webpage4_gr_infos = ['GREECE']
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell0']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell1']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell2']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell3']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell4']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell5']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell6']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell7']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell8']").text)
Webpage4_gr_infos.append(driver.find_element(By.XPATH,
                                             "//div[@id='" + str(greeceCol) + "']//div[@id='ptCell9']").text)

# make the info beutiful
for i, Webpage4_gr_info in enumerate(Webpage4_gr_infos):
    temp = ''
    for char in Webpage4_gr_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage4_gr_infos[i] = temp

# take spain info from the second webpage
Webpage4_spain_infos = ['SPAIN']
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell0']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell1']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell2']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell3']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell4']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell5']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell6']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell7']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell8']").text)
Webpage4_spain_infos.append(driver.find_element(By.XPATH,
                                                "//div[@id='" + str(spainCol) + "']//div[@id='ptCell9']").text)

# make the info beautiful
for i, Webpage4_spain_info in enumerate(Webpage4_spain_infos):
    temp = ''
    for char in Webpage4_spain_info:
        if char == ':':
            temp = ''
        elif char != '(' and char != ')' and char != 'e' and char != 'c' and char != ' ':
            temp += char
    Webpage4_spain_infos[i] = temp

# I have already the info that I need so I close the page seconds
driver.quit()

# connecting to db (msqlite)
connection = sql.connect('webpageInfo.db')

c = connection.cursor()

# send to db greece information
c.execute("INSERT INTO nights_tour VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage1_gr_infos[0],
    Webpage1_gr_infos[1],
    Webpage1_gr_infos[2],
    Webpage1_gr_infos[3],
    Webpage1_gr_infos[4],
    Webpage1_gr_infos[5],
    Webpage1_gr_infos[6],
    Webpage1_gr_infos[7],
    Webpage1_gr_infos[8],
    Webpage1_gr_infos[9],
    Webpage1_gr_infos[10]
)
)
c.execute("INSERT INTO nights_non_residents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage2_gr_infos[0],
    Webpage2_gr_infos[1],
    Webpage2_gr_infos[2],
    Webpage2_gr_infos[3],
    Webpage2_gr_infos[4],
    Webpage2_gr_infos[5],
    Webpage2_gr_infos[6],
    Webpage2_gr_infos[7],
    Webpage2_gr_infos[8],
    Webpage2_gr_infos[9],
    Webpage2_gr_infos[10]
)
)
c.execute("INSERT INTO arrivals_tour VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage3_gr_infos[0],
    Webpage3_gr_infos[1],
    Webpage3_gr_infos[2],
    Webpage3_gr_infos[3],
    Webpage3_gr_infos[4],
    Webpage3_gr_infos[5],
    Webpage3_gr_infos[6],
    Webpage3_gr_infos[7],
    Webpage3_gr_infos[8],
    Webpage3_gr_infos[9],
    Webpage3_gr_infos[10])
)
c.execute("INSERT INTO arrivals_non_residents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage4_gr_infos[0],
    Webpage4_gr_infos[1],
    Webpage4_gr_infos[2],
    Webpage4_gr_infos[3],
    Webpage4_gr_infos[4],
    Webpage4_gr_infos[5],
    Webpage4_gr_infos[6],
    Webpage4_gr_infos[7],
    Webpage4_gr_infos[8],
    Webpage4_gr_infos[9],
    Webpage4_gr_infos[10])
)

# send to db spain information
c.execute("INSERT INTO nights_tour VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage1_spain_infos[0],
    Webpage1_spain_infos[1],
    Webpage1_spain_infos[2],
    Webpage1_spain_infos[3],
    Webpage1_spain_infos[4],
    Webpage1_spain_infos[5],
    Webpage1_spain_infos[6],
    Webpage1_spain_infos[7],
    Webpage1_spain_infos[8],
    Webpage1_spain_infos[9],
    Webpage1_spain_infos[10])
)
c.execute("INSERT INTO nights_non_residents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage2_spain_infos[0],
    Webpage2_spain_infos[1],
    Webpage2_spain_infos[2],
    Webpage2_spain_infos[3],
    Webpage2_spain_infos[4],
    Webpage2_spain_infos[5],
    Webpage2_spain_infos[6],
    Webpage2_spain_infos[7],
    Webpage2_spain_infos[8],
    Webpage2_spain_infos[9],
    Webpage2_spain_infos[10])
)
c.execute("INSERT INTO arrivals_tour VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage3_spain_infos[0],
    Webpage3_spain_infos[1],
    Webpage3_spain_infos[2],
    Webpage3_spain_infos[3],
    Webpage3_spain_infos[4],
    Webpage3_spain_infos[5],
    Webpage3_spain_infos[6],
    Webpage3_spain_infos[7],
    Webpage3_spain_infos[8],
    Webpage3_spain_infos[9],
    Webpage3_spain_infos[10])
)
c.execute("INSERT INTO arrivals_non_residents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
    Webpage4_spain_infos[0],
    Webpage4_spain_infos[1],
    Webpage4_spain_infos[2],
    Webpage4_spain_infos[3],
    Webpage4_spain_infos[4],
    Webpage4_spain_infos[5],
    Webpage4_spain_infos[6],
    Webpage4_spain_infos[7],
    Webpage4_spain_infos[8],
    Webpage4_spain_infos[9],
    Webpage4_spain_infos[10])
)

connection.commit()

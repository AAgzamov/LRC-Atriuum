#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# COLORS.
WHITE = '\033[1;37;40m'
GREEN = '\033[1;32;40m'
RED = '\033[1;31;40m'
YELLOW = '\033[1;33;40m'
CYAN = '\033[1;36;40m'

# LOGIN SCRIPT.
username = str(input(f'{GREEN}[+]{WHITE} Enter username: '))
password = str(input(f'{GREEN}[+]{WHITE} Enter passowrd: '))

print(f'{YELLOW}[Info]{WHITE} Opening the website...')
driver = webdriver.Firefox()
driver.get('https://wiutuz.booksys.net')

print(f'{YELLOW}[Info]{WHITE} Browsing to the LOGIN PAGE...')
button = driver.find_element_by_id('librarylogonlink0')
button.click()

print(f'{CYAN}Sleeping for 1')
time.sleep(1)

print(f'{YELLOW}[Info]{WHITE} Logging in...')
try:
    driver.find_element_by_id('login_username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    button = driver.find_element_by_id('loginButtonID')
    button.click()
except:
    print(f'{RED}[Error]{WHITE} Cannot login!')

print(f'{CYAN}Sleeping for 1')
time.sleep(1)


# SCRIPT FOR CHANGING BOOK INFROMATION.
for i in range(1):
    data = pd.read_excel('./Barcodes.xlsx')
    #if i == 0:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 1')
    #    print(f'{YELLOW}[Info]{WHITE}Reading Set 1 ...')
    #elif i == 1:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 1')
    #    print(f'{YELLOW}[Info]{WHITE}Reading Set 2 ...')
    #elif i ==  2:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 3')
    #    print(f'{YELLOW}[Info]{WHITE}Reading Set 3 ...')
    #elif i == 3:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 4')
    #    print(f'{YELLOW}[Info]{WHITE}Reading Set 4 ...')
    #elif i == 4:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 5')
    #    print(f'{YELLOW}[Info]{WHITE}Reading Set 5 ...')

    for index, row in data.iterrows():
        print(f'{CYAN}Sleeping for 3 seconds ...')
        time.sleep(3)
        barcode = str(row['Barcodes'])
        print(f'\n{YELLOW}[Info]{WHITE} Editing Barcode: {GREEN}{barcode}{WHITE}\n')
        driver.find_element_by_id('GlobalKeywordSearchField').send_keys(barcode)
        #time.sleep(2)
        driver.find_element_by_id('GlobalKeywordSearchButton').click()
        time.sleep(1)
        driver.find_element_by_id('EditActiveHolding1').click()
        time.sleep(1)
        try:
            author = driver.find_element_by_id('bibliographicAuthor').text
            print(f'{YELLOW}[Info]{WHITE} Original author name: {GREEN}{author}{WHITE}')
            auth = author.split(' ')
            if len(auth) > 2:
                with open('check.txt', 'a') as f:
                    f.write('\n')
                    f.write(f'Several authors at: {barcode}')
            # if "Curtis, John".
            if str(auth[0])[-1] == ',':
                author = auth[0]
                #x = auth[0]
                #for i in range(len(x)):
                #    if x[i] == '\'' or x[i] == '.' or x[i] == ',':
                #        x.pop(i)
            # if "Curtis J".
            elif len(str(auth[1])) <= 1:
                author = auth[0]
                #x = auth[0]
                #for i in range(len(x)):
                #    if x[i] == '\'' or x[i] == '.' or x[i] == ',':
                #        x.pop(i)
            # if "Curtis J.".
            elif str(auth[1])[-1] == '.':
                author = auth[0]
                #x = auth[0]
                #for i in range(len(x)):
                #    if x[i] == '\'' or x[i] == '.' or x[i] == ',':
                #        x.pop(i)
            else:
                author = auth[1]
                #x = auth[1]
                #for i in range(len(x)):
                #    if x[i] == '\'' or x[i] == '.' or x[i] == ',':
                #        x.pop(i)
            author = author[0].upper() + author[1:3].lower()
            #print(f'{YELLOW}[Info]{WHITE} Author name: {GREEN}{author}{WHITE} ...')
        except:
            print(f'{RED}[Warning]{WHITE} Cannot define author name!')
        
        #print(f'{YELLOW}[Info]{WHITE} Changing Circulation Class ...')
        circulation = Select(driver.find_element_by_id('CircTypeCode'))
        circulation.select_by_visible_text('30-Day Loan')
        #time.sleep(1)
        #print(f'{YELLOW}[Info]{WHITE} Changing Report Class ...')
        report = Select(driver.find_element_by_id('ReportClassCode'))
        report.select_by_visible_text('Fiction')
        #print(f'{YELLOW}[Info]{WHITE} Clearing Prefix ...')
        driver.find_element_by_id('CallNumberPrefix').clear()
        #time.sleep(2)
        #print(f'{YELLOW}[Info]{WHITE} Clearing Call No. ...')
        driver.find_element_by_id('CallNumberMiddle').clear()
        print(f'{YELLOW}[Info]{WHITE} Changing Call No.:')
        print(f'{GREEN}Fiction\n{author}')
        try:
            driver.find_element_by_id('CallNumberMiddle').send_keys('Fiction', Keys.ENTER, author)
        except:
            print(f'{RED}[Warning]{WHITE} Could not change Call No.!')
        for i in range(len(author)):
            if author[i] == '\'' or author[i] == '.' or author[i] == ',':
                with open('check.txt', 'a') as f:
                    f.write('\n')
                    f.write(f'Strange name at: {barcode}')
                break
        #print(f'{YELLOW}[Info] Saving...')
        driver.find_element_by_id('bsiSave').click()
        print(f'\n{GREEN}[+]{WHITE} Saved changes of {GREEN}{barcode}{WHITE}!')



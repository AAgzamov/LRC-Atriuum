from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# LOGIN SCRIPT.
username = str(input(f'[+] Enter username: '))
password = str(input(f'[+] Enter passowrd: '))

print(f' [Info] Opening the website...')
driver = webdriver.Firefox()
driver.get('https://wiutuz.booksys.net')

print(f' [Info] Browsing to the LOGIN PAGE...')
button = driver.find_element_by_id('librarylogonlink0')
button.click()

print(f' Sleeping for 1')
time.sleep(1)

print(f' [Info] Logging in...')
try:
    driver.find_element_by_id('login_username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    button = driver.find_element_by_id('loginButtonID')
    button.click()
except:
    print(f' [Error] Cannot login!')

print(f' Sleeping for 1')
time.sleep(1)


# SCRIPT FOR CHANGING BOOK INFROMATION.
for i in range(1):
    data = pd.read_excel('./Barcodes.xlsx')
    #if i == 0:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 1')
    #    print(f' [Info]Reading Set 1 ...')
    #elif i == 1:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 1')
    #    print(f' [Info]Reading Set 2 ...')
    #elif i ==  2:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 3')
    #    print(f' [Info]Reading Set 3 ...')
    #elif i == 3:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 4')
    #    print(f' [Info]Reading Set 4 ...')
    #elif i == 4:
    #    data = pd.read_excel('./Barcodes.xlsx', sheet_name='Set 5')
    #    print(f' [Info]Reading Set 5 ...')

    for index, row in data.iterrows():
        print(f' Sleeping for 3 seconds ...')
        time.sleep(3)
        barcode = str(row['Barcodes'])
        print(f'\n [Info] Editing Barcode: {barcode}\n')
        driver.find_element_by_id('GlobalKeywordSearchField').send_keys(barcode)
        #time.sleep(2)
        driver.find_element_by_id('GlobalKeywordSearchButton').click()
        time.sleep(1)
        driver.find_element_by_id('EditActiveHolding1').click()
        time.sleep(1)
        try:
            author = driver.find_element_by_id('bibliographicAuthor').text
            print(f' [Info] Original author name: {author} ')
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
            #print(f' [Info] Author name: {author} ...')
        except:
            print(f' [Warning] Cannot define author name!')

        #print(f' [Info] Changing Circulation Class ...')
        circulation = Select(driver.find_element_by_id('CircTypeCode'))
        circulation.select_by_visible_text('30-Day Loan')
        #time.sleep(1)
        #print(f' [Info] Changing Report Class ...')
        report = Select(driver.find_element_by_id('ReportClassCode'))
        report.select_by_visible_text('Fiction')
        #print(f' [Info] Clearing Prefix ...')
        driver.find_element_by_id('CallNumberPrefix').clear()
        #time.sleep(2)
        #print(f' [Info] Clearing Call No. ...')
        driver.find_element_by_id('CallNumberMiddle').clear()
        print(f' [Info] Changing Call No.:')
        print(f'Fiction\n{author}')
        try:
            driver.find_element_by_id('CallNumberMiddle').send_keys('Fiction', Keys.ENTER, author)
        except:
            print(f' [Warning] Could not change Call No.!')
        for i in range(len(author)):
            if author[i] == '\'' or author[i] == '.' or author[i] == ',':
                with open('check.txt', 'a') as f:
                    f.write('\n')
                    f.write(f'Strange name at: {barcode}')
                break
        #print(f' [Info] Saving...')
        driver.find_element_by_id('bsiSave').click()
        print(f'\n[+] Saved changes of {barcode}!')

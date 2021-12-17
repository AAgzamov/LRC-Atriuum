from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os

def intro():
    print('''
    
        00      000000.   000000        00          00  00000000  00    00  00000000
        00      000  00  00`````        00          00  ```00```  00    00  ```00```
        00      000000.  00              00   00   00`     00     00    00     00
        00      000.``   00              00   00   00      00     00    00     00
        00      00 0.    00               00 0000 00`      00     00    00     00
        000000  00  0.   `000000          0000``0000    00000000  00000000     00
        ``````  ``  ``    ``````          ````  ````    ````````  ````````     ``


                                                            By AAgzamov 

            ''')

def mode():
    while 1:
        user = str(input('Choose active or silent mode (a/s): '))
        if user == 'a':
            return 'a'
        elif user == 's':
            return 's'
        else:
            print('[-] Invalid option!')

def credentials():
    username = str(input('[+] Enter the username: '))
    password = str(input('[+] Enter the password: '))
    return username, password

def call_prefix():
    print('''
        
        What to do with Call Number Prefix?
        [0] Clean.

            ''')

def call_number():
    print('''
        
        What to do with the Call Number?
        [0] Clean.
        [1] "Fiction" and "First 3 letters of the author's surname".

            ''')

def physical_location():
    while 1:
        back = False
        print('''
        
        Indicate Physical Location.

        [0] At Circulation Desk.        [6] Final Projects.     [12] Silent Area.
        [1] Cass Main Area.             [7] Internet.           [13] Strategy Room.
        [2] CD Main Area.               [8] Journals.           [14] Undefined Items.
        [3] Discussion Area.            [9] LRC Archive.        [15] Urgench-Samarkand.
        [4] Dormitory 1.                [10] Lyceum Library.    [16] WIUT_Lyceum Library.
        [5] Dormitory 2.                [11] Main Lybrary.      [17] Work Group Area (Cherdak).

    ''')
        user = input('--> ')
        if user not in range(0, 10):
            print('[-] Invalid option!')
            continue
        elif user in range(0, 10):
            return user

def edit_options():
    while 1:
        back = False
        print('''

        Edit Options:
        [0] Barcode Excel List.
        [1] Single Barcode Input.

        ''')
        user = input('--> ')
        if user == '0':
            while 1:
                excel_path = input('Enter the path to an excel file: ')
                if excel_path == 'back()':
                    back = True
                    break
                if os.access(excel_path, os.F_OK):
                    return user, excel_path
                else:
                    print('[-] Invalid path or file does not exist!')
            if back:
                continue
        elif user == '1':
            return user, False
        else:
            print('[-] Invalid option!')

def edit_values():
    while 1:
        print('Enter the values for the following variables.\n')
        circulation_value = input('Circulation Class: ')
        report_value = input('Report Class: ')
        call_prefix()
        call_prefix_value = input('--> ')
        call_number()
        call_number_value = input('--> ')
        location_value = physical_location()


        
        return circulation_value, report_value, call_prefix_value, call_number_value, location_value



class Atriuum():
    def __init__(self, username, password, mode):
        self.username = username
        self.password = password
        self.mode = mode

    def open(self):
        if self.mode == 'a':
            print('[i] Opening Atriuum Website...')
            driver = webdriver.Firefox()
            driver.get('https://wiutuz.booksys.net')
            time.sleep(1)
            button = driver.find_element_by_id('librarylogonlink0')
            button.click()
            while 1:
                try:
                    time.sleep(1)
                    print('[i] Entering username and password...')
                    driver.find_element_by_id('login_username').send_keys(username)
                    driver.find_element_by_id('password').send_keys(password)
                    button = driver.find_element_by_id('loginButtonID')
                    button.click()
                    time.sleep(1)
                    try:
                        if driver.find_element_by_class_name('error error-block'):
                            success = False
                    except:
                        success = True
                except:
                    print('[-] Invalid username or password!')
                    username, password = credentials()
                    success = False
                if success:
                    print('[i] Logged in successfully.')
                    break
                
        elif self.mode == 's':
            pass

        def edit_barcodes(self, edit, *args):
            if self.edit == '0':
                data = pd.read_excel(*args)
                pass
                
            elif self.edit == '1':
                barcode = input('[+] Enter the barcode: ')

                print('[i] Barcode: {}'.format(barcode))
                pass

            

intro()
mode = mode()
username, password = credentials()


# LOGIN SCRIPT.
website = Atriuum(username, password, mode)
website.open()


# EDIT OPTION SCRIPT.
edit, path = edit_options()
if edit == '0':
    website.edit_barcodes(edit, path)
elif edit == '1':
    website.edit_barcodes(edit)


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

print('Finished!')

input()

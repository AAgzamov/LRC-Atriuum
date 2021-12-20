try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.keys import Keys
    import pandas as pd
    import time
    import os
    import getpass
except:
    print('[-] Cannot import libraries!')
    print('[i] Execution is impossible.')
    input()

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

def license():
    print('Program repository available at https://www.github.com/AAgzamov/LRC-Atriuum')
    print('For license refer to https://www.github.com/AAgzamov/LRC-Atriuum/LICENSE.md')


def menu():
    while 1:
        print('''
        
        [0] Start.
        [1] License.

                ''')
        user = input('--> ')
        if user == '0':
            return user
        elif user == '1':
            license()
            input()

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
    username = str(input('[+] Username: '))
    password = str(getpass.getpass('[+] Password: '))
    return username, password

def circulation_class():
    pass

def report_class():
    pass

def call_prefix():
    while 1:
        back = False
        print('''
        
        What to do with Call Number Prefix?
        [0] Clean.

            ''')

        user = str(input('--> '))
        if user == '0':
            return user
        elif user != '0':
            print('[-] Invalid option!')
            continue


def call_number():
    while 1:
        back = False
        print('''
        
        What to do with the Call Number?
        [0] Clean.
        [1] "Fiction" and "First 3 letters of the author's surname".
        [2] Other.

            ''')

        user = str(input('--> '))
        if user == '0':
            return user
        elif user == '1':
            pass
        elif user == '2':
            while 1:
                user = input('Set Call Number: ')
                if user == 'back()':
                    break
                else:
                    return user
        else:
            print('[-] Invalid option!')
            continue

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
        [5] Dormitory 2.                [11] Main Library.      [17] Work Group Area (Cherdak).

    ''')
        user = str(input('--> '))
        if user == '0':
            return 'At Circulation Desk'
        elif user == '1':
            return 'Cass Main Area'
        elif user == '2':
            return 'CD Main Area'
        elif user == '3':
            return 'Discussion Area'
        elif user == '4':
            return 'Dormitory 1'
        elif user == '5':
            return 'Dormitory 2'
        elif user == '6':
            return 'Final Projects'
        elif user == '7':
            return 'Internet'
        elif user == '8':
            return 'Journals'
        elif user == '9':
            return 'LRC Archive'
        elif user == '10':
            return 'Lyceum Library'
        elif user == '11':
            return 'Main Library'
        elif user == '12':
            return 'Silent Area'
        elif user == '13':
            return 'Strategy Room'
        elif user == '14':
            return 'Undefined Items'
        elif user == '15':
            return 'Urgench-Samarkand'
        elif user == '16':
            return 'WIUT_Lyceum Library'
        elif user == '17':
            return 'Work Group Area (Cherdak)'
        else:
            print('[-] Invalid option!')
            continue

def edit_options():
    while 1:
        back = False
        print('''

        Edit Options:
        [0] Barcode Excel List.
        [1] Single Barcode Input.

        ''')
        user = str(input('--> '))
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
    print('Set the values for the following variables.\n')
    circulation_value = input('Circulation Class: ')
    report_value = input('Report Class: ')
    call_prefix_value = call_prefix()
    call_number_value = call_number()
    physical_location_value = physical_location()    
    return circulation_value, report_value, call_prefix_value, call_number_value, physical_location_value



class Atriuum():
    def __init__(self, username, password, mode):
        self.username = username
        self.password = password
        self.mode = mode

    def open(self, username, password):
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
                    driver.find_element_by_id('login_username').send_keys(self.username)
                    driver.find_element_by_id('password').send_keys(self.password)
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
                    self.username, self.password = credentials()
                    success = False
                if success:
                    print('[i] Logged in successfully.')
                    break
                
        elif self.mode == 's':
            pass

    def edit_barcodes(self, edit, *args, path=None):
        self.edit = edit
        self.args = args
        self.path = path
        if self.edit == '0':
            data = pd.read_excel(self.path)
            pass
    
        elif self.edit == '1':
            barcode = input('[+] Enter the barcodes: ')
            for i in barcode:
                if i == ',':
                    barcode = barcode.split(', ')
                    for b in barcode:
                        print('[i] Barcode: {}'.format(b))
                        driver.find_element_by_id('GlobalKeywordSearchField').send_keys(b)
                        driver.find_element_by_id('GlobalKeywordSearchButton').click()
                        time.sleep(1)
                        for num in range(1, 11):
                            try:
                                driver.find_element_by_id('EditActiveHolding{num}'.format(str(num))).click()
                                # Circulation Class.
                                Select(driver.find_element_by_id('CircTypeCode')).select_by_visible_text(self.arg[0])
                                
                                # Report Class.
                                Select(driver.find_element_by_id('ReportClassCode')).select_by_visible_text(self.arg[1])
                                
                                # Call Number Prefix.
                                if self.arg[2] == '0':
                                    driver.find_element_by_id('CallNumberPrefix').clear()

                                # Call Number.
                                if self.arg[3] == '0':
                                    driver.find_element_by_id('CallNumberMiddle').clear()
                                elif self.arg[3] == '1':
                                    pass
                                else:
                                    temp = arg[3]
                                    temp = temp.split(' ')
                                    driver.find_element_by_id('CallNumberMiddle').clear()
                                    driver.find_element_by_id('CallNumberMiddle').send_keys(temp[0], Keys.ENTER, temp[1])
                                
                                # Physical Location.
                                Select(driver.find_element_by_id('SublocationCode')).select_by_visible_text(self.arg[4])
                                
                                # Save Changes.
                                driver.find_element_by_id('bsiSave').click()
                                print('[i] Saved changes.')
                                time.sleep(2)

                            except:
                                break
                else:
                    print('[i] Barcode: {}'.format(barcode))
                    driver.find_element_by_id('GlobalKeywordSearchField').send_keys(barcode)
                    driver.find_element_by_id('GlobalKeywordSearchButton').click()
                    time.sleep(1)
                    for num in range(1, 11):
                        try:
                            driver.find_element_by_id('EditActiveHolding{num}'.format(str(num))).click()
                            # Circulation Class.
                            Select(driver.find_element_by_id('CircTypeCode')).select_by_visible_text(self.arg[0])
                                
                            # Report Class.
                            Select(driver.find_element_by_id('ReportClassCode')).select_by_visible_text(self.arg[1])
                                
                            # Call Number Prefix.
                            if self.arg[2] == '0':
                                driver.find_element_by_id('CallNumberPrefix').clear()

                            # Call Number.
                            if self.arg[3] == '0':
                                driver.find_element_by_id('CallNumberMiddle').clear()
                            elif self.arg[3] == '1':
                                pass
                            else:
                                temp = arg[3]
                                temp = temp.split(' ')
                                driver.find_element_by_id('CallNumberMiddle').clear()
                                driver.find_element_by_id('CallNumberMiddle').send_keys(temp[0], Keys.ENTER, temp[1])
                                
                            # Physical Location.
                            Select(driver.find_element_by_id('SublocationCode')).select_by_visible_text(self.arg[4])
                                
                            # Save Changes.
                            driver.find_element_by_id('bsiSave').click()
                            print('[i] Saved changes.')
                            time.sleep(2)
                        except:
                            break



# MENU SCRIPT.
intro()
user = menu()
if user == '0':
    mode = mode()
    username, password = credentials()

    # LOGIN SCRIPT.
    website = Atriuum(username, password, mode)
    website.open(username, password)

    # EDIT SCRIPT.
    edit, path = edit_options()
    circulation, report, call_prefix, call_number, physical_location = edit_values()
    if edit == '0':
        website.edit_barcodes(edit, circulation, report, call_prefix, call_number, physical_location, path=path)
    elif edit == '1':
        website.edit_barcodes(edit, circulation, report, call_prefix, call_number, physical_location)


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

try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import os
    import getpass
    import magic
    import datetime
    import pytz
except:
    print('[-] Cannot import libraries!')
    print('[i] Execution is impossible.')
    input()
    exit()

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
        else:
            print('[-] Invalid option!')

def mode():
    while 1:
        user = str(input('\nChoose active or silent mode (a/s): '))
        if user == 'a':
            return 'a'
        elif user == 's':
            return 's'
        else:
            print('[-] Invalid option!')

def logging():
    while 1:
        user = str(input('\nSave logs (y/n)? '))
        if user == 'y' or user == 'n':
            return user
        else:
            print('[-] Invalid option!')

def make_log(logs, *args):
    if logs == 'y':
        if args[0] == 'Barcode':
            with open('logs.txt', 'a') as file:
                file.write('\n')
                file.write('{}: {}.'.format(args[0], args[1]))
        else:
            with open('logs.txt', 'a') as file:
                file.write(' {}: {}.'.format(args[0], args[1]))

def credentials():
    username = str(input('\n[+] Username: '))
    password = str(getpass.getpass('[+] Password: '))
    return username, password

def circulation_class():
    while 1:
        back = False
        print('''

            Item Circulation Class.

            [S] SKIP.

            [0] 1-Day Loan.         [4] AV Circ.
            [1] 3-Day Loan.         [5] Circulation.
            [2] 7-Day Loan.         [6] Online.
            [3] 30-Day Loan.        [7] Reference.

                ''')
        user = str(input('--> ')).lower()
        if user == '0':
            return '1-Day Loan'
        elif user == '1':
            return '3-Day Loan'
        elif user == '2':
            return '7-Day Loan'
        elif user == '3':
            return '30-Day Loan'
        elif user == '4':
            return 'AV Circ'
        elif user == '5':
            return 'Circulation'
        elif user == '6':
            return 'Online'
        elif user == '7':
            return 'Reference'
        elif user == 's':
            return None
        else:
            print('[-] Invalid option!')

def report_class():
    while 1:
        back = False
        print('''

            Item Report Class.

            [S] SKIP.

            [0] 000-099.        [6] 600-699.            [12] CD.                    [18] Undefined.
            [1] 100-199.        [7] 700-799.            [13] Easy Book.             [19] Videocassettes.
            [2] 200-299.        [8] 800-899.            [14] eBook.
            [3] 300-399.        [9] 900-999.            [15] Fiction.
            [4] 400-499.        [10] Audiocassettes.    [16] Journal/Newspaper.
            [5] 500-599.        [11] Biography.         [17] Large Print.


                ''')
        user = str(input('--> ')).lower()
        if user == '0':
            return '000-099'
        elif user == '1':
            return '100-199'
        elif user == '2':
            return '200-299'
        elif user == '3':
            return '300-399'
        elif user == '4':
            return '400-499'
        elif user == '5':
            return '500-599'
        elif user == '6':
            return '600-699'
        elif user == '7':
            return '700-799'
        elif user == '8':
            return '800-899'
        elif user == '9':
            return '900-999'
        elif user == '10':
            return 'Audiocassettes'
        elif user == '11':
            return 'Biography'
        elif user == '12':
            return 'CD'
        elif user == '13':
            return 'Easy Books'
        elif user == '14':
            return 'eBooks'
        elif user == '15':
            return 'Fiction'
        elif user == '16':
            return 'Journal/Newspaper'
        elif user == '17':
            return 'Large Print'
        elif user == '18':
            return 'Undefined'
        elif user == '19':
            return 'Videocassettes'
        elif user == 's':
            return None
        else:
            print('[-] Invalid option!')

def call_prefix():
    while 1:
        back = False
        print('''

        What to do with Call Number Prefix?

        [S] SKIP.

        [0] CLEAN.

            ''')

        user = str(input('--> ')).lower()
        if user == '0':
            return user
        elif user == 's':
            return None
        else:
            print('[-] Invalid option!')
            continue


def call_number():
    while 1:
        back = False
        print('''

        What to do with the Call Number?

        [S] SKIP.

        [0] CLEAN.
        [1] "Fiction" and "First 3 letters of the author's surname".
        [2] OTHER.

            ''')

        user = str(input('--> ')).lower()
        if user == '0':
            return user
        elif user == '1':
            return user
        elif user == '2':
            while 1:
                user = str(input('Set Call Number: '))
                if user == 'back()':
                    break
                else:
                    return user
        elif user == 's':
            return None
        else:
            print('[-] Invalid option!')
            continue

def physical_location():
    while 1:
        back = False
        print('''

        Indicate Physical Location.

        [S] SKIP.

        [0] At Circulation Desk.        [6] Final Projects.     [12] Silent Area.
        [1] Cass Main Area.             [7] Internet.           [13] Strategy Room.
        [2] CD Main Area.               [8] Journals.           [14] Undefined Items.
        [3] Discussion Area.            [9] LRC Archive.        [15] Urgench-Samarkand.
        [4] Dormitory 1.                [10] Lyceum Library.    [16] WIUT_Lyceum Library.
        [5] Dormitory 2.                [11] Main Library.      [17] Work Group Area (Cherdak).

    ''')
        user = str(input('--> ')).lower()
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
        elif user == 's':
            return None
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
                #if os.access(excel_path, os.F_OK):
                #    return user, excel_path
                try:
                    if magic.from_file(excel_path, mime=True) == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                        return user, excel_path
                    else:
                        print('[-] Invalid path or wrong file type!')
                except:
                    print('[-] Invalid path or wrong file type!')
            if back:
                continue
        elif user == '1':
            return user, None
        else:
            print('[-] Invalid option!')

def edit_values():
    print('Set the values for the following variables.\n')
    circulation_value = circulation_class()
    report_value = report_class()
    call_prefix_value = call_prefix()
    call_number_value = call_number()
    physical_location_value = physical_location()
    return circulation_value, report_value, call_prefix_value, call_number_value, physical_location_value



class Atriuum():
    def __init__(self, username, password, mode):
        self.username = username
        self.password = password
        self.mode = mode

    def open(self, username, password, logs):
        self.logs = logs
        if self.mode == 'a':
            print('[i] Opening Atriuum Website...')
            global driver
            driver = webdriver.Firefox()
            driver.get('https://wiutuz.booksys.net')
            time.sleep(1)
            driver.find_element(By.ID, 'librarylogonlink0').click()
            while 1:
                try:
                    time.sleep(1)
                    print('[i] Entering username and password...')
                    driver.find_element(By.ID, 'login_username').clear()
                    driver.find_element(By.ID, 'password').clear()
                    driver.find_element(By.ID, 'login_username').send_keys(self.username)
                    driver.find_element(By.ID, 'password').send_keys(self.password)
                    driver.find_element(By.ID, 'loginButtonID').click()
                    time.sleep(1)
                    try:
                        if driver.find_element(By.CLASS_NAME, 'error error-block'):
                            success = False
                    except:
                        success = True
                except:
                    print('[-] Invalid username or password!')
                    self.username, self.password = credentials()
                    success = False
                if success:
                    print('[i] Logged in successfully.')
                    if self.logs == 'y':
                        with open('logs.txt', 'a') as file:
                            file.write('"{}" logged in on {}'.format(self.username, datetime.datetime.now().astimezone(pytz.timezone('Asia/Tashkent')).strftime('%B %d, %Y at %H:%M:%S')))
                            file.write('\n')
                    break

        elif self.mode == 's':
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print('[i] Silent mode is ON.')
            print('[i] Wait...')
            driver.get('https://wiutuz.booksys.net')
            time.sleep(1)
            driver.find_element(By.ID, 'librarylogonlink0').click()
            while 1:
                try:
                    time.sleep(1)
                    print('[i] Entering the username and password...')
                    driver.find_element(By.ID, 'login_username').clear()
                    driver.find_element(By.ID, 'password').clear()
                    driver.find_element(By.ID, 'login_username').send_keys(self.username)
                    driver.find_element(By.ID, 'password').send_keys(self.password)
                    driver.find_element(By.ID, 'loginButtonID').click()
                    time.sleep(1)
                    try:
                        if driver.find_element(By.CLASS_NAME, 'error error-block'):
                            success = False
                    except:
                        success = True
                except:
                    print('[-] Invalid username or password!')
                    self.username, self.password = credentials()
                    success = False
                if success:
                    print('[i] Logged in successfully.')
                    if self.logs == 'y':
                        with open('logs.txt', 'a') as file:
                            file.write('"{}" logged in on {}'.format(self.username, datetime.datetime.now().astimezone(pytz.timezone('Asia/Tashkent')).strftime('%B %d, %Y at %H:%M:%S')))
                            file.write('\n')
                    break


    def edit_barcodes(self, edit, logs,  *args, path=None):
        self.edit = edit
        self.logs = logs
        self.args = args
        self.path = path
        if self.edit == '0':
            while 1:
                try:
                    sets = int(input('[+] Number of sheets in excel file: '))
                    break
                except:
                    print('\n[-] Only integers are acceptible!')
            for sheet_number in range(1, sets+1):
                data = pd.read_excel(self.path, sheet_name='Set {}'.format(sheet_number))
                print('[i] Set {}.'.format(sheet_number))
                for index, row in data.iterrows():
                    barcode = str(row['Barcodes'])
                    print('[i] Barcode: {}.'.format(barcode))
                    driver.find_element(By.ID, 'GlobalKeywordSearchField').send_keys(barcode)
                    driver.find_element(By.ID, 'GlobalKeywordSearchButton').click()
                    make_log(self.logs, 'Barcode', barcode)
                    time.sleep(1)
                    for num in range(1, 11):
                        try:
                            driver.find_element(By.ID, 'EditActiveHolding{}'.format(str(num))).click()
                            # Circulation Class.
                            if self.args[0] != None:
                                Select(driver.find_element(By.ID, 'CircTypeCode')).select_by_visible_text(self.args[0])
                                make_log(self.logs, 'Circulation Class', self.args[0])
                            # Report Class.
                            if self.args[1] != None:
                                Select(driver.find_element(By.ID, 'ReportClassCode')).select_by_visible_text(self.args[1])
                                make_log(self.logs, 'Report Class', self.args[1])

                            # Call Number Prefix.
                            if self.args[2] != None:
                                if self.args[2] == '0':
                                    driver.find_element(By.ID, 'CallNumberPrefix').clear()
                                    make_log(self.logs, 'Call Number Prefix', self.args[2])

                            # Call Number.
                            if self.args[3] != None:
                                if self.args[3] == '0':
                                    driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                elif self.args[3] == '1':
                                    try:
                                        author = driver.find_element_by_id('bibliographicAuthor').text
                                        print('[i] Original author name: {} '.format(author))
                                        auth = author.split(' ')
                                        if len(auth) > 2:
                                            with open('check.txt', 'a') as file:
                                                file.write('\n')
                                                file.write('Several authors at: {}'.format(barcode))
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
                                        driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                        driver.find_element(By.ID, 'CallNumberMiddle').send_keys('Fiction', Keys.ENTER, author)
                                    except:
                                        print('[-] Cannot define author name!')
                                else:
                                    temp = self.args[3]
                                    for space in temp:
                                        if space == '':
                                            temp = temp.split(' ')
                                            driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                            driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp[0], Keys.ENTER, temp[1])
                                        else:
                                            driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                            driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp)

                            # Physical Location.
                            if self.args[4] != None:
                                Select(driver.find_element(By.ID, 'SublocationCode')).select_by_visible_text(self.args[4])

                            # Save Changes.
                            driver.find_element(By.ID, 'bsiSave').click()
                            print('[i] Saved changes.')
                            make_log(self.logs, 'Circulation Class', self.args[0])
                            make_log(self.logs, 'Report Class', self.args[1])
                            make_log(self.logs, 'Call Number Prefix', self.args[2])
                            make_log(self.logs, 'Call Number', self.args[3])
                            make_log(self.logs, 'Physical Location', self.args[4])
                            # if self.logs == 'y':
                            #     with open('logs.txt', 'a') as file:
                            #         file.write('Barcode: {}.'.format(barcode))
                            #         file.write('Circulation Class: {}.'.format(self.args[0]))
                            #         file.write('Report Class: {}.'.format(self.args[1]))
                            #         file.write('Call Number Prefix: {}.'.format(self.args[2]))
                            #         file.write('Call Number: {}.'.format(self.args[3]))
                            #         file.write('Physical Location: {}.'.format(self.args[4]))
                            #         file.write('\n')
                            time.sleep(2)

                        except:
                            break


        elif self.edit == '1':
            many_barcodes = False
            barcode = str(input('[+] Enter the barcodes: '))
            for i in barcode:
                if i == ',':
                    many_barcodes = True
                    barcode = barcode.split(', ')
                    for b in barcode:
                        print('[i] Barcode: {}.'.format(b))
                        driver.find_element(By.ID, 'GlobalKeywordSearchField').send_keys(b)
                        driver.find_element(By.ID, 'GlobalKeywordSearchButton').click()
                        time.sleep(1)
                        for num in range(1, 11):
                            try:
                                driver.find_element(By.ID, 'EditActiveHolding{}'.format(str(num))).click()
                                # Circulation Class.
                                if self.args[0] != None:
                                    Select(driver.find_element(By.ID, 'CircTypeCode')).select_by_visible_text(self.args[0])

                                # Report Class.
                                if self.args[1] != None:
                                    Select(driver.find_element(By.ID, 'ReportClassCode')).select_by_visible_text(self.args[1])

                                # Call Number Prefix.
                                if self.args[2] != None:
                                    if self.args[2] == '0':
                                        driver.find_element(By.ID, 'CallNumberPrefix').clear()

                                # Call Number.
                                if self.args[3] != None:
                                    if self.args[3] == '0':
                                        driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                    elif self.args[3] == '1':
                                        try:
                                            author = driver.find_element_by_id('bibliographicAuthor').text
                                            print('[i] Original author name: {} '.format(author))
                                            auth = author.split(' ')
                                            if len(auth) > 2:
                                                with open('check.txt', 'a') as file:
                                                    file.write('\n')
                                                    file.write('Several authors at: {}'.format(barcode))
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
                                            driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                            driver.find_element(By.ID, 'CallNumberMiddle').send_keys('Fiction', Keys.ENTER, author)

                                        except:
                                            print('[-] Cannot define author name!')

                                    else:
                                        temp = self.args[3]
                                        for space in temp:
                                            if space == '':
                                                temp = temp.split(' ')
                                                driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                                driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp[0], Keys.ENTER, temp[1])
                                            else:
                                                driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                                driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp)

                                # Physical Location.
                                if self.args[4] != None:
                                    Select(driver.find_element(By.ID, 'SublocationCode')).select_by_visible_text(self.args[4])

                                # Save Changes.
                                driver.find_element(By.ID, 'bsiSave').click()
                                print('[i] Saved changes.')
                                if self.logs == 'y':
                                    with open('logs.txt', 'a') as file:
                                        file.write('Barcode: {}.'.format(barcode))
                                        file.write('Circulation Class: {}.'.format(self.args[0]))
                                        file.write('Report Class: {}.'.format(self.args[1]))
                                        file.write('Call Number Prefix: {}.'.format(self.args[2]))
                                        file.write('Call Number: {}.'.format(self.args[3]))
                                        file.write('Physical Location: {}.'.format(self.args[4]))
                                        file.write('\n')
                                time.sleep(2)

                            except:
                                break
            if not many_barcodes:
                print('[i] Barcode: {}'.format(barcode))
                driver.find_element(By.ID, 'GlobalKeywordSearchField').send_keys(barcode)
                driver.find_element(By.ID, 'GlobalKeywordSearchButton').click()
                make_log(self.logs, 'Barcode', barcode)
                time.sleep(1)
                for num in range(1, 11):
                    try:
                        driver.find_element(By.ID, 'EditActiveHolding{}'.format(str(num))).click()
                        # Circulation Class.
                        if self.args[0] != None:
                            Select(driver.find_element(By.ID, 'CircTypeCode')).select_by_visible_text(self.args[0])

                        # Report Class.
                        if self.args[1] != None:
                            Select(driver.find_element(By.ID, 'ReportClassCode')).select_by_visible_text(self.args[1])

                        # Call Number Prefix.
                        if self.args[2] != None:
                            if self.args[2] == '0':
                                driver.find_element(By.ID, 'CallNumberPrefix').clear()

                        # Call Number.
                        if self.args[3] != None:
                            if self.args[3] == '0':
                                driver.find_element(By.ID, 'CallNumberMiddle').clear()
                            elif self.args[3] == '1':
                                try:
                                    author = driver.find_element_by_id('bibliographicAuthor').text
                                    print('[i] Original author name: {} '.format(author))
                                    auth = author.split(' ')
                                    if len(auth) > 2:
                                        with open('check.txt', 'a') as file:
                                            file.write('\n')
                                            file.write('Several authors at: {}'.format(barcode))
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
                                    driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                    driver.find_element(By.ID, 'CallNumberMiddle').send_keys('Fiction', Keys.ENTER, author)

                                except:
                                    print('[-] Cannot define author name!')

                            else:
                                temp = args[3]
                                for space in temp:
                                    if space == '':
                                        temp = temp.split(' ')
                                        driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                        driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp[0], Keys.ENTER, temp[1])
                                    else:
                                        driver.find_element(By.ID, 'CallNumberMiddle').clear()
                                        driver.find_element(By.ID, 'CallNumberMiddle').send_keys(temp)
                        # Physical Location.
                        if self.args[4] != None:
                            Select(driver.find_element(By.ID, 'SublocationCode')).select_by_visible_text(self.args[4])

                        # Save Changes.
                        driver.find_element(By.ID, 'bsiSave').click()
                        print('[i] Saved changes.')
                        if self.logs == 'y':
                            with open('logs.txt', 'a') as file:
                                file.write('Barcode: {}.'.format(barcode))
                                file.write('Circulation Class: {}.'.format(self.args[0]))
                                file.write('Report Class: {}.'.format(self.args[1]))
                                file.write('Call Number Prefix: {}.'.format(self.args[2]))
                                file.write('Call Number: {}.'.format(self.args[3]))
                                file.write('Physical Location: {}.'.format(self.args[4]))
                                file.write('\n')
                        time.sleep(2)
                    except:
                        break

    def close(self, logs):
        self.logs = logs
        driver.quit()
        if self.logs == 'y':
            with open('logs.txt', 'a') as file:
                file.write('\n')
                file.write('Session Ended.')
                file.write('\n')



# MENU SCRIPT.
intro()
logs = logging()
while 1:
    user = menu()
    if user == '0':
        mode = mode()
        username, password = credentials()

        # LOGIN SCRIPT.
        website = Atriuum(username, password, mode)
        website.open(username, password, logs)

        # EDIT SCRIPT.
        edit, path = edit_options()
        circulation, report, call_prefix, call_number, physical_location = edit_values()
        if edit == '0':
            website.edit_barcodes(edit,logs, circulation, report, call_prefix, call_number, physical_location, path=path)
        elif edit == '1':
            website.edit_barcodes(edit, logs, circulation, report, call_prefix, call_number, physical_location)

        print('\n[+] Finished!')
        user = input('[+] Quit the program (y/n)? ')
        if user == 'y':
            print('[i] Quitting the program...')
            website.close(logs)
            break
        else:
            continue

input()

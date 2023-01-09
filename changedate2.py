from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login():
    df = pd.read_excel('datecorrection2.xlsx', sheet_name='users')  # can also index sheet by name or fetch all sheets
    userlist = df['username'].tolist()
    datelist = df['date'].tolist()


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tecmed.vida24.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("merimna.patras")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("!XZAj_T84TL4")
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="sidebar_patients"]')))
    button.click()
    start = time.time()
    for x in range(len(userlist)):
        print(userlist[x] + "  Start")
        date = str(datelist[x]).replace(' 00:00:00' ,'')
        driver.find_element("xpath", '//input[@class="form-control input-sm"]').send_keys(str(userlist[x]))
        button1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//i[@class="fa fa-fw fa-eye"]')))
        button1.click()
        button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//li[@class="treeview "]/a')))
        button2.click()
        ###########################################################################################################################
        #                                               AROPE - START                                                             #
        ###########################################################################################################################
        button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" AROPE"]')))
        button3.click()
        button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button4.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button5.click()
        button6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button6.click()
        ###########################################################################################################################
        #                                      AROPE - END,   INICIARE  - START                                                   #
        ###########################################################################################################################
        button7 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" INICIARE"]')))
        button7.click()
        button8 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button8.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button9 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button9.click()
        button01 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button01.click()
        ###########################################################################################################################
        #                                  INICIARE - END,  1.KATASTASI UGEIAS   - START                                          #
        ###########################################################################################################################
        button02 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 1.ΚΑΤΑΣΤΑΣΗ ΥΓΕΙΑΣ"]')))
        button02.click()
        button03 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button03.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button04 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button04.click()
        button05 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button05.click()
        ###########################################################################################################################
        #                          1.KATASTASI UGEIAS - END |  2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ - START                             #
        ###########################################################################################################################
        button06 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ"]')))
        button06.click()
        button07 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button07.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button08 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button08.click()
        button09 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button09.click()
        ###########################################################################################################################
        #                          2.ΦΥΣΙΚΟ-ΛΕΙΤΟΥΡΓΙΚΗ ΙΚΑΝΟΤΗΤΑ - END  | 3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ    - START                        #
        ###########################################################################################################################
        button001 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ"]')))
        button001.click()
        button002= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button002.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button003= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button003.click()
        button004= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button004.click()
        ###########################################################################################################################
        #                              3.ΓΝΩΣΤΙΚΗ ΙΚΑΝΟΤΗΤΑ - END  |   4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ   - START                                #
        ###########################################################################################################################
        button005 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ"]')))
        button005.click()
        button006= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button006.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button007= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button007.click()
        button008= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button008.click()
        ###########################################################################################################################
        #             4.ΒΑΣΙΚΕΣ ΑΝΑΓΚΕΣ - END  |   5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ   - START                   #
        ###########################################################################################################################
        button009 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ"]')))
        button009.click()
        button0001= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button0001.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button0002= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button0002.click()
        button0003= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button0003.click()
        ###########################################################################################################################
        # 5.ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΔΙΑΧΕΙΡΙΣΗ ΚΑΙ ΚΟΙΝΩΝΙΚΕΣ ΣΧΕΣΕΙΣ - END  | 6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ   - START  #
        ###########################################################################################################################
        button0004 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ"]')))
        button0004.click()
        button0005= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button0005.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button0006= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button0006.click()
        button0007= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button0007.click()
        ###########################################################################################################################
        #           6.ΙΚΑΝΟΤΗΤΑ ΠΡΟΩΘΗΣΗΣ ΜΙΑΣ ΥΓΙΕΙΝΗΣ ΖΩΗΣ/ΘΑΝΑΤΟΥ - END  | 8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ- START             #
        ###########################################################################################################################
        button0008 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ"]')))
        button0008.click()
        button0009= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button0009.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button0000= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button0000.click()
        button00001= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button00001.click()
        ###########################################################################################################################
        #              8.ΚΟΙΝΩΝΙΚΟ-ΟΙΚΟΝΟΜΙΚΗ ΚΑΤΑΣΤΑΣΗ - END  | 7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ - START                   #
        ###########################################################################################################################
        button00002 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()=" 7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ"]')))
        button00002.click()
        button00003= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//a[text()="Επεξεργασία"]')))
        button00003.click()
        driver.execute_script("$('#date').attr('value',"+str(date)+")")
        button00004= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@class="btn btn-primary pull-right"]')))
        button00004.click()
        button00005= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//button[@id="yesIamSure"]')))
        button00005.click()
        button00006= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="sidebar_patients"]')))
        button00006.click()
        end = time.time()
        print(userlist[x] + "  Done , Time took to run"+str(end - start)+"seconds")
if __name__ == "__main__":
    login()

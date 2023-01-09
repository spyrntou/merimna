from selenium.webdriver.common.by import By
import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def login():
    dateselector = random.choice([13, 14, 21, 22])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://tecmed.vida24.com/")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//input[@id="username"]').send_keys("merimna.patras")
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("!XZAj_T84TL4")
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    driver.find_element(By.XPATH, '//li[@id="sidebar_patients"]').click()
    time.sleep(7)
    driver.find_element("xpath", '//input[@class="form-control input-sm"]').send_keys("GRFBI008530")
    time.sleep(7)
    driver.find_element("xpath", '//i[@class="fa fa-fw fa-eye"]').click()
    time.sleep(7)
    driver.find_element("xpath", '//li[@class="treeview "]/a').click()
    time.sleep(5)
    driver.find_element("xpath", '//a[text()=" AROPE"]').click()
    time.sleep(7)
    driver.find_element("xpath", '//a[text()=" 7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ"]').click()
    time.sleep(7)
    fysiko_leitourgiki_ikanotita_MESSAGE = driver.find_element("xpath", "//div[@class='nav-tabs-custom']")
    if fysiko_leitourgiki_ikanotita_MESSAGE.text == 'Δεν υπάρχουν δεδομένα':
        print("7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ Start")
        driver.find_element("xpath", "//div[@class='box-tools pull-right']").click()
        time.sleep(2)
        driver.execute_script("$('#date').attr('value','2022-12-" + str(dateselector) + "')")

        driver.find_element("xpath", "//input[@name='question[live_alone]' and @value='1']/following-sibling::label").click()
        driver.find_element("xpath", "//input[@name='question[usual_caregivers]' and @value='0']/following-sibling::label").click()

        driver.find_element("xpath", "//button[@class='btn btn-primary pull-right']").click()
        time.sleep(3)
        print("7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ done")
    else:
        print("User contain Data")
        print("7.ΟΙΚΟΓΕΝΕΙΑ, ΣΥΝΤΡΟΦΟΙ ΚΑΙ ΦΡΟΝΤΙΣΤΕΣ done")

    time.sleep(57)
if __name__ == "__main__":
    login()

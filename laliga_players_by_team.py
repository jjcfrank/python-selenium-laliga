from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

def data():
    #Where the file is located
    PATH = "/Applications/chromedriver"

    #Web driver
    driver = webdriver.Chrome(PATH)

    #Website to scrape
    driver.get("https://transfermarkt.co.uk/")

    #Settings
    ##For waiting
    wait = WebDriverWait(driver,10)

    ##For consenting GDPR
    def gdpr():
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[id^='sp_message_iframe']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='ACCEPT ALL']"))).click()
        driver.switch_to.default_content()

    #Search for a team
    selectTeam = "Sevilla FC"
    search = wait.until(EC.element_to_be_clickable((By.NAME, "query")))
    search.send_keys(selectTeam, Keys.RETURN)

    gdpr()

    try:
        sevfclink = wait.until(EC.element_to_be_clickable((By.ID, "368")))
        sevfclink.click()
    except:
        pass

    lsts = driver.find_elements_by_xpath('//*[@id="yw1"]/table/tbody')

    players_list = []

    for lst in lsts:
        lst = driver.find_elements_by_css_selector("tr")
        for value in lst:
            players_list.append(value.text)

    driver.close()

    return players_list

data = data()

date = datetime.now()
fulldate = date.strftime("%d-%b-%Y (%H:%M:%S)")

data.append(fulldate)
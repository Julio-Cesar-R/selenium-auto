import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
import time

#Conxeion a la pagina
driver=webdriver.Edge()
driver.get("https://es.goodbarber.com/create/apps/?gad_source=5&gclid=EAIaIQobChMI3_er2OPBjAMVjVR_AB35WgI8EAAYASAAEgKqG_D_BwE")
#!-------------------------------------------------------------------------
#constantes
conectivity={
"toggle1":"//*[@id='CybotCookiebotDialogBodyLevelButtonPreferences']",
"toggle2":"//*[@id='CybotCookiebotDialogBodyLevelButtonStatistics']",
"toggle3":"//*[@id='CybotCookiebotDialogBodyLevelButtonMarketing']",
}

connection= False
time.sleep(5)
while connection == False:
    verification=[]
    for data in conectivity.values():
        toggle=driver.find_element(By.XPATH,value=data)
        if not toggle.is_selected():
            verification.append(toggle.is_selected())
            toggle.click()
            time.sleep(5)
        else:
            verification.append(toggle.is_selected())
            
    if all(verification):
        connection = True
        print(verification)
    else:
        print("el ciclo conntinua")
        print(verification)
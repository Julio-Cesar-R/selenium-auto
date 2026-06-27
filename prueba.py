import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#Esperar a que aparezca un texto
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.TAG_NAME, "body"),
        "Las cookies de este sitio web se usan para personalizar el contenido y los anuncios, ofrecer funciones de redes sociales y analizar el tráfico. Además, compartimos información sobre el uso que haga del sitio web con nuestros partners de redes sociales, publicidad y análisis web, quienes pueden combinarla con otra información que les haya proporcionado o que hayan recopilado a partir del uso que haya hecho de sus servicios."
    )
)
print("El texto apareció")    
#!------------------------------

#Buscar en un elemento específico
#elemento = driver.find_element(By.ID, "mensaje")
#
#if "correcto" in elemento.text.lower():
#    print("Encontrado")

#!------------------------------    
#Buscar en toda la página
texto_pagina = driver.find_element(By.TAG_NAME, "body").text.lower()

if "Las cookies de este sitio web se usan para personalizar el contenido y los anuncios, ofrecer funciones de redes sociales y analizar el tráfico. Además, compartimos información sobre el uso que haga del sitio web con nuestros partners de redes sociales, publicidad y análisis web, quienes pueden combinarla con otra información que les haya proporcionado o que hayan recopilado a partir del uso que haya hecho de sus servicios." in texto_pagina:
    print("Texto encontrado")
else:
    print("No encontrado")
#!------------------------------
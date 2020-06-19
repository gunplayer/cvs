import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def cargaPagina():
    driver.get("https://www.python.org/")
    logging.info("cargando sitio")

def busquedaCriterio(criterio):
    busqueda = driver.find_element_by_id("id-search-field")
    busqueda.clear()
    busqueda.send_keys(criterio)
    botonBuscar = driver.find_element_by_id("submit")
    botonBuscar.click()
    logging.info("realizar busqueda")

def esperaValidacion(criterio):
    espera = WebDriverWait(driver,10)
    #botonSearch = driver.find_element_by_xpath('//*[@value="Search"]')
    botonSearch = espera.until(EC.element_to_be_clickable((By.XPATH,'//*[@value="Search"]')))
    assert criterio in driver.current_url, "no realizo la busqueda" 

def test_4_2_1():
    logging.info("ejecutando test_4_2_1b")
    cargaPagina()    
    busquedaCriterio("Script")
    esperaValidacion("Script")
    driver.quit()
    
if __name__ == "__main__":
    test_4_2_1()    
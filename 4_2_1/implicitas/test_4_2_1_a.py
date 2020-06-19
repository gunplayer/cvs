import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_4_2_1():
    logging.info("ejecutando test_4_2_1")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.python.org/")
    logging.info("cargando sitio")
    criterio = "Script"
    busqueda = driver.find_element_by_id("id-search-field")
    busqueda.clear()
    busqueda.send_keys(criterio)
    botonBuscar = driver.find_element_by_id("submit")
    botonBuscar.click()
    logging.info("realizar busqueda")
    botonSearch = driver.find_element_by_xpath('//*[@value="Search"]')
    assert criterio in driver.current_url, "no realizo la busqueda"
    driver.quit()
    
if __name__ == "__main__":
    test_4_2_1()    
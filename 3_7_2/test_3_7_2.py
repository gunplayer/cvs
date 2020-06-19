import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_3_7_2():
    driver = webdriver.Chrome()
    logging.info("ejecutando test_3_7_2")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php?controller=prices-drop")
    #encontramos el objeto
    lista = driver.find_element_by_id("selectProductSort")
    lista.click()
    #buscamos la opcion
    opcion = driver.find_element_by_xpath('//option[@value="quantity:desc"]')
    opcion.click()
    assert "quantity" in driver.current_url, "orden seleccionado en lista no aplicado."
    driver.quit
    
if __name__ == "__main__":
    test_3_7_2()  
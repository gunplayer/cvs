import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_3_6_2():
    driver = webdriver.Chrome()
    logging.info("ejecutando test_3_6_2")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    #encontramos el objeto
    login = driver.find_element_by_class_name("login")
    #capturamos su propiedad
    texto_html = login.get_attribute("outerHTML")
    logging.info("outer HTML es: "+texto_html)
    driver.quit()
    
if __name__ == "__main__":
    test_3_6_2()     
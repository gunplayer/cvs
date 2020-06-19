import logging
import time
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()

def capturadepantalla():
    fecha_actual = time.localtime()
    nombrepantalla = "/home/selenium/lab_feb2020/3_3_1_ext/"
    nombrepantalla = nombrepantalla+ str(fecha_actual.tm_mday)+str(fecha_actual.tm_mon)+str(fecha_actual.tm_year)
    nombrepantalla = nombrepantalla+ str(fecha_actual.tm_hour)+str(fecha_actual.tm_min)+str(fecha_actual.tm_sec)+".png"
    logging.info("creando captura de pantalla")
    driver.get_screenshot_as_file(nombrepantalla) 

def test_3_3_1_ext():
    logging.info("ejecutando test_3_3_1_ext")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    marco = driver.find_element_by_id("iframeResult")
    logging.info("cambiando foco a marco")
    driver.switch_to.frame(marco)
    driver.find_element_by_xpath('//button[@onclick="myFunction()"]')
    logging.info("volviendo foco a pantalla")
    driver.switch_to.default_content()
    assert "Tryit Editor" in driver.title, "pagina no correspondiente"
    capturadepantalla()
    driver.quit()
    
if __name__ == "__main__":
    test_3_3_1_ext()    
    
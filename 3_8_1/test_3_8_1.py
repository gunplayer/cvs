import logging
from selenium import webdriver
import time
logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()

def test_3_8_1_ext():
    logging.info("ejecutando test_3_3_1_ext")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    marco = driver.find_element_by_id("iframeResult")
    logging.info("cambiando foco a marco")
    driver.switch_to.frame(marco)
    boton = driver.find_element_by_xpath('//button[@onclick="myFunction()"]')
    logging.info("click en boton")
    boton.click()
    logging.info("cambiando foco a alerta")
    time.sleep(3)
    alerta = driver.switch_to.alert
    mensaje = alerta.text
    assert "Hello! I am an alert box!" in mensaje, "alerta muestra otro mensaje"
    logging.info("cerrado de alerta")    
    alerta.dismiss()
    driver.switch_to.default_content()
    driver.quit()
    
if __name__ == "__main__":
    test_3_8_1()      
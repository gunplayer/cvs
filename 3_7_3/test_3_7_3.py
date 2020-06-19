import logging
import time
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_3_7_3():
    driver = webdriver.Chrome()
    logging.info("ejecutando test_3_7_3")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("http://automationpractice.com")
    #encontramos el objeto
    enlace = driver.find_element_by_xpath('//ul[@id="homefeatured"]//h5/a[@title="Faded Short Sleeve T-shirts"]')
    enlace.click()
    # en detalle de producto seleccionamos el carro
    time.sleep(5)
    boton_carro = driver.find_element_by_xpath('//button[@class="exclusive"]')
    boton_carro.click()
    time.sleep(5)
    #encontramos el modal
    modal = driver.find_element_by_id("layer_cart")
    #buscamos el boton dentro del modal
    boton_checkout = modal.find_element_by_xpath('//a[@title="Proceed to checkout"]')
    boton_checkout.click()
    assert "controller=order" in driver.current_url, "carro de compra no direccionado."
    driver.quit()
    
if __name__ == "__main__":
    test_3_7_3()  
    
    
    
    
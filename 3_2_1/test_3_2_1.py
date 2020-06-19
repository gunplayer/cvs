import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_3_2_1():
    logging.info("ejecutando test_3_2_1")
    driver = webdriver.Chrome()
    driver.get("https://docs.python.org/3/")
    pagina = driver.current_url
    titulo = driver.title
    logging.info ("pagina desplegada: "+pagina)
    logging.info("titulo de pagina desplegada: "+titulo)
    assert "Documentation" in titulo, "pagina no encontrada"
    driver.quit()
    
if __name__ == "__main__":
    test_3_2_1()
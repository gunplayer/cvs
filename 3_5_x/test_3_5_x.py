import logging
from selenium import webdriver 
logging.basicConfig(level=logging.INFO)

def test_3_5_x():
    driver = webdriver.Chrome()
    logging.info("ejecutando test_3_5_x")
    logging.info("maximizando ventana")
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    # 3.5.1 cuadro de busqueda por ID
    busqueda = driver.find_elements_by_id("search_query_top")
    logging.info("se han encontrado :"+str(len(busqueda))+" elementos por id")
    # 3.5.2 iniciar sesion por nombre de clase
    login = driver.find_elements_by_class_name("login")
    logging.info("se han encontrado :"+str(len(login))+" elementos por clase")
    # 3.5.3 elemento h1 por nombre de etiqueta
    cabecera = driver.find_elements_by_tag_name("h1")
    logging.info("se han encontrado :"+str(len(cabecera))+" elementos por etiqueta")
    # 3.5.4 contactenos por texto total y parcial
    enlace1 = driver.find_elements_by_link_text("Contact us")
    logging.info("se han encontrado :"+str(len(enlace1))+" elementos por texto completo")
    enlace2 = driver.find_elements_by_partial_link_text("Contact")
    logging.info("se han encontrado :"+str(len(enlace2))+" elementos por texto parcial")
    # 3.5.5 cuadro de busqueda por xpath
    busquedaX = driver.find_elements_by_xpath('//*[@id="search_query_top"]')
    logging.info("se han encontrado :"+str(len(busquedaX))+" elementos por xpath")
    driver.quit()
    
if __name__ == "__main__":
    test_3_5_x()    
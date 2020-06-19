import logging
import time
logging.basicConfig(level=logging.DEBUG)

def test_3_1():
        logging.debug("ejecutando test_3_1")
        fecha_actual = time.localtime()
        logging.info("fecha actual :"+
                     str(fecha_actual.tm_mday)+"-"+
                     str(fecha_actual.tm_mon)+"-"+
                     str(fecha_actual.tm_year)+" "+
                     str(fecha_actual.tm_hour)+":"+
                     str(fecha_actual.tm_min)+"-"+
                     str(fecha_actual.tm_sec))
        assert fecha_actual.tm_hour > 1,"hora mayor a 1 hrs"
            
if __name__ == "__main__":
    test_3_1()
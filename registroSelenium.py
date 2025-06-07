from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def registro_automatico():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    try:
        
        driver.get("http://127.0.0.1:8000/usuarios/registro")
        time.sleep(2)
        
        datos = {
            'username': 'YinaCalderon1',
            'email': 'YINA123@ejemplo.com',
            'telefono': '3001234444',
            'direccion': 'Calle falsa 123, Bogotá',
            'password1': 'MiContraseña123!',
            'password2': 'MiContraseña123!'
        }
        
        for campo, valor in datos.items():
            elemento = driver.find_element(By.NAME, campo)
            elemento.clear()
            elemento.send_keys(valor)
            time.sleep(0.5)
        
        
        boton_registro = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        boton_registro.click()
        
        time.sleep(40)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    registro_automatico()
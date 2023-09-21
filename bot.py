from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
#Abrir pagina
driver_path = 'C:\chromedriver_win32\chromedriver.exe'

driver = webdriver.Chrome()

driver.get('https://sena.territorio.la/index.php?login=true')
#Iniciar Sesion

time.sleep(3)

login_button = driver.find_element(By.NAME, 'typeDocument')
login_button.click()
#login = WebDriverWait(driver, 10)
finder_button = driver.find_element(By.XPATH, '//*[@id="marcoingreso"]/tbody/tr[3]/td/div')
finder_button.click()

select_button = driver.find_element(By.XPATH, '//*[@id="typeDocument"]/option[2]')
select_button.click()

id_button = driver.find_element(By.XPATH, '//*[@id="document"]')
id_button.send_keys('1094891499')

password = driver.find_element(By.XPATH, '//*[@id="passwd"]')
password.send_keys('10948DEIVIDCALLEJAs')

Join = driver.find_element(By.XPATH, '//*[@id="ingresar"]')
Join.click()
time.sleep(3)

Enter = driver.find_element(By.XPATH, '//*[@id="catalogo-main-content"]/li[1]/div/div[2]/span[1]/div/a')
Enter.click()
time.sleep(3)

Evidencia = driver.find_element(By.XPATH, '//*[@id="aTareas"]')
Evidencia.click()
time.sleep(3)

Date = driver.find_element(By.ID, 'fechaFiltro')
Date.click()
time.sleep(3)

Select_date = driver.find_element(By.XPATH, '//*[@id="fechaFiltro"]/option[2]')
Select_date.click()
time.sleep(3)

Open_Evidencia = driver.find_element(By.XPATH, '//*[@id="tarea[416513569]"]/table/tbody/tr/td[1]/a')
Open_Evidencia.click()
time.sleep(5)

link = driver.find_element(By.XPATH, '//*[@id="divVinculosRespuesta"]/a')
link.click()
link_insert = driver.find_element(By.XPATH, '//*[@id="linktare"]')
link_insert.send_keys('https://github.com/Deiviidcallejas/boot.git')
time.sleep(2)
Send = driver.find_element(By.XPATH, '//*[@id="botonL"]')
Send.click()

time.sleep(3)

Answer = driver.find_element(By.XPATH, '//*[@id="contestarTareaBoton"]')
Answer.click()

time.sleep(15)



#//*[@id="cke_1_contents"]


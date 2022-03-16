import os
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By

dir_path = os.getcwd()
chromedriver = os.path.join(dir_path, "chromedriver.exe")
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.netflix.com/br/login')
nome = driver.find_element(By.ID, 'id_userLoginId')
nome.clear()
# Colocar o ID da conta Netflix
nome.send_keys('')
senha = driver.find_element(By.ID, 'id_password')
senha.clear()
# Colocar o senha da conta Netflix
senha.send_keys('')
senha.send_keys(Keys.RETURN)

sleep(6)
# Selecionar um perfil depois de logar
perfil = driver.find_element(By.XPATH, "(//div[@class='profile-icon'])[1]")
perfil.click()
sleep(5)


driver.get('https://www.netflix.com/browse/genre/1')
# Inicio da verificação de paginas
total = 3444
# Contador de erros
contador = 0

# O final do laço é a quantidade de paginas a serem verficadas
while total < 10000:
    try:
        auxPrint = driver.find_element(By.CLASS_NAME, 'genreTitle').text
        print(str(total) + " - Genero: " + auxPrint)
    except:
        contador += 1

    total += 1
    auxConsulta = 'https://www.netflix.com/browse/genre/' + str(total)
    driver.get(auxConsulta)

sleep(4)
print(str(contador) + " páginas deram errado")
driver.close()

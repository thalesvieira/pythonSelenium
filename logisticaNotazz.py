import email
from  selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
#options.add_argument("--headless")

# Parametros que serão necessários
parameters = {
    'LOGIN': 'caiko11',
    'SENHA': '415236Ca*1',
    'HEADLESS': False
}

if (parameters['HEADLESS']) == True:
      options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=options) # Diretório do driver
link = 'https://app.notazz.com/' # Link do site
driver.get(link)
driver.maximize_window()  # Maximizando a tela



def loginNotazz(driver):

        # Fazendo o login na plataforma
        driver.find_element_by_css_selector('#usuario').send_keys(parameters['LOGIN'])
        driver.find_element_by_name('senha').send_keys(parameters['SENHA'])
        driver.execute_script('document.getElementsByClassName("btn bg-olive btn-block")[0].click()') # Aperta o botão de login

def cadastroTransportadora(driver):

        btn_transportadora = driver.find_element_by_css_selector('fa fa-road') # Clica no menu transportadoras
        time.sleep(1)
        btn_transportadora.click()

def main():

    loginNotazz()
# Importando o Selenium 
from  selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/')
driver.maximize_window()

# Clicar em Carregar mais
driver.execute_script('document.getElementsByClassName("style__LoadMoreButton-sc-1ynvx8h-5")[0].click()')

# Buscando informações da página
h2 = driver.find_elements_by_tag_name('h2')

# Visualizando os títulos 
for c in range(0,len(h2)):
    print(h2[c].text)

#Timeout na Página
time.sleep(10)









# IMPORTANDO O SELENIUM
from socket import timeout
from  selenium import webdriver
import time

# ACESSANDO A PÁGINA
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/')
driver.maximize_window()

# CLICANDO EM CARREGAR MAIS
driver.execute_script('document.getElementsByClassName("style__LoadMoreButton-sc-1ynvx8h-5")[0].click()')

# TIMEOUT PARA CARREGAR OS OUTROS 6 PATCH NOTES
time.sleep(2)

# BUSCANDO AS INFORMAÇÕES DA PÁGINA
h2 = driver.find_elements_by_tag_name('h2')

# PEGANDO O NOME DOS PATCH NOTES
for c in range(0,len(h2)):
    print(h2[c].text)

# FECHANDO A PÁGINA
driver.quit()
    


    #driver.execute_script("window.open('');") #abre uma aba nova
    #driver.switch_to.window(driver.window_handles[c]) #seleciona a aba que foi aberta
    #driver.get('https://www.leagueoflegends.com/pt-br/news/tags/patch-notes/') #Entra na URL de patch notes.
    #Clica em carregar mais
    #driver.execute_script('document.getElementsByClassName("style__Title-sc-1h41bzo-8 fEywOQ")[0].click()') # Clica em algum dos patch notes.

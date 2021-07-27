##### ESTÁ FUNCIONANDO PERFEITAMENTE / DIA 16/06/2021

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# direório para download
dir = "D:\15.1 Mestrado - ATUALIZADO\PYTHON\testes_cap_14\WS_pdf"

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {"download.default_directory": "D:\15.1 Mestrado - ATUALIZADO\PYTHON\testes_cap_14\WS_pdf",    # directory to doownload the files
                                          "download.prompt_for_download": False,    # to auto downaload the file
                                          "download.directory_upgrade": True,
                                          "plugins.always_open_pdf_externally": True    # it will not show PDF directly on chrome
                                          })

# local onde o chromedriver está (precisa baixar o chrome driver e colocar seu arquivo nesse caminho)
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path, options=options)

# url da busca
url = "http://www4.tjrj.jus.br/ejuris/ConsultarJurisprudencia.aspx"
driver.get(url)

# campo de busca
busca = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtTextoPesq")
busca.send_keys("transporte aéreo")
busca.send_keys(Keys.RETURN)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''Demora um tempo até a página com o campo de pesquisa que coloquei ser acessada, para o código não prosseguir antes de essa página ser acessada,
coloca-se esse try, que espera até a página ser localizada. Quando é localizada, ai continua o código.
'''
try:
    result = WebDriverWait(driver, 10).until(                                ## esperar o acesso ao site por até 10 segundos, depois prossegue com o código
        EC.presence_of_element_located((By.ID, "tudo"))                      ## tô procurando o id=tudo no código html da página que resultou das linhas do campo de busca
    )
except:
    driver.quit()
time.sleep(5)       ### esperar 5 segundos para a página ser toda carregada e prosseguir com o código


from selenium.webdriver.support.select import Select        ### para selecionar botoes com lista

for i in range(1,18):
    dropdown_page = driver.find_element_by_id("seletorPaginasTopo")         ### id de onde está a troca de páginas
    page = Select(dropdown_page)
    page.select_by_visible_text(str(i))
    time.sleep(5)

    links = driver.find_elements_by_link_text("Íntegra do Acórdão")             # pega todos os links das íntegras do acórdão (se eu quiser, posso pegar os das decisões monocráticas também)
    print(links)
    for link in links:
        try:
            atual = link.get_attribute('href')          ### pego o link que tem o pdf
            driver.get(atual)
            print('Download completed!')
        except AttributeError as e:
            print(e)
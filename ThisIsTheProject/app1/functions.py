from bs4 import BeautifulSoup
import requests
from .models import WebSiteInfo
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def getNumberPages(): #Get Number of pages
    list1 = []
    NumberPages = []
    counter = 0
    print('\n GETTING AMOUNT OF PAGES...PLEASE WAIT...')
    source = requests.get(f'https://pt.proxyservers.pro/').text
    soup = BeautifulSoup(source, 'lxml')
    pages = soup.find('div', class_='card-footer')
    for object1 in pages.find_all('ul'):
        rows = object1.find_all('a')
        for row in rows:
            list1.append(row.text.split())
            for number in list1:
                NumberPages = number
    NumberPages = int(NumberPages[0])
    print(f'  {NumberPages} Pages Found.')
    return NumberPages

def getStructure(): #Get Main site structure
    pages = getNumberPages()
    print('\n MAKING BLACK MAGIC...PLEASE WAIT...\n')
    list1 = []
    url = 'https://pt.proxyservers.pro/'
    web_r = requests.get(url)
    web_soup = BeautifulSoup(web_r.text, 'html.parser')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    html = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(web_r.text, 'html.parser')     
    
    for pagina in range(0, 1):
        source = requests.get(f'https://pt.proxyservers.pro/proxy/list/order/speed/order_dir/asc/page/{pagina}', timeout=100).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('table', class_='table table-hover')
        for object1 in table.find_all('tbody'):
            rows = object1.find_all('tr', attrs={'valign':'top'})
            for row in rows:
                object2 = row.find_all('td')
                for item in object2:
                    list1.append(item.text.split())
        # list1.pop(25)
    return list1

def formatList(YourList):
    formatedList = [YourList[x:x+8] for x in range(0, len(YourList),8)]
    return formatedList

def do_something(): #Compilado
    list1 = getStructure()
    list2 = formatList(list1)
    # print(f'Lista Normal: {list1} \n')
    # print(f'Lista Formatada: {list2}')
    print('\n SUMMONNING DEMONS AND ANGELS...PLEASE WAIT...\n')            
    for item in list2:
        # print(f'\nitem: {item}')
        for i in range(0,8):
            if len(item[i])==2:
                var1 = item[i][0] + ' ' + item[i][1]
            elif len(item[i])==1:
                var1 = item[i][0]
            else:
                var1 = ''
            # print(f'var1: {var1}')
            if i == 0:
                Atualizado = var1
            elif i == 1:
                IP = var1
            elif i == 2:
                Porto = var1
            elif i == 3:
                Pais = var1
            elif i == 4:
                Velocidade = var1
            elif i == 5:
                Conectados = var1
            elif i == 6:
                Protocolo = var1
            elif i == 7:
                Anonimato = var1
        # print(f'item: {item} \n')
        #Should Return something like this['42', 'min'], ['88.198.50.103'], [], ['Alemanha'], ['10.06', 'sec'], ['2d', '9h'], ['HTTPS'], ['Elite']

        ins = WebSiteInfo(Atualizado=Atualizado,
                   IP=IP, Porto=Porto, Pais=Pais, Velocidade=Velocidade,
                   Conectados=Conectados, Protocolo=Protocolo, Anonimato=Anonimato)
        # print(f'\nAtualizado: {Atualizado} | IP: {IP} | Porto: {Porto} | Pais: {Pais} | Velocidade: {Velocidade} | Conectados: {Conectados} | Protocolo: {Protocolo} | Anonimato: {Anonimato}\n')
        # x = input()
        ins.save()

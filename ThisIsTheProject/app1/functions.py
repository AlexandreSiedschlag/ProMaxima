from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import chromedriver_binary
from .models import WebSiteInfo


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
    print(f'       {NumberPages} Pages Found.')
    return NumberPages


def getStructure(): #Get Main site structure
    pages = getNumberPages()
    print('\n MAKING BLACK MAGIC...PLEASE WAIT...\n')
    list1 = []
    url = 'https://pt.proxyservers.pro/'
    web_r = requests.get(url)
    web_soup = BeautifulSoup(web_r.text, 'html.parser')
    driver = webdriver.Chrome()
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

def do_something(): #Compilado
    list1 = getStructure()
    list2 = formatList(list1)
    print(f'Lista Normal: {list1} \n')
    print(f'Lista Formatada: {list2}')
    print('\n SUMMONNING DEMONS AND ANGELS...PLEASE WAIT...\n')
    for item in list2:
        print(f'item: {item} \n')
        #Should Return this['42', 'min'], ['88.198.50.103'], [], ['Alemanha'], ['10.06', 'sec'], ['2d', '9h'], ['HTTPS'], ['Elite']
        Atualizado = item[0][0]
        IP = item[1][0]
        Porto = 0   
        Pais = item[3][0]
        Velocidade = item[4][0]
        Conectados = item[5][0]
        Protocolo = item[6][0]
        Anonimato = item[7][0]
        ins = WebSiteInfo(Atualizado=Atualizado,
                   IP=IP, Porto=Porto, Pais=Pais, Velocidade=Velocidade,
                   Conectados=Conectados, Protocolo=Protocolo, Anonimato=Anonimato)
        ins.save()
        print(f'\nAtualizado: {Atualizado} | IP: {IP} | Porto: {Porto} | Pais: {Pais} | Velocidade: {Velocidade} | Conectados: {Conectados} | Protocolo: {Protocolo} | Anonimato: {Anonimato}\n')
        # x = input()
        
def formatList(YourList):
    formatedList = [YourList[x:x+8] for x in range(0, len(YourList),8)]
    return formatedList








'''

def getAtualizado(): #Get Valores
    list1 = getStructure()
    if len(list1[0])>0:
        Atualizado = list1[0][0]
    else: 
        return None
    return Atualizado

def getIP():#Get Valores
    list1 = getStructure()
    if len(list1[1])>0:
        Porto = list1[1][0]
    else:
        return None
    return Porto

def getPorto():#Get Valores
    list1 = getStructure()
    if len(list1[2])>0:
        Porto = list1[2][0]
    else:
        return None
    return Porto

def getPais():#Get Valores
    list1 = getStructure()
    Pais = ''
    if len(list1[3])>0:
        for item in list1[3]:
            Pais = str(Pais) + ' ' + str(item)
    else:
        Pais = list1[3][0]
    return Pais

def getVelocidade():#Get Valores
    list1 = getStructure()
    if len(list1[4])>0:
        Porto = list1[4][0]
    else:
        return None
    return Porto

def getConectados():#Get Valores
    list1 = getStructure()
    if len(list1[5])>0:
        Porto = list1[5][0]
    else:
        return None
    return Porto

def getProtocolo():#Get Valores
    list1 = getStructure()
    if len(list1[6])>0:
        Porto = list1[6][0]
    else:
        return None
    return Porto

def getAnonimato():#Get Valores
    list1 = getStructure()
    if len(list1[7])>0:
        Porto = list1[7][0]
    else:
        return None
    return Porto

'''
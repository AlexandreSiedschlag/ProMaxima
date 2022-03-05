# Promaxima_TesteSeletivo :chart_with_upwards_trend:
Entry test for the company Promaxima(Maceio-Brazil)

# What the company asked for :pushpin:
The goal of this challenge is create an aplication that collects, lists, adds, edits and deletes data from DataBase using the requirements below.

## Requirements:shopping_cart:
Django aplication. <br />
Colect data from the main table from https://pt.proxyservers.pro/. <br />
Must use Scrapy or BeautifuSoup for scrap data.<br />
Must collect data from all pages not just the first. <br />
Data must be saved in a SQLite DataBase.<br />
List data collected.<br />
Allow to Add/Edit/Delete itens in this list.<br />
Rows and collums must be similiar to the collected.<br />
Upload your code in a GitHub repo(Public Acess).<br />
Write step-by-step the execution on README.<br />
Simple code(Readable).<br />

## Extra
Docker or Docker-Compose if well documented.<br />
Web Deploy for public acess.<br />

# The Project itself
## Technology used
Python 3.10 (Backend)<br />
Django 4.0 (Project)<br />
SQLite3 (DataBase)<br />
BeautifulSoup 4.10 (Web Scrapping)<br />
Selenium (1)<br />
Chromedriver_binary 99.0 (2)<br />

1 = Selenium was required for this project, because, when you load the page with beautifulsoup, some data is still not completly loaded, so, i made selenium render BeautifulSoup just after the data is completly loaded.<br />
2 = Insted of downlaoding a ChromeDriver, i used this library to do the same job for me.

## How to use(step-by-step)
Clone this repo in your machine.<br />
Open it.<br />
Cd into the project directory, "ThisIsTheProject", or until you find a folder with the file "manage.py" in the same folder. <br />
Run this code, "python manage.py runserver" in CLI, this code SHOULD run a good and stabilized running application. <br />
Run application in local host. Open your Chrome and type http://127.0.0.1:8000/ (Local Host)<br />
On this your are at now, when you click the button, it will do the magic of web scrapping, scrapping the data from the table as required.<br />
What happens next? This data(from the table)  will be saved in a SQLite DataBase and Django will see that and make another magic, showing all of this data in Django's Admin Dashboard, HERE: http://127.0.0.1:8000/admin. <br />
From Django Admin Dashboard you can create/edit/delete any data you want.<br />
And thats complete the project, lest check the acomplished its below.<br />

## Requiremends acomplished
Django aplication. (:heavy_check_mark: done) <br /> 
Colect data from the main table from https://pt.proxyservers.pro/. (:heavy_check_mark: done)<br />
Must use Scrapy or BeautifuSoup for scrap data. (:heavy_check_mark: done)<br />
Must collect data from all pages not just the first. (:heavy_check_mark: done)<br />
Data must be saved in a SQLite DataBase. (:heavy_check_mark: done)<br />
List data collected. (:heavy_check_mark: done)<br />
Allow to Add/Edit/Delete itens in this list. (:heavy_check_mark: done)<br />
Rows and collums must be similiar to the collected. (:heavy_check_mark: done)<br />
Upload your code in a GitHub repo(Public Acess). (:heavy_check_mark: done)<br />
Write step-by-step the execution on README. (:heavy_check_mark: done)<br />
Simple code(Readable). (:heavy_check_mark: done)<br />
   

# ProMaxima
Junior's WebScrapper entry test for the company Promaxima(Maceio-Brazil)

# What the company asked for  :green_circle:
The goal of this challenge is to create an aplication that collects, lists, adds, edits and deletes data from DataBase using the requirements below.

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

## Extra :rocket:
Docker or Docker-Compose if well documented.<br />
Web Deploy for public acess.<br />

# The project itself :green_circle:
## Technologys used :electron:
Python 3.10 (Backend)<br />
Django 4.0 (Project)<br />
SQLite3 (DataBase)<br />
BeautifulSoup 4.10 (Web Scrapping)<br />
Google Chrome <br />
Selenium (1)<br />
Lxml 4.8 <br />
Webdriver-manager 3.5 (2)<br />



1 = Selenium was required for this project, because, when you load the page with beautifulsoup, some data is still not completly loaded, so, i made selenium render BeautifulSoup just after the data is completly loaded.<br />
2 = Instead of downlaoding manually a ChromeDriver, i used this library to do the same job for all Chrome versions.


## How to use(step-by-step) :arrow_forward:
1- Clone this repo in your machine.<br />
2- Open it.<br />
3- Cd into the project directory, "ThisIsTheProject", or until you find a folder with the file "manage.py" in the same folder. <br />
4- Run this code to start the application.<br />
```python manage.py runserver```

5- Open your Chrome and type http://127.0.0.1:8000/ , or just ctrl+click the link in your CLI.<br />
6- Click the button on the web page, it will do the magic of web scrapping, get the data from the table.<br /><br />

What happens next? This data(from the table)  will be saved in a SQLite DataBase called "Info" and Django will see that and show all of this data in Django's Admin Dashboard, HERE: http://127.0.0.1:8000/admin. <br />
```Login: admin , Password: 1234.```<br/>
From Django Admin Dashboard or the Main Page, you can create/edit/delete any data you want.<br />
And that completes the project, let's check the acomplished its below.<br />

## Requirements acomplished :brain:
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

## Extra :rocket:
Docker or Docker-Compose if well documented. :x:<br />
Web Deploy for public acess.(1):x:<br />

1- Changed the Debug mode to False, made the build to Heroku, tryied to deploy, but for some reason i keep getting Error 500 from the deployed page.

## Aditional Info
Note that, some information(like the Port column) from the main table of https://pt.proxyservers.pro/ is JavaScript feeded.
BeautifulSoup cant handle this kind of information feed.
To solve this problem would be necessary run a JavaScript program to collect that data. But by now lets leave it like this.
In resume, if the information of the html is loaded without JavaScript, BeautifulSoup can collect it normally.

# Issues
CSS not working properly, i made the link from settings, django, html and css. But for some reason when i make some changes, its not updating properly. (1)

1- After sometime i found out that my browser's cache was full, so i did Ctrl+F5 to hard refresh and solved the problem. Now Css is working properly

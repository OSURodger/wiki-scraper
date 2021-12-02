"This program will create a web-page about a person using a given HTML request."
"Use http://127.0.0.1:5000/<firstName>/<lastName>"

import requests
from bs4 import BeautifulSoup
from flask import Flask

def urlget(firstName, lastName)->str:

    url= ('https://en.wikipedia.org/wiki/'+ firstName + '_' + lastName)
    return (url)

def createSoup(firstName, lastName)->str:
    
    url=urlget(firstName, lastName)
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, 'html.parser')
    return (soup)

def getContent(soup)->str:

    content = soup.find_all("td", {"class": "infobox-data"})
    
    return (content)

def getTitle(soup)->str:

    title = soup.find_all("th", {"class": "infobox-label"})
    
    return (title)

app = Flask (__name__)

@app.route('/')
def home():
    return "Welcome to the home page. I am working."

@app.route("/<firtName>/<lastName>")
def person(firtName, lastName):
    #return f'Welcome {firtName} {lastName}'

    soup=createSoup(firtName, lastName)
    title=getTitle(soup)
    content=getContent(soup)

    retText= '<body><p>'
    for a, b in zip(title, content):
        #return (a.getText()+', '
        retText += (a.getText()+', '+b.getText()+'<br>')
        #f.write('"'+b.getText()+'"')
        #f.write('\n')
    retText += '</p></body>'
    
    return (retText)

if __name__ == '__main__':
    app.run()


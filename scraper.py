"""
To get this working, input  " pip install "requests" " and
"pip install "requests" " into the comand prompt after
having installed Python.
"""

"""
"Cheap trick to install required modules."
try:
    import requests
except ImportError: 
    os.system ('python -m pip install requests')
try:
    from bs4 import beautifulsoup4
except ImportError: 
    os.system ('python -m pip install beautifulsoup4')
"""

import requests

from bs4 import BeautifulSoup

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

soup=createSoup('Joanne', 'Campbell')

title=getTitle(soup)
content=getContent(soup)

for a, b in zip(title, content):
    print('---')
    print(a.getText(separator=u' '))
    print(b.getText(separator=u' '))
    print('---')

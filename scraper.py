"""
To get this working, input  "pip install "requests"" and
"pip install "requests"", into the comand prompt
after having installed Python.
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


"For demonstration purposes, simply replace these two names with the fristname and last name of the desired person."
"Then, run the program. It will replace the contents of actorBio.csv with the updated infomation."
soup=createSoup('Joanne', 'Campbell')

title=getTitle(soup)
content=getContent(soup)

f = open("actorBio.csv", "w")
f.write("Type, Data\n")
f.close()

f = open("actorBio.csv", "a")
for a, b in zip(title, content):
    f.write(a.getText()+', ')
    f.write('"'+b.getText()+'"')
    f.write('\n')
f.close()


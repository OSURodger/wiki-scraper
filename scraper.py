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

def getHeader(firstName, lastName)->str:

    url=urlget(firstName, lastName)
    
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, 'html.parser')
    title = soup.find(id='firstHeading')
    return (title)

title=getHeader('Lee', 'Aaker')
print (title.string)

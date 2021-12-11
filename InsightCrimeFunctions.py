
#Don't modify for regular usage
#Given an insight crime link with a specific search term and page number, gets all news links from page
#Only use returnLinks function.

#c:\users\cjmes\appdata\local\programs\python\python39\lib\site-packages
import requests
from bs4 import BeautifulSoup as bs
import re

def isInsightCrimeLink(strLink):
    if(strLink.find("facebook") != -1):
        return -1
    elif(strLink.find("linkedin") != -1):
        return -1
    elif(strLink.find("twitter") != -1):
        return -1
    elif(strLink.find("whatsapp") != -1):
        return -1

    return 1

def createSoupObject(url):
    req = requests.get(url)
    soup = bs(req.text, "html.parser")
    return soup

def createListOfLinks(soup):
    construction = []
    for link in soup.find_all('a'):
        strLink = (link.get('href'))
        if (str(type(strLink))) == "<class 'NoneType'>":
            continue
        else:
            if(strLink.find("-") != -1 and isInsightCrimeLink(strLink) != -1 and len(strLink) > 39 and strLink.find("news") != -1):
                construction.append(strLink)
    return construction

def returnLinks(link):
    parseThis = createSoupObject(link)
    return createListOfLinks(parseThis)

    
    
   





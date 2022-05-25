import requests
import lxml.html
from lxml.html import etree


def parse(url):
    res = requests.get(url)
    if res.status_code == 200:

        tree = lxml.html.document_fromstring(res.text)
        titles = tree.xpath("//*[@class='project__name']/text()")
        skills = tree.xpath("//*[@class='circle__title']/text()")
        return titles, skills
    else:
        print(f'connection error: {res.status_code}')

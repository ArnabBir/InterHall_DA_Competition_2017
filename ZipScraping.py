import urllib2
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)

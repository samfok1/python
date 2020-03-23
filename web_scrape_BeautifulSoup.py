import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(final_hn):
	return sorted(final_hn, key=lambda k:k['vote'], reverse=True)

def create_custom_hn(links, subtext):
    hn=[]
    for idx, item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if vote != None:
            try:
                point = int(vote[0].get_text().replace(' points',''))
                if point > 99:
                    hn.append({'title':title, 'href':href, 'vote':point})
            except:
            	continue
    return hn

i=1
final_hn=[] 
while True:
    i=str(i)
    link=[]
    url = "https://news.ycombinator.com/news?p="+i
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.storylink')
    if len(links) == 0:
    	break
    subtext = soup.select('.subtext')
    final_hn += create_custom_hn(links, subtext)
    i=int(i)
    i+=1

pprint.pprint(sort_stories_by_votes(final_hn))

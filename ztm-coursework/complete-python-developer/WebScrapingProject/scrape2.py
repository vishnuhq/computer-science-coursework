import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get("https://news.ycombinator.com/news")
soup1 = BeautifulSoup(res1.text, "html.parser")
links1 = soup1.select(".titleline > a")
subtext1 = soup1.select(".subtext")

res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup2 = BeautifulSoup(res2.text, "html.parser")
links2 = soup2.select(".titleline > a")
subtext2 = soup2.select(".subtext")

all_links = links1 + links2
all_subtexts = subtext1 + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda x: x["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        votes = subtext[idx].select(".score")
        if len(votes):  # if length is not zero
            points = int(votes[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(all_links, all_subtexts))

# FINAL NOTE:
# To learn more about web scraping in python, do these -
#     1) Learn more about BeautifulSoup Library
#     2) Learn about Scrapy FrameWork (https://scrapy.org/)

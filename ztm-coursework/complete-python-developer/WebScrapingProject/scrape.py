import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")


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


pprint.pprint(create_custom_hn(links, subtext))

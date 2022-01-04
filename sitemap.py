import requests
from bs4 import BeautifulSoup
import csv
import re
def main(url):
    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        links = [item.text for item in soup.select("loc")]
        with open("data1.csv", 'w') as f:
            writer = csv.writer(f)
            for link in links:
                r = req.get(link)
                print(link)
                writer.writerow([link])
                soup = BeautifulSoup(r.content, 'html.parser')
                end = [item.text for item in soup.select("loc")].text
                for a in end:
                    r = req.head(a)
                    print(a.text)
                    writer.writerow([a])

main("https://www.linescape.com/sitemap.xml")
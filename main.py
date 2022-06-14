import requests
from bs4 import BeautifulSoup
from datetime import datetime
import lxml
import pandas as pd
import openpyxl


url = "https://www.tradingview.com/markets/stocks-usa/market-movers-high-dividend/"

def connect_1():
    res = []
    koti=[]
    links =[]
    lasti=[]
    epss=[]
    cap = []
    link = "https://tradingview.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    naz = soup.find_all("sup",{"class":"apply-common-tooltip tickerDescription-qN79lDF8"})
    kot = soup.find_all("a",{"class":"apply-common-tooltip tickerName-qN79lDF8"})
    last = soup.find_all("td",{"class":"cell-v9oaRE4W right-v9oaRE4W"})
    for x in range(100):
        res.append("".join(list(naz[x])))
        koti.append("".join(list(kot[x])))
    for a in soup.find_all('a',{"class":"apply-common-tooltip tickerName-qN79lDF8"},href=True):
        post=link + a['href']
        links.append(post)
        post = link
    for bio in links:
        otvet = requests.get(bio)
        back = BeautifulSoup(otvet.content, "html.parser")
        eps = back.find_all("div", {"class": " tv-fundamental-block__value js-symbol-eps "})
        epss.append(eps)
        capital = back.find_all("span", {"class": "tv-widget-fundamentals__value apply-overflow-tooltip"})
        cap.append(capital)
    df = pd.DataFrame({"Company":res,"Kotirovka":koti,"Links":links})
    df.to_excel('./teams.xlsx')
    print(epss)
    print(cap)
    return kot


if __name__ == "__main__":
    print(connect_1())
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import openpyxl
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options,
                          executable_path="C:\\Users\\Иван\\PycharmProjects\\pythonProject1\\chromedriver\\chromedriver.exe")

stealth(
    driver,
    languages=["en-Us", "en"],
    vendor="Google Inc.",
    platform="Win64",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True
)


def get_mvid():
    url = "https://www.mvideo.ru/product-list-page?q=lightning+%D0%BA%D0%B0%D0%B1%D0%B5%D0%BB%D1%8C&category=kabeli-dlya-sotovyh-telefonov-344"
    uri = "https://www.mvideo.ru/product-list-page?q=%D0%BA%D0%B0%D0%B1%D0%B5%D0%BB%D0%B8+usb+type-c&category=344"
    try:
        driver.get(url)
        time.sleep(7)
        resMvideo = []
        soup = BeautifulSoup(driver.page_source, "lxml")
        data = soup.find_all("span", {"class": "price__main-value"})
        for x in range(len(data)):
            resMvideo.append("".join(list(data[x])).replace("\xa0", ""))
        print(resMvideo)

        driver.get(uri)
        time.sleep(7)
        resc=[]
        replit = driver.page_source
        sop = BeautifulSoup(replit, "lxml")
        dat = sop.find_all("span", {"class": "price__main-value"})
        for x in range(len(dat)):
            resc.append("".join(list(dat[x])).replace("\xa0", ""))
        print(resc)
        df = pd.DataFrame({"Mvideo ligthting": resMvideo})
        dt = pd.DataFrame({"Mvideo TYPE c": resc})

        df.to_excel('./mvid.xlsx')


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    print(get_mvid())
    print("a")

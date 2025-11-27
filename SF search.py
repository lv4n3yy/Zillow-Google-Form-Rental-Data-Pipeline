from selenium import webdriver
import requests
import lxml
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

options = Options()
options.add_experimental_option("detach", True)
config = {
    "User-Agent": os.getenv("USER_AGENT"),
    # add more headers if needed
}

print("User-Agent from env:", repr(os.getenv("USER_AGENT")))
print("Headers dict:", config)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

WEBSITE = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55692569140625%2C%22east%22%3A-122.30973330859375%2C%22south%22%3A37.7037516730222%2C%22north%22%3A37.84676307513626%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%7D'
response = requests.get(WEBSITE, headers=config)






soup = BeautifulSoup(response.text, 'lxml')
ads = []
advs = soup.find_all('article', attrs={'role': 'presentation'})
for adv in advs:
    ads.append(adv.find('a')['href'])
for i in range(len(ads)):
    if ads[i][:len(ads[i])-5] != 'https':
        ads[i] = 'https://www.zillow.com' + ads[i]
prices = []
for adv in advs:
    prices.append(adv.find('span').text)
for i in range(len(prices)):
    prices[i] = prices[i][0:6]
print(ads)
print(prices)
titles = []
for adv in advs:
    titles.append(adv.find('a').text)
print(titles)
GOOGLE_URL = os.getenv('GOOGLE_URL')
driver.get(GOOGLE_URL)
for i in range(len(titles)):
    time.sleep(2)
    address_inp = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_inp.send_keys(titles[i])
    time.sleep(0.5)
    prices_inp = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices_inp.send_keys(prices[i])
    time.sleep(0.5)
    ads_inp = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ads_inp.send_keys(ads[i])
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(2)
    for i in range(len(titles)):
        driver.get(GOOGLE_URL)  # always open a fresh blank form
        time.sleep(2)

        address_inp = driver.find_element(By.XPATH,
                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_inp.send_keys(titles[i])

        prices_inp = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        prices_inp.send_keys(prices[i])

        ads_inp = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ads_inp.send_keys(ads[i])

        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        time.sleep(2)


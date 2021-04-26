import bs4
import requests
import os, time, re, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

def Scraper(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(url)        
        soup = bs4.BeautifulSoup(driver.page_source, 'lxml')        
        return soup.text.strip().replace("\n", "")
    except:
        try:
            driver.get("https://"+url)        
            soup = bs4.BeautifulSoup(driver.page_source, 'lxml')            
            return soup.text.strip().replace("\n", "")
        except:
            try:
                driver.get("http://"+url)        
                soup = bs4.BeautifulSoup(driver.page_source, 'lxml')            
                return soup.text.strip().replace("\n", "")
            except:
                return "error happned, url is invalid"

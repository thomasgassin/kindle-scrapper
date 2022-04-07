import webbrowser
import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
import os
# from webdriver_manager.chrome import ChromeDriverManager
# import chromedriver_binary

url_kindle_accueil = "https://www.amazon.com/b?node=154606011"
url_kindle_cat_art_and_photo ="https://www.amazon.com/s?bbn=154606011&rh=n%3A133140011%2Cn%3A154606011%2Cn%3A154607011&dc&qid=1648440703&rnid=154606011&ref=lp_154606011_nr_n_0"
url_kindle_cat_art_and_photo_subcat_music_p1 = "https://www.amazon.com/s?rh=n%3A156302011&fs=true&ref=lp_156302011_sar"
url_kindle_cat_art_and_photo_subcat_umusic_p2 = "https://www.amazon.com/s?i=digital-text&rh=n%3A156302011&fs=true&page=2&qid=1648440846&ref=sr_pg_2"
url_kindle_cat_art_and_photo_subcat_umusic_p3  ="https://www.amazon.com/s?i=digital-text&rh=n%3A156302011&fs=true&page=3&qid=1648440968&ref=sr_pg_3"


from pathlib import Path
from selenium import webdriver
# DRIVER_PATH = str(Path('/usr/local/bin/geckodriver.exe').resolve())
DRIVER_PATH_geckodriver = str(Path('geckodriver.exe').resolve())
DRIVER_PATH_chromedriver = str(Path('chromedriver.exe').resolve())

# print(DRIVER_PATH)
browser_firefox = webdriver.Firefox(executable_path = DRIVER_PATH_geckodriver)
browser_firefox.get(url_kindle_accueil)

browser_chrome = webdriver.Chrome(executable_path= DRIVER_PATH_chromedriver)
browser_chrome.get(url_kindle_accueil)
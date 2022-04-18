from selenium import webdriver
from pathlib import Path

url_kindle_accueil = "https://www.amazon.com/b?node=154606011"

DRIVER_PATH_chromedriver = str(Path('chromedriver').resolve())

browser = webdriver.Chrome(executable_path= DRIVER_PATH_chromedriver)

browser.get(url_kindle_accueil)
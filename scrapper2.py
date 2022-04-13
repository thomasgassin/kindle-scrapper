from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
url_kindle_accueil = "https://www.amazon.com/b?node=154606011"

######## METHODE DE LA 1 ERE VIDEO ###########
DRIVER_PATH_chrome = str(Path('chromedriver.exe').resolve())
print(DRIVER_PATH_chrome)
# path_absolute_chrome= r"\\wsl$\Ubuntu\home\thomas\code\thomasgassin\kindle-scrapper\chromedriver.exe"
# path_windows_chrome = r"C:\Users\Thomas\chromedriver.exe"
# DRIVER_PATH_firefox = str(Path('geckodriver.exe').resolve()) 
# navigateur = webdriver.Firefox(executable_path= DRIVER_PATH_firefox )
# navigateur.get(url_kindle_accueil)

# => ' 'geckodriver.exe' executable may have wrong permissions.'
# pour pallier à cette erreur 

#######################"UTILISATION SERVICE"

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")

#==> erreur  (The process started from chrome location /opt/google/chrome/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
# peut-être on peut modifier l'endroit d'o est executé chrome sur la VM
#################UTILISATION OPTIONS

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

################################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service(DRIVER_PATH_chrome)
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)


# #######################

# DRIVER_PATH_chrome = str(Path('chromedriver.exe').resolve())
# s = Service(r"/home/thomas/code/thomasgassin/kindle-scrapper/chromedriver.exe")
# # print(DRIVER_PATH_chrome)
# driver = webdriver.Chrome(service = s)
# driver.get('http://inventwithpython.com')
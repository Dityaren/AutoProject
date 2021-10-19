from selenium import webdriver
from selenium.webdriver.common.by import By

usernameStr = 'Username123' #masukkan username disini   
passwordStr = 'Password123' #masukkan password disini

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

browser = webdriver.Chrome('chromedriver', chrome_options=options)
browser.get(('https://elearningft.unimed.ac.id/login/index.php'))

username = browser.find_element_by_id('username')
username.send_keys(usernameStr)
password = browser.find_element_by_id('password')
password.send_keys(passwordStr)
chkbox = browser.find_element_by_id('rememberusername')
chkbox.click()
login = browser.find_element_by_id('loginbtn')
login.click()

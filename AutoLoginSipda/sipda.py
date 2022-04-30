import os
import PySimpleGUI as sg
from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By

#PySimpleGUI Theme, login Layout, and warning layout
sg.theme('SandyBeach')
layout = [
	[sg.Text('Tolong masukkan Nim dan Password Sipda Anda')],
	[sg.Text('Nim : ', size =(15, 1)), sg.InputText()],
   	[sg.Text('Password :', size=(15, 1)), sg.InputText('', password_char='*')],
	[sg.Submit('Simpan & Mulai'), sg.Cancel('Batal')]
]
warning = [
    [sg.Text('Nim atau password yang anda masukkan salah!')],
    [sg.Cancel('Oke')]
]

#ChromeDriver configuration
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation", "enable-logging"])

#I added this to remove the annoying warning from my IDE
# because NimVar and PassVar variable isnt defined in local variable
NimVar = NULL
PassVar = NULL

#Load or Create acc.dat
if os.path.exists('./acc.dat') == True:
    exec(open("./acc.dat").read())
else:
    window = sg.Window('Auto Sipda', layout, icon='favicon.ico').read(close=True)
    event, values = window.read()
    if event == 'Batal':
        exit()
    else:
        window.close()
        f = open("acc.dat", "a")
        f.write("NimVar = '"+values[0]+"' \nPassVar = '"+values[1]+"' ")
        f.close()
        exec(open("./acc.dat").read())

#Starting ChromeDriver
driver = webdriver.Chrome('chromedriver', options=options)
driver.get(('https://elearningft.unimed.ac.id/login/index.php'))

#inserting Nim & password
username = driver.find_element(By.ID, "username")
username.send_keys(NimVar)
password = driver.find_element(By.ID, "password")
password.send_keys(PassVar)
login = driver.find_element(By.ID, "loginbtn")
login.click()

#This block of code executed if the previously entered Nim or Pass is incorrect
if(driver.current_url != 'https://elearningft.unimed.ac.id/my/'):
    warning = sg.Window('Auto Sipda', warning, icon='favicon.ico').read(close=True)
    event, values = warning.read()
    driver.quit()
    os.remove("./acc.dat")
    exit()
 
#to prevent it from closing after user logged in
Exit = ""
print("LOGIN BERHASIL, Kamu bisa Mengeluarkan Prompt ini..")
while Exit != "\n":
    a = input()
exit()

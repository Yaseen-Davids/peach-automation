from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
# browser.get("https://peach-website.herokuapp.com/users/register")
browser.get("http://localhost:4040/users/register")

def register():
    username = browser.find_element_by_name('username')
    username.send_keys('selenium-user')

    email = browser.find_element_by_name('email')
    email.send_keys('seleniumtest@gmail.com')

    password = browser.find_element_by_name('password')
    password.send_keys("selenium1")

    confPassword = browser.find_element_by_name('confPassword')
    confPassword.send_keys("selenium1")

    confPassword.submit()
    print("** REGISTER SUCCESSFUL **")

register()

# CLOSE BROWSER
browser.close()
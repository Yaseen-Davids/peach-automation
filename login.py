from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
# browser.get("https://peach-website.herokuapp.com/users/login")
browser.get("http://localhost:4040/users/login")

# LOGIN
def login():
    # ENTER USERNAME
    username = browser.find_element_by_name('username')
    username.send_keys('selenium-user')
    # ENTER PASSWORD
    password = browser.find_element_by_name('password')
    password.send_keys("pass12")
    # ATTEMPT LOGIN
    password.submit()
    print("** LOGIN SUCCESSFUL **")

login()

# CLOSE BROWSER
browser.close()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options)
# browser.get("https://peach-website.herokuapp.com/users/login")
browser.get("http://localhost:4040/users/login")


# ************* LOGIN *************
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
    addNewMerchant()
    time.sleep(2)
    editMerchant()
    time.sleep(1)
    deleteMerchant()
    time.sleep(1)
    logout()


# ************* ADD NEW MERCHANT *************
def addNewMerchant():
    # CLICK ADD NEW MERCHANT BUTTON
    browser.find_element_by_class_name("merchant_btn").click()
    # ENTER MERCHANT NAME
    merchantName = browser.find_element_by_name("name")
    merchantName.send_keys("Test Merchant")
    # SELECT OPTION
    merchantSandbox = Select (browser.find_element_by_name("sandbox"))
    merchantSandbox.select_by_visible_text("Yes")
     # SELECT OPTION
    merchantDocs = Select (browser.find_element_by_name("documents"))
    merchantDocs.select_by_visible_text("Yes")
    # SELECT OPTION
    merchantContract = Select (browser.find_element_by_name("contract"))
    merchantContract.select_by_visible_text("No")
    # ENTER MERCHANT UPDATE
    merchantUpdate = browser.find_element_by_name("update")
    merchantUpdate.send_keys("Just a test")
    # SUBMIT NEW MERCHANT
    submit = browser.find_elements_by_class_name("button_calendar")
    for submitBtn in submit:
        if submitBtn.is_displayed():
            submitBtn.click()
            print("** MERCHANT ADDED SUCCESSFUL **")
            return


# ************* REMOVE MERCHANT *************
def deleteMerchant():
    browser.find_element_by_class_name("delete_merchant").click()
    delete_merchant = browser.find_elements_by_id("delete_button")
    for deleteBtn in delete_merchant:
        if deleteBtn.is_displayed():
            deleteBtn.click()
            print("** MERCHANT REMOVED SUCCESSFUL **")
            return


# ************* EDIT MERCHANT *************
def editMerchant():
    browser.find_element_by_class_name("edit_merchant").click()
    time.sleep(1)
    merchantName = browser.find_element_by_id("merchant_name")
    merchantName.clear()
    merchantName.send_keys("Edit Merchant")
    # SELECT OPTION
    merchantSandbox = Select (browser.find_element_by_id("merchant_sandbox"))
    merchantSandbox.select_by_visible_text("Yes")
    # SELECT OPTION
    merchantDocs = Select (browser.find_element_by_id("merchant_documents"))
    merchantDocs.select_by_visible_text("No")
    # SELECT OPTION
    merchantContract = Select (browser.find_element_by_id("merchant_contract"))
    merchantContract.select_by_visible_text("Yes")
    # ENTER MERCHANT UPDATE
    merchantUpdate = browser.find_element_by_id("merchant_update")
    merchantUpdate.clear()
    merchantUpdate.send_keys("Edited")
    # SUBMIT NEW MERCHANT
    submit = browser.find_elements_by_class_name("button_calendar")
    for submitBtn in submit:
        if submitBtn.is_displayed():
            submitBtn.click()
            print("** MERCHANT UPDATED SUCCESSFUL **")
            return

# ***************  LOGOUT ***************
def logout():
    # CLICK LOGOUT ICON
    browser.find_element_by_class_name("profile_btn").click()
    # LOGOUT
    browser.find_element_by_class_name("fa-sign-out-alt").click()
    print("** LOGOUT SUCCESSFUL **")

login()

print(" -- Operation Complete --")
browser.close()
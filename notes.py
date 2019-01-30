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
    addTask()
    time.sleep(1)
    completeTask()
    time.sleep(1)
    uncompleteTask()
    time.sleep(1)
    editTask()
    time.sleep(1)
    completeTask()
    time.sleep(1)
    removeTask()
    time.sleep(1)
    logout()


# *************** ADD TASK ***************
def addTask():
    # ADD TASK BUTTON
    browser.find_element_by_class_name("notes_btn ").click()
    # INPUT TASK NAME
    newNote = browser.find_element_by_name("note")
    newNote.send_keys("Selenium test")
    # INPUT TASK IMPORTANCE
    importance = Select (browser.find_element_by_name("importance"))
    importance.select_by_visible_text("Normal")
    # SUBMIT NEW TASK
    browser.find_element_by_class_name("button_calendar").click()
    # logout()
    print("** ADD TASK SUCCESSFUL **")


# *************** COMPLETE TASK ***************
def completeTask():
    complete = browser.find_elements_by_class_name("note_check ")
    if complete != []:
        complete[0].click()
        print("** TASK COMPLETED SUCCESSFUL **")
    else:
        print("No Tasks Found")


# *************** UNCOMPLETE TASK ***************
def uncompleteTask():
    uncomplete = browser.find_elements_by_class_name("note_complete ")
    if uncomplete != []:
        uncomplete[0].click()
        print("** TASK UNCOMPLETED SUCCESSFUL **")
    else:
        print("No Tasks Found")


# *************** REMOVE TASK ***************
def removeTask():
    note_complete = browser.find_elements_by_class_name("note_complete")[0]

    if note_complete != []:
        deleteBtn = browser.find_elements_by_class_name("delete_note")
        confirmDelete = browser.find_element_by_id("delete_button")
        for delete_button in deleteBtn:
            if delete_button.is_displayed():
                delete_button.click()
                confirmDelete.click()
                print("** REMOVE TASK SUCCESSFUL **")
                return
    else:
        print("No Tasks Found")


# *************** EDIT TASK ***************
def editTask():
    # ADD TASK BUTTON
    edit_button = browser.find_elements_by_class_name("notes_notes ")[0]
    if edit_button != []:
        edit_button.click()
        # INPUT TASK NAME
        time.sleep(1)
        editNote = browser.find_element_by_id("note_edit")
        editNote.clear()
        editNote.send_keys("Selenium edited")
        # INPUT TASK IMPORTANCE
        editImportance = Select (browser.find_element_by_id("note_importance"))
        editImportance.select_by_visible_text("None")
        # SUBMIT NEW TASK
        submitBtn = browser.find_elements_by_class_name("button_calendar")
        # CHECK IF SUBMIT BUTTON IS VISIBLE
        for button in submitBtn:
            if button.is_displayed():
                button.click()
                print("** EDIT TASK SUCCESSFUL **")
                return
    else:
        print("No Task Found")


# ***************  LOGOUT ***************
def logout():
    # CLICK LOGOUT ICON
    browser.find_element_by_class_name("profile_btn").click()
    # LOGOUT
    browser.find_element_by_class_name("fa-sign-out-alt").click()
    print("** LOGOUT SUCCESSFUL **")


login()

print("-- Operation Complete --")
browser.close()
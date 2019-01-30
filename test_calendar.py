from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    browser.find_element_by_link_text("Calendar").click()
    print("** REDIRECT CALENDAR SUCCESSFUL **")
    addCalendarDate()
    time.sleep(1)
    openCalendarOptions()
    time.sleep(1)
    editCalendarDate()
    time.sleep(1)
    openCalendarOptions()
    time.sleep(1)
    removeCalendarDate()
    time.sleep(1)
    logout()


def addCalendarDate():
    addDate = browser.find_element_by_class_name("add_new_date")
    time.sleep(2)

    if addDate.is_displayed():
        addDate.click()
        # ENTER CALENDAR USERNAME
        calendarUsername = browser.find_element_by_name("username")
        calendarUsername.send_keys("Calendar test")
        # ENTER REASON FOR LEAVE
        calenderReason = browser.find_element_by_name("title")
        calenderReason.send_keys("Selenium test")
        # ENTER START DATE
        startDate = browser.find_element_by_name("startDate")
        startDate.send_keys("0020190110")
        # ENTER END DATE
        endDate = browser.find_element_by_name("endDate")
        endDate.send_keys("0020190130")
        # ENTER COLOR
        submit = browser.find_elements_by_class_name("button_calendar")
        for button in submit:
            if button.is_displayed():
                button.click()
                print("** CALENDAR DATE ADDED SUCCESSFUL **")
                return


def openCalendarOptions():
    theCalendar = browser.find_element_by_id("calendar")
    if theCalendar.is_displayed():
        time.sleep(1)
        theDate = browser.find_elements_by_class_name("fc-title")[4]
        theDate.click()
        print("** CALENDAR OPTIONS OPEN SUCCESSFUL **")


def removeCalendarDate():
    deleteBtn = browser.find_element_by_class_name("modal_delete_btn")
    if deleteBtn.is_displayed():
        deleteBtn.click()
        print("** CALENDAR DATE DELETE SUCCESSFUL **")
        return
    

def editCalendarDate():
    editBtn = browser.find_element_by_class_name("modal_edit_btn")
    if editBtn.is_displayed():
        editBtn.click()
        time.sleep(1)
        # ENTER CALENDAR USERNAME
        calendarUsername = browser.find_element_by_name("edit_fullname")
        calendarUsername.clear()
        time.sleep(1)
        calendarUsername.send_keys("Calendar edited")
        # ENTER REASON FOR LEAVE
        calenderReason = browser.find_element_by_name("edit_leave")
        calenderReason.clear()
        time.sleep(1)
        calenderReason.send_keys("Selenium edited")
        # ENTER START DATE
        startDate = browser.find_element_by_name("edit_startdate")
        startDate.clear()
        time.sleep(1)
        startDate.send_keys("0020190115")
        # ENTER END DATE
        endDate = browser.find_element_by_name("edit_enddate")
        endDate.clear()
        time.sleep(1)
        endDate.send_keys("0020190125")
        # ENTER COLOR
        submit = browser.find_elements_by_class_name("button_calendar")
        for button in submit:
            if button.is_displayed():
                button.click()
                print("** CALENDAR DATE EDITED SUCCESSFUL **")
                return

    else:
        addCalendarDate()
    

# ***************  LOGOUT ***************
def logout():
    time.sleep(2)
    # CLICK LOGOUT ICON
    profile = browser.find_element_by_class_name("profile_btn")
    if profile.is_displayed():
        profile.click()
        # LOGOUT
        browser.find_element_by_class_name("fa-sign-out-alt").click()
        print("** LOGOUT SUCCESSFUL **")
        browser.close()
    
    

login()
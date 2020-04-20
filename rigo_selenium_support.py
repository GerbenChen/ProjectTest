import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import logfile
from selenium.common.exceptions import NoSuchElementException
username = ""
password = ""
browser = webdriver.Remote(
            command_executor='',
            desired_capabilities=DesiredCapabilities.CHROME)
browser.maximize_window()


#browser = webdriver.Chrome()
#browser.maximize_window()

def login_url(browser, url):
    try:
        browser.get(url)
        browser.implicitly_wait(10)
        logfile.print_logfile("Open Browser PASS, Session ID = " + browser.session_id)
    except:
        assert False, logfile.print_logfile("Open Browser FAIL")

def login_account_by_id(browser, account_value, string):
    try:
        browser.find_element_by_id("account").clear()
        browser.find_element_by_id("account").send_keys("%s" % username)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def login_account_by_name(browser, account_value, string):
    try:
        browser.find_element_by_name("account").clear()
        browser.find_element_by_name("account").send_keys("%s" % username)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def login_account_by_xpath(browser, account_value, string):
    try:
        browser.find_element_by_xpath("account").clear()
        browser.find_element_by_xpath("account").send_keys("%s" % username)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def login_password_by_id(browser, password_value, string):
    try:
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys("%s" % password)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)


def login_password_by_name(browser, password_value, string):
    try:
        browser.find_element_by_name("password").clear()
        browser.find_element_by_name("password").send_keys("%s" % password)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def login_password_by_xpath(browser, password_value, string):
    try:
        browser.find_element_by_xpath("password").clear()
        browser.find_element_by_xpath("password").send_keys("%s" % password)
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def submit_xpath(browser, xpath, string):
    try:
        browser.find_element_by_xpath("//button[@type='submit']").click()
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)


def isElements_by_id(browser,value, string):
    element = browser.find_elements_by_id(value)
    if element == []:
        assert False, logfile.print_logfile("Check Element : %s FAIL" % string)
    else:
        logfile.print_logfile("Check Element : %s PASS" % string)


def isElements_by_name(browser, value, string):
    element = browser.find_elements_by_name(value)
    if element == []:
        assert False, logfile.print_logfile("Check Element : %s FAIL" % string)
    else:
        logfile.print_logfile("Check Element : %s PASS" % string)


def isElements_by_xpath(browser, value, string):
    element = browser.find_elements_by_xpath(value)
    if element == []:
        assert False, logfile.print_logfile("Check Element : %s FAIL" % string)
    else:
        logfile.print_logfile("Check Element : %s PASS" % string)

def click_button_by_id(browser, value, string):
    try:
        element = browser.find_elements_by_id(value).click()
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def click_button_by_name(browser, value, string):
    try:
        element = browser.find_elements_by_name(value).click()
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def click_button_by_xpath(browser, value, string):
    try:
        element = browser.find_elements_by_xpath(value).click()
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)

def click_button_by_link_text(browser, value, string):
    try:
        element = browser.find_element_by_link_text(value).click()
        logfile.print_logfile("Click Button : %s PASS" % string)
    except:
        assert False, logfile.print_logfile("Click Button : %s FAIL" % string)


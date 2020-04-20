import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re,os,time
import logfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Remote(
            command_executor='',
            desired_capabilities=DesiredCapabilities.CHROME)
browser.maximize_window()

url = ""
#browser = webdriver.Chrome()
#browser.maximize_window()
try:
    browser.get(url)
    browser.implicitly_wait(10)
    logfile.print_logfile("Open Browser PASS, Session ID = " + browser.session_id)
except:
    browser.quit()
    assert False, logfile.print_logfile("Open Browser FAIL")

browser.find_element_by_name("account").clear()
browser.find_element_by_name("account").send_keys("")
browser.find_element_by_name("password").click()
browser.find_element_by_name("password").clear()
browser.find_element_by_name("password").send_keys("")
browser.find_element_by_xpath("//button[@type='submit']").click()
browser.find_element_by_link_text("Driver").click()
browser.implicitly_wait(10)


def postman_on_web(url,method):
    postman_url = ""
    browser.get(postman_url)
    browser.implicitly_wait(10)
    browser.find_element_by_name("url").click()
    browser.find_element_by_name("url").clear()
    browser.find_element_by_name("url").send_keys(url)
    browser.find_element_by_xpath("//div/div/label").click()
    browser.find_element_by_xpath(method).click()
    js="var q=document.documentElement.scrollTop=3000"
    browser.execute_script(js)
    browser.find_element_by_xpath("//button[@type='submit']").click()
    while True:
        try:
            time.sleep(5)
            browser.find_element_by_xpath("(//button[@type='button'])[2]").click()
            time.sleep(5)
            break
        except:
            print "Click Close Fail"

def check_sms_content(url,text):
    browser.get(url)
    browser.implicitly_wait(10)
    browser.find_elements_by_partial_link_text(text)

def driver_get_last_account():
    browser.find_element_by_link_text("Driver").click()
    driver_id = browser.find_element_by_xpath("//td[2]/span")
    driver_id = driver_id.text
    logfile.print_logfile(driver_id)
    return driver_id

def create_driver_account(index,mobile_num):
    while True:
        try:
            time.sleep(5)
            browser.find_element_by_xpath("//div/div/button").click()
            time.sleep(5)
            break
        except:
            print "Click Create Fail"

    browser.find_element_by_name("password").click()
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys("0000")
    browser.find_element_by_name("passwordconfirm").click()
    browser.find_element_by_name("passwordconfirm").clear()
    browser.find_element_by_name("passwordconfirm").send_keys("0000")
    browser.find_element_by_name("displayName").click()
    browser.find_element_by_name("displayName").clear()
    browser.find_element_by_name("displayName").send_keys("gold_flow_%s" % index)
    browser.find_element_by_xpath("//div[5]/div/div/div/label").click()
    browser.find_element_by_xpath("//li[76]/span").click()
    browser.find_element_by_xpath("//div[7]/div/div/div/label/input").click()
    browser.find_element_by_xpath("//div[7]/div/div/div/label/input").click()
    browser.find_element_by_xpath("//div[7]/div/div/div/ul/li[8]/span").click()
    browser.find_element_by_name("birthday").click()
    browser.find_element_by_name("birthday").clear()
    browser.find_element_by_name("birthday").send_keys("002020-01-01")
    browser.find_element_by_name("remark").click()
    browser.find_element_by_name("remark").clear()
    browser.find_element_by_name("remark").send_keys("1")
    browser.find_element_by_name("permanentAddr").click()
    browser.find_element_by_name("permanentAddr").clear()
    browser.find_element_by_name("permanentAddr").send_keys("1")
    browser.find_element_by_name("residentialAddr").click()
    browser.find_element_by_name("residentialAddr").clear()
    browser.find_element_by_name("residentialAddr").send_keys("1")
    browser.find_element_by_name("telNo").click()
    browser.find_element_by_name("telNo").clear()
    browser.find_element_by_name("telNo").send_keys("%s" % mobile_num)
    browser.find_element_by_name("mobileNo").click()
    browser.find_element_by_name("mobileNo").clear()
    browser.find_element_by_name("mobileNo").send_keys("%s" % mobile_num)
    js="var q=document.documentElement.scrollTop=600"
    browser.execute_script(js)
    browser.find_element_by_name("picture").send_keys("C:\images.jpg")
    browser.find_element_by_name("ssNo").click()
    browser.find_element_by_name("ssNo").clear()
    browser.find_element_by_name("ssNo").send_keys("1")
    browser.find_element_by_name("driverLicenseNo").click()
    browser.find_element_by_name("driverLicenseNo").clear()
    browser.find_element_by_name("driverLicenseNo").send_keys("1")
    browser.find_element_by_name("driverLicenseType").click()
    browser.find_element_by_name("driverLicenseType").clear()
    browser.find_element_by_name("driverLicenseType").send_keys("1")
    browser.find_element_by_name("driverLicenseAvailable").click()
    browser.find_element_by_name("driverLicenseAvailable").clear()
    browser.find_element_by_name("driverLicenseAvailable").send_keys("002020-01-01")
    browser.find_element_by_name("BCRNo").click()
    browser.find_element_by_name("BCRNo").clear()
    browser.find_element_by_name("BCRNo").send_keys("1")
    browser.find_element_by_name("BCRAvailable").click()
    browser.find_element_by_name("BCRAvailable").clear()
    browser.find_element_by_name("BCRAvailable").send_keys("002020-01-01")
    browser.find_element_by_name("contractNo").click()
    browser.find_element_by_name("contractNo").clear()
    browser.find_element_by_name("contractNo").send_keys("1")
    if index == "6" or "7" or "8":
        bankInfo1CodeIFSC = ""
    else:
        bankInfo1CodeIFSC = "11111111111"
    browser.find_element_by_name("bankInfo1CodeIFSC").click()
    browser.find_element_by_name("bankInfo1CodeIFSC").clear()
    browser.find_element_by_name("bankInfo1CodeIFSC").send_keys("%s" % bankInfo1CodeIFSC)
    browser.find_element_by_name("bankInfo1AccountName").click()
    browser.find_element_by_name("bankInfo1AccountName").clear()
    browser.find_element_by_name("bankInfo1AccountName").send_keys("")
    browser.find_element_by_name("bankInfo1AccountNo").click()
    browser.find_element_by_name("bankInfo1AccountNo").clear()
    browser.find_element_by_name("bankInfo1AccountNo").send_keys("")
    browser.find_element_by_name("bankInfo2Email").click()
    browser.find_element_by_name("bankInfo2Email").clear()
    browser.find_element_by_name("bankInfo2Email").send_keys("")
    browser.find_element_by_name("bankInfo2MobileNo").click()
    browser.find_element_by_name("bankInfo2MobileNo").clear()
    browser.find_element_by_name("bankInfo2MobileNo").send_keys("%s" % mobile_num)
    while True:
        try:
            time.sleep(5)
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(5)
            break
        except:
            logfile.print_logfile("Click Submit Fail")
    while True:
        try:
            browser.find_element_by_xpath("(//button[@type='button'])[15]").click()
            time.sleep(3)
            break
        except:
            logfile.print_logfile("Click Close Fail")
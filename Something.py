import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    cas = driver.find_element_by_css_selector
    driver.get("http://ivanka/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(1)").click()
    cas("#box-apps-menu li:nth-child(1)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(2)").click()
    cas("#box-apps-menu li:nth-child(2)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(3)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(4)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(5)").click()
    cas("#box-apps-menu li:nth-child(5)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(6)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(7)").click()
    cas("#box-apps-menu li:nth-child(7)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(8)").click()
    cas("#box-apps-menu li:nth-child(8)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(9)").click()
    cas("#box-apps-menu li:nth-child(9)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(10)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(11)").click()
    cas("#box-apps-menu li:nth-child(11)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(12)").click()
    cas("#box-apps-menu li:nth-child(12)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(13)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(14)").click()
    cas("#box-apps-menu li:nth-child(14)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(15)").click()
    cas("#box-apps-menu li:nth-child(15)> ul").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(16)").click()
    driver.get("http://ivanka/admin")
    cas("#box-apps-menu li:nth-child(17)").click()
    cas("#box-apps-menu li:nth-child(17)> ul").click()
    return cas

def are_elements_present(driver, h1):
    driver.get("http://ivanka/admin")
    wd = webdriver.Chrome()
    wd.find_elements_by_css_selector("ul#box-apps-menu > h1")




















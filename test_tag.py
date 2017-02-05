import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://ivanka/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://ivanka/admin/")
    elem = driver.find_elements_by_tag_name("h1")
    print(elem)
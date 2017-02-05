import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd)
    request.addfinalizer(wd.quit)
    return wd

def test_sticker(driver):
    driver.get("http://ivanka/en/")
    try:
        driver.find_element_by_css_selector("#sticker")
        return True
    except NoSuchElementException:
        return False





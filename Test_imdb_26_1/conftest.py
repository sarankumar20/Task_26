import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_imdb_26_1.data import test_source


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(test_source.Values().url)
    request.cls.driver = driver
    yield
    driver.close()
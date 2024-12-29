import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

def setup_function():
    global driver
    # Setup WebDriver
    path = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=path)
    driver.implicitly_wait(20)
    driver.get("https://www.coursera.org/?authMode=login")
    driver.maximize_window()
def teardown_function():
    driver.quit()
def my_cred():
    return [
        ('python16@gmail.com', 'python@123'),
        ('selenium19@gmail.com', 'sel@123'),
        ('pytsel@gmail.com', 'pytsel@123')
    ]
@pytest.mark.parametrize("username, password", my_cred())
def test_login(username, password):
    print("My pytest Login")
    driver.find_element(By.NAME, 'email').send_keys(username)
    time.sleep(10)
    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(10)
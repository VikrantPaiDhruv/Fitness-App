import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8501/")
    yield driver
    driver.quit()

def test_valid_login(driver):
    try:
        email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@aria-label=":blue[E-mail]"]'))
    )
        email_input.send_keys("test@gmail.com")  
        password_input = driver.find_element(By.XPATH, '//input[@aria-label=":blue[Password]"]')
        password_input.send_keys("12345") 
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="activity-visualization"]'))
    )
        assert element.is_displayed()


    except Exception as e:
        pytest.fail(f"An error occurred during login: {e}")

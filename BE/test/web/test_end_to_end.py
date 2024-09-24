import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from assertpy import assert_that


@pytest.fixture(scope="module")
def driver():
    # Setup Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_register_new_user(driver):
    try:
        driver.get("http://localhost:8080")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))).send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "confirm_password").send_keys("password")
        driver.find_element(By.NAME, "register").click()
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "success"))).text
        assert_that(success_message).contains("Registration successful")
    except Exception as e:
        print(f"Exception in test_register_new_user: {e}")
        raise


def test_calculation_methods(driver):
    try:
        driver.get("http://localhost:8080")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "username"))).send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "login").click()

        # Add
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "num1"))).send_keys("5")
        driver.find_element(By.NAME, "num2").send_keys("3")
        driver.find_element(By.NAME, "add").click()
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))).text
        assert_that(result).is_equal_to("8")

        # Subtract
        driver.find_element(By.NAME, "num1").clear()
        driver.find_element(By.NAME, "num2").clear()
        driver.find_element(By.NAME, "num1").send_keys("5")
        driver.find_element(By.NAME, "num2").send_keys("3")
        driver.find_element(By.NAME, "subtract").click()
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))).text
        assert_that(result).is_equal_to("2")

        # Multiply
        driver.find_element(By.NAME, "num1").clear()
        driver.find_element(By.NAME, "num2").clear()
        driver.find_element(By.NAME, "num1").send_keys("5")
        driver.find_element(By.NAME, "num2").send_keys("3")
        driver.find_element(By.NAME, "multiply").click()
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))).text
        assert_that(result).is_equal_to("15")

        # Divide
        driver.find_element(By.NAME, "num1").clear()
        driver.find_element(By.NAME, "num2").clear()
        driver.find_element(By.NAME, "num1").send_keys("6")
        driver.find_element(By.NAME, "num2").send_keys("3")
        driver.find_element(By.NAME, "divide").click()
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "result"))).text
        assert_that(result).is_equal_to("2")
    except Exception as e:
        print(f"Exception in test_calculation_methods: {e}")
        raise


def test_history_feature(driver):
    try:
        driver.get("http://localhost:8080")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.NAME, "username"))).send_keys("testuser")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "login").click()

        # Perform calculations
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "num1"))).send_keys("5")
        driver.find_element(By.NAME, "num2").send_keys("3")
        driver.find_element(By.NAME, "add").click()
        driver.find_element(By.NAME, "num1").clear()
        driver.find_element(By.NAME, "num2").clear()
        driver.find_element(By.NAME, "num1").send_keys("6")
        driver.find_element(By.NAME, "num2").send_keys("2")
        driver.find_element(By.NAME, "subtract").click()

        # Open history
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "history"))).click()
        history = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "history-list"))).text
        assert_that(history).contains("5 + 3 = 8")
        assert_that(history).contains("6 - 2 = 4")
    except Exception as e:
        print(f"Exception in test_history_feature: {e}")
        raise

from behave import *
from selenium.webdriver.common.by import By
import time


@given('que o site carregou')
def abre_home_page(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[1]")
    time.sleep(3)


@then('o logo da Orange deve aparecer')
def verifica_logo(context):
    status = context.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/img").is_displayed()
    assert status is True

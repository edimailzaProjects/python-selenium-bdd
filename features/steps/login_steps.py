from features.support.pages.login_page import LoginPage
from behave import *
from selenium.webdriver.common.by import By
import time

@when('insiro meu login "{usuario}" e senha "{senha}"')
def loga_conta(context, usuario, senha):
    time.sleep(3)

    context.driver.find_element(By.NAME, "username").send_keys(usuario)
    context.driver.find_element(By.NAME, "password").send_keys(senha)
    context.driver.find_element(By.XPATH,
                                "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(3)

@then('eu serei direcionado para a página de dashboard')
def exibe_dashboard(context):
    esperado = "Dashboard"
    obtido = context.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    assert esperado == obtido

@then('posso me desconectar')
def sair(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
    time.sleep(3)

@then('eu não serei conectado com sucesso')
def exibe_credenciais_invalidas(context):
    esperado = "Invalid credentials"
    obtido = context.driver.find_element(By.XPATH, "// *[ @ id = \"app\"] / div[1] / div / div[1] / div / div[2] / div[2] / div / div[1] / div[1] / p").text
    context.driver.save_screenshot('log/screenie.png')
    assert esperado == obtido

def after_scenario(context):
    context.driver.quit()
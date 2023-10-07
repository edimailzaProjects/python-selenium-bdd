from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def loga_conta(self, usuario, senha):
        self.driver.find_element(By.NAME, "username").send_keys(usuario)
        self.driver.find_element(By.NAME, "password").send_keys(senha)
        self.driver.find_element(By.XPATH,
                                    "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)

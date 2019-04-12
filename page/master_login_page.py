from selenium.webdriver.common.by import By
from common.page import Page


class MasterLoginPage(Page):
    login_user_input = (By.ID, 'username')
    login_passw_input = (By.ID, 'password')
    login_sumbit_button = (By.TAG_NAME, 'button')

    def login(self, user, passw):
        self.find_element(*self.login_user_input).send_keys(user)
        self.find_element(*self.login_passw_input).send_keys(passw)
        buttons = self.find_elements(*self.login_sumbit_button)
        for i in buttons:
            if i.text == '登 录':
                i.click()
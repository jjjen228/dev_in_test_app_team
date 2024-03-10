from .page import Page

class LoginPage(Page):
    AUTH_BUTTON_XPATH = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Авторизоваться"]'
    EMAIL_XPATH = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    PASSWORD_XPATH = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    
    def tap_auth_button(self):
        self.click_element(self.AUTH_BUTTON_XPATH)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_XPATH, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_XPATH, password)

    def tap_login_button(self):
        self.click_element(self.AUTH_BUTTON_XPATH)

    def is_logged_in(self):
        success_element = self.find_element('com.ajaxsystems:id/menuDrawer')
        return bool(success_element)

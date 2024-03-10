from .page import Page
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SideBarPage(Page):
    MENU_BUTTON_XPATH = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
    SETTINGS_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Настройки приложения"]'
    HELP_TEXTVIEW_XPATH = '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Помощь"]'

    def open_sidebar(self):
        logger.info("открываем боковую панель")
        self.click_element(self.MENU_BUTTON_XPATH)

    def verify_sidebar_element_sett(self):
        logger.info(f"проверяем наличие элемента в боковой панели: {self.SETTINGS_TEXTVIEW_XPATH}")
        element = self.find_element(self.SETTINGS_TEXTVIEW_XPATH)
        if element:
            logger.info('настройки на месте')
        else:
            logger.info('настройки НЕ на месте')
        return element.is_displayed()
    
    def verify_sidebar_element_help(self):
        logger.info(f"проверяем наличие элемента в боковой панели: {self.HELP_TEXTVIEW_XPATH}")
        element = self.find_element(self.HELP_TEXTVIEW_XPATH)
        if element:
            logger.info('помощь на месте')
        else:
            logger.info('помощь НЕ на месте')
        return element.is_displayed()


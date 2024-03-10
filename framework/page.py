from appium.webdriver.common.touch_action import TouchAction
import time
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        logger.info(f"поиск элемента с локатором: {locator}")
        return self.driver.find_element_by_xpath(locator)

    def click_element(self, locator):
        logger.info(f"клик по элементу с локатором: {locator}")
        element = self.find_element(locator)
        element.click()
        time.sleep(2)

    def tap_coordinates(self, x, y):
        logger.info(f"нажатие по координатам: x={x}, y={y}")
        actions = TouchAction(self.driver)
        actions.tap(x=x, y=y).perform()
        time.sleep(2)

    def send_keys(self, locator, keys):
        logger.info(f"ввод текста '{keys}' в элемент с локатором: {locator}")
        element = self.find_element(locator)
        element.send_keys(keys)
        time.sleep(1)



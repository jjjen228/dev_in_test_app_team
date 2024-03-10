import logging
import subprocess
import time

import pytest
from appium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from utils.android_utils import android_get_desired_capabilities

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture(scope='session')
def run_appium_server():
    logger.info("запуск сервера appium")
    try:
        subprocess.Popen(
            ['appium', '-a', '127.0.0.1', '-p', '4723', '--allow-insecure', 'adb_shell'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            shell=True
        )
        time.sleep(5)
        logger.info("сервер Appium запущен")
    except Exception as e:
        logger.error(f"ошибка при запуске сервера Appium: {e}")
        raise

@pytest.fixture(scope='session')
def driver(run_appium_server):
    desired_caps = android_get_desired_capabilities()
    logger.info(f"инициализация драйвера с capabilities: {desired_caps}")
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info("драйвер успешно создан")
    except Exception as e:
        logger.error(f"не удалось создать сессию драйвера: {e}")
        raise
    yield driver
    driver.quit()

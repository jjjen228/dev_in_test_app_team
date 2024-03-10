import pytest

from framework.sidebar import SideBarPage


@pytest.fixture(scope='function')
def sidebar_page_fixture(driver):
    yield SideBarPage(driver)
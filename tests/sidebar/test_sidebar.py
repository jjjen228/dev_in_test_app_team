import time
import pytest

def test_sidebar_elements(sidebar_page_fixture):
    time.sleep(10)
    side_check = sidebar_page_fixture
    side_check.open_sidebar()
    time.sleep(2)

    side_check.verify_sidebar_element_help()
    side_check.verify_sidebar_element_sett()

    

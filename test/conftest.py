import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope= 'class')
def init__driver(request):



    appium_service = AppiumService()
    appium_service.start(args=['-p 4723'])



    cap: Dict[str, Any] = {

        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.ebay.mobile',
        'appActivity': '.home.impl.main.MainActivity'

    }

    url = 'http://localhost:4723'

    web_driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    wait = WebDriverWait(web_driver, 20)

    wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Close'))).click()

    request.cls.driver = web_driver

    yield
    web_driver.quit()
    appium_service.stop()





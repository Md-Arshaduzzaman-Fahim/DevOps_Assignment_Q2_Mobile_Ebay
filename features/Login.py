from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self,driver):
        self.driver = driver



    def login(self, uname, passwd):
        wait = WebDriverWait(self.driver, 20)

        self.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.ebay.mobile:id/navigation_bar_item_icon_view"])[2]').click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Sign in"]'))).click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Use email or username"]'))).click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Email or username"]'))).send_keys(uname)
        self.driver.find_element(AppiumBy.XPATH, value='//android.widget.EditText[@text="Password"]').send_keys(passwd)
        self.driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Sign in"]').click()
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Skip for now"]'))).click()
        user_name = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="automte-0"]'))).get_attribute("text")

        return user_name


    def is_messege_button(self):

        return self.driver.find_element(AppiumBy.XPATH,value='//android.widget.ImageView[@content-desc="Messages"]')




    def my_ebay_options(self):
        wait = WebDriverWait(self.driver, 20)
        el = wait.until(EC.visibility_of_all_elements_located((AppiumBy.XPATH,
                                                               '(//android.widget.TextView[@text="My eBay"])[2]/following-sibling::android.view.View/android.widget.TextView')))



        print(len(el))
        return len(el)









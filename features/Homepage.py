from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home:
    def __init__(self,driver):
        self.driver = driver



    def ebay_icon_displayed(self):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="eBay"]'))).is_displayed()


    def cart(self):
        return self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Cart button"]').is_displayed()


    def register_button(self):
        return self.driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ebay.mobile:id/button_register"]').is_displayed()




    def login_button(self):
        return self.driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ebay.mobile:id/button_sign_in"]').is_displayed()


    def search_tags(self):
        wait = WebDriverWait(self.driver, 20)
        i = 0
        li = []
        lis = wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,
                                                              '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/recyclerview_items"])[1]/android.widget.Button')))
        for n in lis:
            li.append(n.get_attribute("text"))
        while i < 4:
            wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         'new UiScrollable(new UiSelector().resourceId("com.ebay.mobile:id/recyclerview_items").instance(0)).setAsHorizontalList().scrollToEnd(1)')))

            lis.clear()
            lis = wait.until(EC.presence_of_all_elements_located((AppiumBy.XPATH,
                                                                  '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/recyclerview_items"])[1]/android.widget.Button')))

            for n in lis:
                li.append(n.get_attribute("text"))

            i += 1

        li = list(dict.fromkeys(li))

        print(li)

        return li



    def seach_tag_click(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.Button[@content-desc="Watches"]'))).click()

        return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@text="Luxury Watches"]'))).is_displayed()



    def brand_names(self):
        wait = WebDriverWait(self.driver, 20)
        lis = wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,
                                                                 '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/recyclerview_items"])[1]/android.widget.Button')))
        li = []

        for i in lis:
            li.append(i.get_attribute("text"))


        print(li)

        return li
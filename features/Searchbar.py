from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search:
    def __init__(self,driver):
        self.driver = driver



    def get_search_text_item(self):
        wait = WebDriverWait(self.driver, 20)

        self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@content-desc="Search Keyword Search on eBay"]').click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.AutoCompleteTextView[@resource-id="com.ebay.mobile:id/search_src_text"]'))).send_keys("shoe")

        el = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ebay.mobile:id/search_suggestion_text"][1]')))

        print(el.get_attribute('text'))

        return el.get_attribute('text')



    def sort_button_check(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/search_suggestion_text"][1]'))).click()
        wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                                     "When you save a search, we'll let you know when a new item is listed double tap to dismiss"))).click()

        return self.driver.find_element(AppiumBy.XPATH,
                                        value='//android.widget.Button[@resource-id="com.ebay.mobile:id/button_sort"]').is_displayed()

    def sort_options(self):
        wait = WebDriverWait(self.driver, 20)
        self.driver.find_element(AppiumBy.XPATH,
                                 value='//android.widget.Button[@resource-id="com.ebay.mobile:id/button_sort"]').click()

        lis = wait.until(EC.visibility_of_all_elements_located((AppiumBy.XPATH,
                                                                '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/search_result_refine_panel_fragment_xp_recyclerview"]/android.view.ViewGroup/android.widget.TextView')))

        li = []

        for i in lis:
            li.append(i.get_attribute("text"))

        print(li)

        return li

    def buying_format_options(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/search_textview_filter_title" and @text="Lowest Price + Shipping"]'))).click()

        wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Filter"]'))).click()

        els = wait.until(EC.visibility_of_all_elements_located((AppiumBy.XPATH,
                                                                '(//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/recyclerview_items"])[2]/android.widget.Button')))
        el = []

        for n in els:
            el.append(n.get_attribute("text"))

        print(el)

        return el

    def condition_options(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/title" and @text="Condition"]'))).click()

        lis2 = wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,
                                                                 '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/search_result_refine_panel_fragment_xp_recyclerview"]/android.view.ViewGroup/android.widget.TextView[@resource-id="com.ebay.mobile:id/text_title"]')))
        li2 = []
        for x in lis2:
            li2.append(x.get_attribute("text"))

        print(li2)
        return li2

    def category_options(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="com.ebay.mobile:id/checkbox"])[4]'))).click()

        self.driver.find_element(AppiumBy.XPATH,
                                 value='//android.widget.ImageButton[@content-desc="Back to all refinements"]').click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/title" and @text="Category"]'))).click()

        lis3 = wait.until(EC.visibility_of_any_elements_located((AppiumBy.XPATH,
                                                                 '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.ebay.mobile:id/search_result_refine_panel_fragment_xp_recyclerview"]/android.widget.RadioButton')))
        li3 = []
        for y in lis3:
            li3.append(y.get_attribute("text"))

        print(li3)
        return li3




    def filtered_items(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(
            (AppiumBy.XPATH, '//android.widget.RadioButton[@text="Sporting Goods"]'))).click()

        self.driver.find_element(AppiumBy.XPATH,
                                 value='//android.widget.ImageButton[@content-desc="Back to all refinements"]').click()

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.Button[@resource-id="com.ebay.mobile:id/call_to_action_button"]'))).click()

        return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/textview_header_0" and @text="Men\'s Nike Golf Shoes White, Black & Brown , Size 11"]'))).is_displayed()



    def search_success(self):
        wait = WebDriverWait(self.driver, 20)

        wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,
                                                     '//android.widget.TextView[@resource-id="com.ebay.mobile:id/textview_header_0" and @text="Men\'s Nike Golf Shoes White, Black & Brown , Size 11"]'))).click()

        return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="com.ebay.mobile:id/imageview_image"]'))).is_displayed()

import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestingMobileApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_wifi_settings(self):
        # #Rozwiązanie 1
        # self.driver.find_element_by_accessibility_id("Preference").click()
        # self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().checkable(true)').click()  # zmiana na zaznaczony
        # self.driver.back()
        # self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().checkable(true)').click()

        #Rozwiązanie 2
        self.driver.find_element_by_accessibility_id("Preference").click()
        self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        checkboxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        amount_of_checkboxes = len(checkboxes)

        # dydaktycznie printy:
        print("Liczba checkboxow: ")
        print(amount_of_checkboxes)

        # pętla po checkboxach, która zaznacza wszystkie checkboxy

        for el in checkboxes:
            el.click()

        for el in checkboxes:
            is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")
            if is_checked_value == 'true':
                print("Wszystkie checkboxy są zaznaczone")

        # 4.

        # self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()  zamiast tego ja mam to poniżej:

        is_enabled = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].get_attribute("enabled")
        print(is_enabled)
        if is_enabled == "true":


            password_input = "1,2,3,4"
            self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
            self.driver.find_element_by_class_name("android.widget.EditText").send_keys(password_input)
            # password_ = self.driver.find_element_by_class_name("android.widget.EditText")

            passwordCurrent = self.driver.find_element_by_class_name("android.widget.EditText").text

            print(type(passwordCurrent))
            print(passwordCurrent)
            print(type(password_input))
            print(password_input)

            if password_input == passwordCurrent:
                print("IF hasło wpisane jest prawidłowe")

            self.assertEqual(passwordCurrent, password_input)



            # print(password.text)
            sleep(4)

            # kliknij ok
            self.driver.find_element_by_id("android:id/button1").click()
            self.driver.back()
            self.driver.back()

        # asercja

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)





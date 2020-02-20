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
        desired_caps['unicodeKeyboard'] = True
        desired_caps["resetKeyboard"] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_simple_actions1(self):
        #     self.driver.find_element_by_accessibility_id("Graphics").click()
        #     self.driver.find_element_by_accessibility_id("Arcs").click()
        #     el= self.driver.find_elements_by_android_uiautomator("new UiSelector().text('Graphics/Arcs')")
        #     self.assertIsNotNone(el)
        #
        #     self.driver.back()

        def test_simple_actions2(self):
            self.driver.find_element_by_accessibility_id("Graphics").click()
            sleep(5)
            # element = self.driver.find_element_by_accessibility_id("App")
            # sleep(3)
            # self.assertIsNotNone(element)

            elements = self.driver.find_elements_by_android_uiautomator("new UiSelector().enabled(true)")
            print("Liczba elementow")
            print(len(elements))

            self.assertGreaterEqual()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
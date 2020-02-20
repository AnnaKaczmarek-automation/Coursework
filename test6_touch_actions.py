import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

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

    def test_touch_actions(self):
        el = self.driver.find_element_by_accessibility_id("Views")

        action = TouchAction(self.driver)
        action.tap(el).perform()
        sleep(3)

        self.driver.find_element_by_accessibility_id("Expandable Lists").click()
        self.driver.find_element_by_accessibility_id("1. Custom Adapter").click()
        element1 = self.driver.find_element_by_xpath("//android.widget.TextView[@text=\"People Names\"]")
        action.long_press(element1).perform()
        sleep(3)
        self.driver.find_element_by_class_name("android.widget.TextView").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
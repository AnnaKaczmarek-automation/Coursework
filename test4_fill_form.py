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
        desired_caps['app'] = PATH('ContactManager.apk')  # nazwa folderu z aplikacją, który jest skopiowany na komputer i zapisany w folderze z testem
        desired_caps['appPackage'] = 'com.example.android.contactmanager '
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps["resetKeyboard"] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contact(self):
        self.driver.find_element_by_id("com.example.android.contactmanager:id/addContactButton").click()
        sleep(2)
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Ania")
        textfields[1].send_keys("563820125")
        textfields[2].send_keys("aniaAnia@gmail.com")

        sleep(1)

        # dydaktycznie
        print(textfields[0].text)
        print(textfields[1].text)
        print(textfields[2].text)

        self.assertEqual(textfields[0].text, "Ania")
        self.assertEqual(textfields[1].text, "563820125")
        self.assertEqual(textfields[2].text, "aniaAnia@gmail.com")

        self.driver.find_elements_by_class_name("android.widget.Button")

   

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)

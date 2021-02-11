from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

# Create your tests here.

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:\Program Files')

        @classmethod
        def tearDownClass(cls):
            cls.selenium.quit()
            super().tearDownClass()

        def test_login(self):
            # ログインページを開く
            self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

            # ログイン
            username_input = self.selenium.find_element_by_name("login")
            username_input.send_keys('test@test.com')
            password_input = self.selenium.find_element_by_name("password")
            password_input.send_keys('test0000')
            seld.selenium.find_element_by_class_name('btn').click()

            # ページタイトルの検証
            self.assertEquals('睡眠管理アプリケーション | Private Sleepin', self.selenium.title)
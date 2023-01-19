import time

from appium import webdriver
from day03.pageobjects.login_page import LoginPage


class TestLogin():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "6.0.1",
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.netease.cloudmusic",
        "appActivity": "module.login.LoginActivity",
        "automationName": "UiAutomator1",
        "newCommandTimeout":"6000",
        "noReset": True
    }

    # 2、appium server 进行启动

    # 3、发送指令给到appium server
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # 登录页面=base层属性及行为+当前页面类定义的属性及行为

    def test_login(self):
        login_page = LoginPage(driver=self.driver)
        login_page.in_login()
        login_page.login("abc@163.com","abc")


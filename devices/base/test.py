import time

from appium import webdriver

from base.peiwang import A

class TestLogin():
    desired_caps={
        "platformName":"Android",
        "platformVersion":"11",
        "deviceName":"eqe6begabacmingi",
        "appPackage":"com.xiaomi.smarthome",
        "appActivity":"com.xiaomi.smarthome.SmartHomeMainActivity",
        "automationName":"UiAutomator2",
        "noReset":True
    }

    driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    #driver.implicitly_wait(20)
    #点击进入设备

    def test_peiwang(self):
        P = A(driver=self.driver)
        P.piliang_linhuo()
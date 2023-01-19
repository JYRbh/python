from appium import webdriver

#1、设置终端参数项
from selenium.webdriver.common.by import By

desired_caps={
    "platformName":"Android",
    "platformVersion":"6.0.1",
    "deviceName":"127.0.0.1:7555",
    "appPackage":"com.tuya.smart.ble",
    "appActivity":"com.tuya.smart.activity.MainActivity",
    "automationName":"UiAutomator1",
    "noReset":True
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

window_size=driver.get_window_size()

print("手机屏幕尺寸：",window_size)
x=window_size["width"]
y=window_size["height"]


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

#2、appium server 进行启动

#3、发送指令给到appium server
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#元素定位方法：通过resourceid
el_botton=driver.find_element(By.ID,"android:id/button1").click()

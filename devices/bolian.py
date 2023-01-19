from appium import webdriver

#1、设置终端参数项
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps={
    "platformName":"Android",
    "platformVersion":"11",
    "deviceName":"eqe6begabacmingi",
    "appPackage":"com.tuya.smartiot",
    "appActivity":"com.tuya.smart.hometab.activity.FamilyHomeActivity",
    "automationName":"UiAutomator2",
    "noReset":True
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#driver.implicitly_wait(20)
#light = driver.find_element(MobileBy.ID,"com.xiaomi.smarthome:id/eb1").click()


# for x in range(10000):
#     # WebDriverWait(driver, 20, 1).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='开启']").click())
#     # WebDriverWait(driver,20,1).until(lambda x:x.find_element(MobileBy.XPATH,"//*[@text='关闭']").click())
#
#     switch = driver.find_element(MobileBy.XPATH,"//*[@text='关闭']").click()
#     switch2 = driver.find_element(MobileBy.XPATH,"//*[@text='开启']").click()
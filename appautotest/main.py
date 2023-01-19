# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from selenium.webdriver.common.by import By

from appium import webdriver

#1、设置终端参数项
from selenium.webdriver.common.by import By

user_name="aaaa"
user_key="bbbb"

desired_caps={
    "platformName":"Android",
    "platformVersion":"6.0.1",
    "deviceName":"127.0.0.1:7555",
    "appPackage":"com.netease.cloudmusic",
    "appActivity":"module.login.LoginActivity",
    "automationName":"UiAutomator1",
    "noReset":True
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#勾选协议
driver.find_element(By.ID,"com.netease.cloudmusic:id/agreeCheckbox").click()

#转入邮箱登录界面
driver.find_element(By.ID,"com.netease.cloudmusic:id/mail").click()

#账号密码登录
driver.find_element(By.ID,"com.netease.cloudmusic:id/email").send_keys(user_name)
driver.find_element(By.ID,"com.netease.cloudmusic:id/password").send_keys(user_key)




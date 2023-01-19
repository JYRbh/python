from day03.base.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class LoginPage(BasePage):

    #用户协议勾选
    elm_xieyi=(MobileBy.ID,"com.netease.cloudmusic:id/agreeCheckbox")

    #登录方式选择
    elm_wy=(MobileBy.ID,"com.netease.cloudmusic:id/mail")

    #用户名&密码元素定位
    elm_username=(MobileBy.ID,"com.netease.cloudmusic:id/email")
    elm_userkey=(MobileBy.ID,"com.netease.cloudmusic:id/password")

    #登录按键
    elm_login=(MobileBy.ID,"com.netease.cloudmusic:id/login")

    def in_login(self):

        self.click(self.elm_xieyi)
        self.click(self.elm_wy)


    def login(self,username,userkey):

        self.input(self.elm_username,username)
        self.input(self.elm_userkey,userkey)

        self.click(self.elm_login)


import time

from appium.webdriver.common.mobileby import MobileBy

from base.base_page import BasePage


class A(BasePage):
    def peiwang(self):
        #self.click((MobileBy.XPATH,'//*[@text="设备"]'))

        for i in range(100):
            self.press_botton((MobileBy.ID,'com.xiaomi.smarthome:id/ad2'))

            #点击删除
            self.click((MobileBy.ID,'com.xiaomi.smarthome:id/r_'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/tb"]'))

            self.driver.implicitly_wait(40)

            #重新配网
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/g0"]'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/g7"]'))
            self.click((MobileBy.XPATH,'//*[@text="米家LED灯泡 蓝牙MESH版"]'))

            # # #配网完成
            self.click((MobileBy.XPATH,"//*[@text='电工测试']"))
            self.click((MobileBy.ID,"com.xiaomi.smarthome:id/d73"))
            time.sleep(2)
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/au3"]'))
            time.sleep(2)
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/c5p"]'))
            time.sleep(2)
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/au3"]'))


            # #tongyi
            self.click((MobileBy.XPATH,"//*[@resource-id='com.xiaomi.smarthome:id/h0']"))
            self.click((MobileBy.XPATH,'//*[@content-desc="返回"]'))
            print(i)

    def piliang(self):

        self.click((MobileBy.XPATH, '//*[@text="设备"]'))

        for i in range(100):
            self.press_botton((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[5]'))

            # 点击删除
            self.click((MobileBy.XPATH, '//*[@text="删除设备"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/td"]'))

            self.driver.implicitly_wait(40)
            time.sleep(10)
            # 重新配网
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/g0"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/g7"]'))
            time.sleep(5)
            self.click((MobileBy.XPATH, '//*[@text="米家LED灯泡 蓝牙MESH版"]'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/fu"]'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/c11"]'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/fu"]'))
            

            # # #配网完成
            time.sleep(40)
            self.click((MobileBy.ID,'com.xiaomi.smarthome:id/c6e'))
            self.click((MobileBy.XPATH, '//*[@text="卧室"]'))
            self.click((MobileBy.ID, "com.xiaomi.smarthome:id/d84"))
            time.sleep(2)
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/c6e"]'))
            time.sleep(2)

            print(i)

    def piliang_linhuo(self):

        self.click((MobileBy.XPATH, '//*[@text="设备"]'))

        for i in range(100):
            self.press_botton((MobileBy.XPATH,
                               '//*[@resource-id="com.xiaomi.smarthome:id/cn2"] / android.view.ViewGroup[1]'))
            self.click((MobileBy.XPATH,
                        '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]'))
            self.click((MobileBy.XPATH,
                        '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[4]'))
            self.click((MobileBy.XPATH,
                        '//*[@resource-id="com.xiaomi.smarthome:id/egz"]/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]'))

            # 点击删除
            self.click((MobileBy.XPATH, '//*[@text="删除设备"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/td"]'))

            self.driver.implicitly_wait(40)
            time.sleep(10)
            # 重新配网
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/g0"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/g7"]'))
            time.sleep(5)
            self.click((MobileBy.XPATH, '//*[@text="小米智能开关（三开 零火版）"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/fu"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/c11"]'))
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/fu"]'))

            # # #配网完成
            time.sleep(40)
            self.click((MobileBy.ID, 'com.xiaomi.smarthome:id/c6e'))
            self.click((MobileBy.XPATH, '//*[@text="电工测试"]'))
            self.click((MobileBy.ID, "com.xiaomi.smarthome:id/d84"))
            time.sleep(2)
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/c6e"]'))
            time.sleep(2)

            print(i)

    def peiwang(self):
        #self.click((MobileBy.XPATH,'//*[@text="设备"]'))

        for i in range(100):
            self.press_botton((MobileBy.ID,'com.xiaomi.smarthome:id/ad2'))

            #点击删除
            self.click((MobileBy.ID,'com.xiaomi.smarthome:id/r_'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/tb"]'))

            self.driver.implicitly_wait(40)

            #重新配网
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/g0"]'))
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/g7"]'))
            self.click((MobileBy.XPATH,'//*[@text="米家LED灯泡 蓝牙MESH版"]'))

            # # #配网完成
            self.click((MobileBy.XPATH,"//*[@text='电工测试']"))
            self.click((MobileBy.ID,"com.xiaomi.smarthome:id/d73"))
            time.sleep(2)
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/au3"]'))
            time.sleep(2)
            self.click((MobileBy.XPATH,'//*[@resource-id="com.xiaomi.smarthome:id/c5p"]'))
            time.sleep(2)
            self.click((MobileBy.XPATH, '//*[@resource-id="com.xiaomi.smarthome:id/au3"]'))


            # #tongyi
            self.click((MobileBy.XPATH,"//*[@resource-id='com.xiaomi.smarthome:id/h0']"))
            self.click((MobileBy.XPATH,'//*[@content-desc="返回"]'))
            print(i)

    def Connect(self):
        self.click()

        self.driver.implicitly_wait(40)
        self.driver.find_element_by_xpath("")


class Tuya():
    pass
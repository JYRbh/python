from appium.webdriver.common.touch_action import TouchAction


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    #元素定位
    def locator(self,loc):
        #loc = (MobileBy.ID,"resourceid值")
        return self.driver.find_element(*loc)

    #输入
    def input(self,loc,value):
        self.locator(loc).send_keys(value)

    #按键
    def click(self,loc):
        self.locator(loc).click()

    #滑动
    def swipe(self,start_x,start_y,end_x,end_y):
        window_size=self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        self.driver.swipe(start_x = x*start_x,
                          start_y = y*start_y,
                          end_x = x*end_x,
                          end_y = y*end_y,
                          duration=1000)

    # 长按设备
    def press_botton(self,loc):
        el = self.driver.find_element(*loc)
        TouchAction(self.driver).long_press(el).perform()

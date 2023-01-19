#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

url="https://developer.tuya.com/cn/docs/iot/introduction-of-iot?id=K914jiv4b9y5x"

header = {


}


option =  webdriver.ChromeOptions()
option.add_experimental_option("detach",True)





def login():
    driver.find_element(By.XPATH,"//*[@id='__ty_protal_header__']/div[4]/div[3]/div[2]/div").click()  #点击进入登陆界面

    driver.find_element(By.ID,'username').click()
    driver.find_element(By.ID,'username').send_keys('18857762061')

    driver.find_element(By.ID,'passwd').click()
    driver.find_element(By.ID,'passwd').send_keys('jyr.19990722')

    driver.find_element(By.ID,'check').click()
    driver.find_element(By.CSS_SELECTOR,'button.ant-btn').click()


if __name__ == '__main__':

    #login()
        #cookies_iot = driver.get_cookies()
    #print('获取所有cookie:', cookies_iot)
    driver = webdriver.Chrome(options=option)
    driver.add_cookie([{'domain': 'auth.tuya.com', 'expiry': 1701431023, 'httpOnly': False, 'name': 'gt_user_id',
                        'path': '/', 'secure': False, 'value': 'afcb0dd0-713c-11ed-9204-1faa944661f4'}])

    driver.get(url)
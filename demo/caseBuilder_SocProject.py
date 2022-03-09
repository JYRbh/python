# -*- coding: utf-8 -*-
import xlrd, xlsxwriter

class TestProject:
    def __init__(self):
        self.title = [u"标题*", u"目录层级", u"前置条件", u"步骤描述", u"期望结果", u"标签", u"优先级", u"关联需求编号", u"备注"]
        self.column = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.proLine = u"SOC方案"
        self.product = u"宠物喂食器"
        self.funcList = [u"DP校验", u"主页界面", "产测校验", "升级校验", "配网校验", "引脚校验", "首页界面", "数据界面", "设置界面", "其他", "UED校验"]
        self.pages = [u"首页", u"数据", u"设置"]
        self.lineW = 1
        self.xlsxInit()
        self.caseTitle_init()

    def comWrite(self, row, col, contentDate):
        if col in [6,]:
            self.worksheetW1.write(row, col, contentDate, self.comFormat_Mid)
        else:
            self.worksheetW1.write(row, col, contentDate, self.comFormat_left)

    def xlsxInit(self):
        self.workbookR = xlrd.open_workbook(self.product + u"引脚配置.xlsx")
        self.workbookW = xlsxwriter.Workbook(self.product + u"测试用例.xlsx")
        self.worksheetW1 = self.workbookW.add_worksheet(u"SoC测试")

    def xlsxClose(self):
        self.workbookR.close()
        self.workbookW.close()

    def connector(self, *key, constr="-"):
        return constr.join(key)

    def loadCaselist(self):
        # 根据sheet索引或者名称获取sheet内容
        sheet = self.workbookR.sheet_by_index(0)
        print("Start to load the fixed case")
        self.writeFixedCase()
        print("Finished to load the fixed case")

        print("Start to create the case of pinConfig")
        for i in range(sheet.nrows):
            self.writePinConfigCase(sheet.row_values(i))
        self.writePinErgodicCase()
        print("Finished to load the case of pinConfig")
        self.workbookW.close()

    def writeFixedCase(self):
        # 产测校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "产测校验", "固件烧录测试"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[2], constr="|"))
        self.comWrite(self.lineW, 2, "1、打开产测工具（或云模组烧录工具）")
        self.comWrite(self.lineW, 3, "1、开启云模组烧录工具，使用蓝牙烧录工具连上设备，输入token授权码\n2、点击开始运行\n3、烧录完毕后，设备重新上电\n4、查看设备是否运行正常")
        self.comWrite(self.lineW, 4, "1、固件烧录成功\n2、设备重新上电后，烧录正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "产测校验", "RSSI和GPIO烧录测试"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[2], constr="|"))
        self.comWrite(self.lineW, 2, "1、打开产测工具（或云模组烧录工具）")
        self.comWrite(self.lineW, 3, "1、云模组工具开始RSSI和GPIO检测\n2、输入token授权码\n3、点击开始运行")
        self.comWrite(self.lineW, 4, "1、固件烧录成功，RSSI和GPIO检测通过")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "产测校验", "固件烧录成功，进行二次检测"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[2], constr="|"))
        self.comWrite(self.lineW, 2, "1、打开产测工具（或云模组烧录工具）")
        self.comWrite(self.lineW, 3, "1、烧录授权完成后，模块重新上电\n2、云模组工具上选择二次检测\n3、点击开始运行")
        self.comWrite(self.lineW, 4, "1、二次检测成功")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "模块升级校验", "从低版本升级到当前版本"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[3], "模块升级校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将模块烧写成比当前测试版本低一版本的代码\n2、NG后台上查找固件key，创建升级到当前版本的固件升级项\n3、设备组网后获取设备id，固件升级项中输入设备id\n4、面板中检查升级是否能成功\n5、面板中检查升级后的版本号是否更新")
        self.comWrite(self.lineW, 4, "1、固件能够升级成功\n2、升级后的版本号为当前版本号")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "模块升级校验", "从当前版本升级到高版本"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[3], "模块升级校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将模块烧写或升级成当前版本\n2、NG后台上查找固件key，创建升级到更高版本的固件升级项\n3、设备组网后获取设备id，固件升级项中输入设备id\n4、面板中检查升级是否能成功\n5、面板中检查升级后的版本号是否更新")
        self.comWrite(self.lineW, 4, "1、固件能够升级成功\n2、升级后的版本号为高版本号")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "模块升级校验", "苹果手机升级校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[3], "模块升级校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、NG后台中设置循环OTA升级项\n2、设备组网后获取设备id，循环OTA升级中输入设备id\n3、使用苹果手机触发升级\n4、查看是否能够成功升级")
        self.comWrite(self.lineW, 4, "1、苹果手机能够成功进行模块升级")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "模块升级校验", "安卓手机升级校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[3], "模块升级校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、NG后台中设置循环OTA升级项\n2、设备组网后获取设备id，循环OTA升级中输入设备id\n3、使用安卓手机触发升级\n4、查看是否能够成功升级")
        self.comWrite(self.lineW, 4, "1、安卓手机能够成功进行模块升级")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "WiFi指示灯", "未联网指示灯校验", "未联网亮灯"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "WiFi指示灯", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将未联网指示灯设置为亮灯，已联网指示灯设置为灭灯，保存配置\n2、授权模块，重新上电\n3、查看组网指示灯是否是亮灯状态")
        self.comWrite(self.lineW, 4, "1、未联网情况下，WiFi指示灯是亮灯状态")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "WiFi指示灯", "未联网指示灯校验", "未联网灭灯"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "WiFi指示灯", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将未联网指示灯设置为灭灯，已联网指示灯设置为亮灯，保存配置\n2、授权模块，重新上电\n3、查看组网指示灯是否是灭灯状态")
        self.comWrite(self.lineW, 4, "1、未联网情况下，WiFi指示灯是灭灯状态")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "WiFi指示灯", "已联网指示灯校验", "已联网亮灯"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "WiFi指示灯", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将未联网指示灯设置为灭灯，已联网指示灯设置为亮灯，保存配置\n2、授权模块，重新上电\n3、查看组网指示灯是否是亮灯状态")
        self.comWrite(self.lineW, 4, "1、未联网情况下，WiFi指示灯是亮灯状态")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "WiFi指示灯", "已联网指示灯校验", "已联网灭灯"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "WiFi指示灯", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将未联网指示灯设置为亮灯，已联网指示灯设置为灭灯，保存配置\n2、授权模块，重新上电\n3、查看组网指示灯是否是灭灯状态")
        self.comWrite(self.lineW, 4, "1、未联网情况下，WiFi指示灯是灭灯状态")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "复位按键", "复位按钮长按时间校验", "长按3S"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "复位按键", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将配网长按秒数设置为3s\n2、授权模块，重新上电\n3、组网后，长按复位按钮3s\n4、查看是否能成功复位模块\n5、复位后进行组网\n6、查看组网是否能成功")
        self.comWrite(self.lineW, 4, "1、长按复位按钮3s能复位成功\n2、复位后能成功组网")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "复位按键", "复位按钮长按时间校验", "长按10S"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[4], "复位按键", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将配网长按秒数设置为10s\n2、授权模块，重新上电\n3、组网后，长按复位按钮10s\n4、查看是否能成功复位模块\n5、复位后进行组网\n6、查看组网是否能成功")
        self.comWrite(self.lineW, 4, "1、长按复位按钮10s能复位成功\n2、复位后能成功组网")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "文本显示校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "显示校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、查看设备名称显示是否正确\n2、查看内容文本是否为：XXXX\n3、底部菜单文本是否为：首页、数据、设置")
        self.comWrite(self.lineW, 4, "1、界面文本显示正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "图片显示校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "显示校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、查看界面中的图片的大小和布局显示是否正确")
        self.comWrite(self.lineW, 4, "1、界面图片显示正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "返回按钮点击校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击返回按钮\n2、查看界面是否跳转到涂鸦设备列表界面")
        self.comWrite(self.lineW, 4, "1、界面跳转正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "编辑按钮点击校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、查点击编辑按钮\n2、查看界面是否跳转到名称设置界面\n3、查看是否能设置设备名称")
        self.comWrite(self.lineW, 4, "1、界面跳转正常，名称设置正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "开关按钮校验", "开启"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击开启开关按钮\n2、查看界面中的开关按钮是否开启\n3、查看设备上的开关是否开启")
        self.comWrite(self.lineW, 4, "1、界面显示正确\n2、设备开关会开启")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "开关按钮校验", "关闭"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击关闭开关按钮\n2、查看界面中的开关按钮是否关闭\n3、查看设备上的开关是否关闭")
        self.comWrite(self.lineW, 4, "1、界面显示正确\n2、设备开关会关闭")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "首页按钮点击校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击底部的首页按钮\n2、查看界面是否加载首页界面")
        self.comWrite(self.lineW, 4, "1、界面会加载首页界面")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "数据按钮点击校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击底部的数据按钮\n2、查看界面是否加载数据界面")
        self.comWrite(self.lineW, 4, "1、界面会加载数据界面")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[6], "设置按钮点击校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[6], "控件校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、点击底部的设置按钮\n2、查看界面是否加载设置界面")
        self.comWrite(self.lineW, 4, "1、界面会加载设置界面")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[7], "显示校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[7], "显示校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、查看界面标题显示为数据\n2、文本信息为：XXXX")
        self.comWrite(self.lineW, 4, "1、界面文本显示正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[7], "XX控件校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[7], "数据校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入数据界面")
        self.comWrite(self.lineW, 3, "1、点击控件按钮\n2、查看界面中XX的信息是否正常更新")
        self.comWrite(self.lineW, 4, "1、界面数据更新正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "显示校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[8], "显示校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入数据界面")
        self.comWrite(self.lineW, 3, "1、查看界面标题显示为设置")
        self.comWrite(self.lineW, 4, "1、界面文本显示正确")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "网页跳转入口校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "入口校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、查看面板的设置界面中是否增加了网页跳转的入口\n3、在IoT平台上关闭高级云功能中的跳转网页\n4、查看面板的设备界面中的网页跳转的入口是否消失")
        self.comWrite(self.lineW, 4, "1、开启跳转网页后，设置界面有网页跳转的入口显示\n2、关闭跳转网页后，设备界面没有网页跳转的入口显示")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "单网页跳转校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "跳转校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、设置一项网页跳转链接\n3、查看面板中网页跳转点击后，是否直接跳转到链接页面")
        self.comWrite(self.lineW, 4, "1、点击后界面直接跳转到链接界面")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "多网页跳转校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "跳转校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、设置多个网页跳转链接\n3、查看面板中网页跳转点击后，是否跳转到链接列表界面\n4、点击列表项，查看是否跳转到对应的链接界面")
        self.comWrite(self.lineW, 4, "1、点击跳转网页后，界面会跳转到链接列表界面\n2、点击列表项，界面会跳转到对应的链接界面")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "云定时校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "云定时", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的云定时功能\n2、点击云定时按钮添加一个新的定时，例：开启开关")
        self.comWrite(self.lineW, 4, "1、设置界面有运云定时的入口\n2、定时新增成功，到达定时时间后开关开启")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "APP解除绑定后组网使用"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[8], "APP解绑", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、点击设置界面中的移除设备按钮\n2、选择解除绑定项\n3、重新组网\n4、进行主功能校验")
        self.comWrite(self.lineW, 4, "1、解绑后组网使用正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[8], "APP解除绑定后组网使用"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[8], "APP恢复出厂设置", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、面板有设置界面（否则该用例可能不支持）\n3、进入设置界面")
        self.comWrite(self.lineW, 3, "1、点击设置界面中的移除设备按钮\n2、选择解绑并清除数据\n3、重新组网\n4、进行主功能校验")
        self.comWrite(self.lineW, 4, "1、恢复出厂设置后组网使用正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[9], "美国区面板主功能校验(可选)"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[9], "时区校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入XX详情界面")
        self.comWrite(self.lineW, 3, "1、手机切换到纽约时区\n2、涂鸦APP时区切换到纽约\n3、涂鸦APP登录美国区账号\n4、验证XX功能是否正常\n5、验证XX功能是否正常")
        self.comWrite(self.lineW, 4, "1、XX功能正常\n2、XX功能正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[9], "欧洲区面板主功能校验(可选)"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[9], "时区校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入XX详情界面")
        self.comWrite(self.lineW, 3, "1、手机切换到巴黎时区\n2、涂鸦APP时区切换到巴黎\n3、涂鸦APP登录法国账号，注意不能和美国账号一样\n4、验证XX功能是否正常\n5、验证XX功能是否正常")
        self.comWrite(self.lineW, 4, "1、XX功能正常\n2、XX功能正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[9], "苹果手机主功能校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[9], "苹果机型校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入XX详情界面")
        self.comWrite(self.lineW, 3, "1、使用苹果手机\n2、验证XX功能是否正常\n3、验证XX功能是否正常")
        self.comWrite(self.lineW, 4, "1、XX功能正常\n2、XX功能正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[9], "安卓手机主功能校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[9], "安卓机型校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入群组详情界面")
        self.comWrite(self.lineW, 3, "1、使用安卓手机\n2、验证XX功能是否正常\n3、验证XX功能是否正常")
        self.comWrite(self.lineW, 4, "1、群组功能正常\n2、打卡功能正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[9], "遍历机型测试验证"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[9], "兼容性", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、需要验证iOS机型：SE（10.2.1）、7（11.2.6）、8P（12.2）、XR（13.2）\n2、需要验证安卓机型：OPPO R9（5.1）、LG 5X（6.0）、三星 C8（7.0）、华为荣耀 8Xmax（8.1）、vivo Y97(8.1)、魅族 16xs(9.0)、一加 7PRO（10）")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[10], "用户设计体验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[10], constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
        self.comWrite(self.lineW, 3, "1、该用例需要通知UI设计人员执行\n2、UI设计人员来进行用例体验的校验\n3、若校验通过则该用例通过")
        self.comWrite(self.lineW, 4, "1、UED校验通过")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例,\n" + self.product + "SoC冒烟用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1

    def writePinConfigCase(self, pinInfo):
        if "P" not in pinInfo[1]:
            return

        if "灯" in pinInfo[0]:
            pinAction = pinInfo[0].split("灯")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "引脚设置为高电平有效\n2、对模块重新授权\n3、面板进行" + pinAction + "操作\n4、确认对应高电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinInfo[0] + "引脚高电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "引脚设置为低电平有效\n2、对模块重新授权\n3、面板进行" + pinAction + "操作\n4、确认对应低电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinInfo[0] + "引脚低电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "检测" in pinInfo[0]:
            pinAction = pinInfo[0].split("检测")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "引脚设置为高电平有效\n2、对模块重新授权\n3、面板触发" + pinAction + "操作\n4、确认对应高电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinInfo[0] + "引脚高电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "引脚设置为低电平有效\n2、对模块重新授权\n3、面板触发" + pinAction + "操作\n4、确认对应低电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinInfo[0] + "引脚低电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "输出" in pinInfo[0]:
            pinAction = pinInfo[0].split("引脚")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinAction + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinAction + "引脚设置为高电平有效\n2、对模块重新授权\n3、面板触发" + pinAction + "操作\n4、确认对应高电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinAction + "引脚高电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinAction + "引脚设置为低电平有效\n2、对模块重新授权\n3、面板触发" + pinAction + "操作\n4、确认对应低电平输出指示灯会亮起")
            self.comWrite(self.lineW, 4, "1、" + pinAction + "引脚低电平输出正常")
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1

        if "按" in pinInfo[0]:
            pinAction = pinInfo[0].split("按")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为高电平有效\n2、引脚接线到高有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "后能成功" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为低电平有效\n2、引脚接线到低有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "后能成功" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚多次点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、多次点击" + pinInfo[0] + "\n2、查看每次点击是否都能正常触发" + pinAction + "按钮")
            self.comWrite(self.lineW, 4, "1、每次点击都能正常触发" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "切换" in pinInfo[0]:
            pinAction = pinInfo[0].split("切换")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为高电平有效\n2、引脚接线到高有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinInfo[0])
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功" + pinInfo[0])
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为低电平有效\n2、引脚接线到低有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinInfo[0])
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功" + pinInfo[0])
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "开关" in pinInfo[0]:
            pinAction = pinInfo[0].split("开关")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为高电平有效\n2、引脚接线到高有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为低电平有效\n2、引脚接线到低有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "转" in pinInfo[0]:
            pinAction = pinInfo[0].split("转")[0]
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为高电平有效\n2、引脚接线到高有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功触发" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功触发" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为低电平有效\n2、引脚接线到低有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功触发" + pinAction)
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功触发" + pinAction)
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif "恢复出厂" in pinInfo[0]:
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚高电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为高电平有效\n2、引脚接线到高有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功触发" + pinInfo[0])
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功触发" + pinInfo[0])
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例，\n" + self.product + "SoC冒烟用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", pinInfo[0] + "引脚低电平校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、设备已烧录")
            self.comWrite(self.lineW, 3, "1、将" + pinInfo[0] + "的引脚设置为低电平有效\n2、引脚接线到低有效按钮上\n3、对模块进行授权\n4、模块重新上电，按触发按钮\n5、查看是否能成功触发" + pinInfo[0])
            self.comWrite(self.lineW, 4, "1、按" + pinInfo[0] + "按钮后能成功触发" + pinInfo[0])
            self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1

    def writePinErgodicCase(self):
        # 引脚遍历
        self.comWrite(self.lineW, 0, self.connector(self.product, "引脚遍历", "指示灯引脚遍历"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚遍历", "指示灯引脚", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、将WiFi指示灯未联网状态设置为亮灯\n2、依次遍历所有可选引脚，授权模块，重新上电\n3、查看对应的引脚灯是否会亮起")
        self.comWrite(self.lineW, 4, "1、遍历引脚，对应指示灯都会亮起")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "引脚校验", "按钮引脚遍历"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "引脚遍历", "按钮引脚", constr="|"))
        self.comWrite(self.lineW, 2, "1、设备上电\n2、打开APP")
        self.comWrite(self.lineW, 3, "1、重置按钮依次遍历所有引脚，授权模块，重新上电\n2、查看点击对应引脚按钮\n3、查看是否会重置成功")
        self.comWrite(self.lineW, 4, "1、遍历引脚，对应按钮都能成功触发重置")
        self.comWrite(self.lineW, 5, self.product + "SoC方案用例")
        self.comWrite(self.lineW, 6, "P0")
        self.lineW += 1

    def caseTitle_init(self):
        print("start to init the title of testcase.")
        redN = self.workbookW.add_format({'border': 1, 'align': 'center', 'color': '#ff0000', 'bg_color': '#9BC2E6', 'font_name':'微软雅黑', 'font_size': 11, 'bold': False})
        self.comFormat_left = self.workbookW.add_format({'border': 1, 'align': 'left', 'valign': 'vcenter', 'bg_color': '#EBEBEB', 'font_name': '微软雅黑', 'font_size': 11, 'text_wrap': 1})
        self.comFormat_Mid = self.workbookW.add_format({'border': 1, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#EBEBEB', 'font_name': '微软雅黑', 'font_size': 11, 'text_wrap': 1})
        # 设置列行的宽高
        self.worksheetW1.set_column("A:A", 30)
        self.worksheetW1.set_column("B:B", 30)
        self.worksheetW1.set_column("C:C", 18)
        self.worksheetW1.set_column("D:D", 45)
        self.worksheetW1.set_column("E:E", 35)
        self.worksheetW1.set_column("F:F", 18)
        self.worksheetW1.set_column("G:G", 10)
        self.worksheetW1.set_column("H:H", 10)
        self.worksheetW1.set_column("I:I", 10)

        for (index, item) in zip(self.column, self.title):
            self.worksheetW1.write(index + "1", item, redN)
        print("finished to init the title of testcase.")

if __name__ == "__main__":
    project_fan = TestProject()
    project_fan.loadCaselist()
    #project_fan.loadCaselist()





# -*- coding: utf-8 -*-
import xlrd, xlsxwriter

class TestProject:
    def __init__(self):
        self.title = [u"标题*", u"目录层级", u"前置条件", u"步骤描述", u"期望结果", u"标签", u"优先级", u"关联需求编号", u"备注"]
        self.column = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        self.proLine = u"小家电"
        self.product = u"宠物喂食器"
        self.funcList = [u"DP校验", u"主页界面"]
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
        self.workbookR = xlrd.open_workbook(self.product + u"功能列表.xlsx")
        self.workbookW = xlsxwriter.Workbook(self.product + u"测试用例.xlsx")
        self.worksheetW1 = self.workbookW.add_worksheet(u"面板测试")

    def xlsxClose(self):
        self.workbookR.close()
        self.workbookW.close()

    def connector(self, *key, constr="-"):
        return constr.join(key)

    def loadCaselist(self):
        # 写入功能校验用例
        # 根据sheet索引或者名称获取sheet内容
        sheet = self.workbookR.sheet_by_index(0)
        print("Start to load the function list of dp.")
        for i in range(sheet.nrows):
            self.writeFuncCase(sheet.row_values(i))
        print("Finished to load the function list of dp")

        # 写入枚举项dp的校验：模式、风速
        print("Start to load the case of enum dp.")
        for i in range(sheet.nrows):
            self.writeEnumCase(sheet.row_values(i))
        print("Finished to load the case of enum dp")
        #
        # # 写入页面校验用例
        print("Start to load the function list of page")
        for page in self.pages:
            self.writePageCase(page)
        print("Finished to load the function list of page")
        #
        # # 写入其他测试用例
        print("Start to load the function list of other")
        self.writeOtherCase()
        print("Finished to load the function list of other")

        self.workbookW.close()

    # def menuInit(self, dpInfo, module=0):
    #     # self.comWrite(self.lineW, 0, self.proLine)
    #     # self.comWrite(self.lineW, 1, self.product)
    #     # self.comWrite(self.lineW, 2, self.funcList[module])
    #     # self.comWrite(self.lineW, 3, dpInfo[1])
    #     # self.comWrite(self.lineW, 4, "")
    #     self.comWrite(self.lineW, 0, self.connector(self.proLine, self.product, self.funcList[module], dpInfo[1]))
    #
    # def dirInit(self, pageName="", subPageOrCheck="", checkPoint=""):
    #     # self.comWrite(self.lineW, 0, self.proLine)
    #     # self.comWrite(self.lineW, 1, self.product)
    #     # self.comWrite(self.lineW, 2, pageName)
    #     # self.comWrite(self.lineW, 3, subPageOrCheck)
    #     # self.comWrite(self.lineW, 4, checkPoint)
    #     self.comWrite(self.lineW, 0, self.connector(self.proLine, self.product, pageName, subPageOrCheck, checkPoint))

    def writeFuncCase(self, dpInfo):
        print(dpInfo)
        dpid = str(dpInfo[0]).split(".")[0]
        if dpInfo[4] == 'bool' and '可下发可上报' in dpInfo[3]:
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1]+"下发-开"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、打开" + dpInfo[1] + "按钮\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为on")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1]+"上报-开"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "开的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "按钮开启")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1]+"下发-关"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、关闭" + dpInfo[1] + "按钮\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为off")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1]+"上报-关"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "关的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "按钮关闭")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
        elif dpInfo[4] == "enum" and "可下发可上报" in dpInfo[3]:
            dpAttri = dpInfo[5]
            dpEnumData = dpAttri.split(u"枚举值")[1].split(",")
            print(dpEnumData)
            for i in range(len(dpEnumData)):
                if i == 0 or i == (len(dpEnumData)-1):
                    self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "下发-" + dpEnumData[i]))
                    self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                    self.comWrite(self.lineW, 2, "1、打开APP")
                    self.comWrite(self.lineW, 3, "1、将" + dpInfo[1] + "设置为" + dpEnumData[i] + "\n2、查看下发的dp信息")
                    self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为" + dpEnumData[i])
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                    self.comWrite(self.lineW, 6, "P1")
                    self.lineW += 1
                    self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + dpEnumData[i]))
                    self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                    self.comWrite(self.lineW, 2, "1、打开APP")
                    self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + dpEnumData[i] + "的dp信息\n2、查看界面显示")
                    self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "为" + dpEnumData[i])
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                    self.comWrite(self.lineW, 6, "P2")
                    self.lineW += 1
        elif dpInfo[4] == "enum" and "只上报" in dpInfo[3]:
            dpAttri = dpInfo[5]
            dpEnumData = dpAttri.split(u"枚举值")[1].split(",")
            print(dpEnumData)
            for i in range(len(dpEnumData)):
                if i == 0 or i == (len(dpEnumData)-1):
                    self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "下发-" + dpEnumData[i]))
                    self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                    self.comWrite(self.lineW, 2, "1、打开APP")
                    self.comWrite(self.lineW, 3, "1、将" + dpInfo[1] + "设置为" + dpEnumData[i] + "\n2、查看下发的dp信息")
                    self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为" + dpEnumData[i])
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                    self.comWrite(self.lineW, 6, "P1")
                    self.lineW += 1
                    self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + dpEnumData[i]))
                    self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                    self.comWrite(self.lineW, 2, "1、打开APP")
                    self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + dpEnumData[i] + "的dp信息\n2、查看界面显示")
                    self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "为" + dpEnumData[i])
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                    self.comWrite(self.lineW, 6, "P2")
                    self.lineW += 1
        elif dpInfo[4] == "value" and "可下发可上报" in dpInfo[3]:
            dpAttri = dpInfo[5]
            print(dpAttri)
            dpAttri = dpAttri.replace(" ", "")
            print(dpAttri)
            dataArr = dpAttri.split(",")[0].split(":")[1].split("-")
            if len(dataArr) == 2:
                print("Value范围为：" + str(dataArr))
                valueMin = dataArr[0]
                valueMax = dataArr[1]
            else:
                print("Value范围为：" + str(dataArr))
                valueMin = "-" + dataArr[1]
                valueMax = dataArr[2]
            valueMid = str(int(valueMax) / 2 if int(valueMax) % 2 == 0 else (int(valueMax) + 1) / 2).split(".")[0]
            print(valueMin, valueMid, valueMax)

            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "下发-" + valueMin))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、将" + dpInfo[1] + "设置为" + valueMin + "\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为" + valueMin)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMin))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMin + "的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMin)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "下发-" + valueMid))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、将" + dpInfo[1] + "设置为" + valueMid + "\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为" + valueMid)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMid))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMid + "的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMid)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "下发-" + valueMax))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、将" + dpInfo[1] + "设置为" + valueMax + "\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、dpid为" + dpid + ",value为" + valueMax)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMax))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMax + "的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMax)
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
        elif dpInfo[4] == "value" and "只上报" in dpInfo[3]:
            dpAttri = dpInfo[5]
            dataArr = dpAttri.split(",")[0].split(":")[1].split("-")
            if len(dataArr) == 2:
                print("Value范围为：" + str(dataArr))
                valueMin = dataArr[0]
                valueMax = dataArr[1]
            else:
                print("Value范围为：" + str(dataArr))
                valueMin = "-" + dataArr[1]
                valueMax = dataArr[2]
            valueMid = str(int(valueMax) / 2 if int(valueMax) % 2 == 0 else (int(valueMax) + 1) / 2).split(".")[0]
            print(valueMin, valueMid, valueMax)

            if dpInfo[2] == "battery_percentage":
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + "0%"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + "0%" + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + "0%")
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + "19%"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + "19%" + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + "19%")
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + "20%"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + "20%" + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + "20%")
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + "100%"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + "100%" + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + "100%")
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
            else:
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMin))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMin + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMin)
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMid))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMid + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMid)
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
                self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "上报-" + valueMax))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP")
                self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "为" + valueMax + "的dp信息\n2、查看界面显示")
                self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "显示为" + valueMax)
                self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P2")
                self.lineW += 1
        elif dpInfo[4] == "raw" and "可下发可上报" in dpInfo[3]:
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "设置下发"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、手机设置" + dpInfo[1] + "信息\n2、查看下发的dp信息")
            self.comWrite(self.lineW, 4, "1、mcu收到的dp信息正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "设置上报"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "信息更新正常")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
        elif dpInfo[4] == "raw" and "只上报" in dpInfo[3]:
            self.comWrite(self.lineW, 0, self.connector(self.product, self.funcList[0], dpInfo[1] + "设置上报"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, self.funcList[0], dpInfo[1], constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP")
            self.comWrite(self.lineW, 3, "1、通过mcu上报" + dpInfo[1] + "的dp信息\n2、查看界面显示")
            self.comWrite(self.lineW, 4, "1、界面中" + dpInfo[1] + "信息更新正常")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
        else:
            pass

    def writeEnumCase(self, dpInfo):
        print(dpInfo)
        dpid = str(dpInfo[0]).split(".")[0]
        if dpInfo[4] == "enum" and "可下发可上报" in dpInfo[3] and dpInfo[2] == "mode":
            dpAttri = dpInfo[5]
            dpEnumData = dpAttri.split(u"枚举值")[1].split(",")
            enumString = "、".join(dpEnumData)
            self.comWrite(self.lineW, 0, self.connector(self.product, "模式弹出框", "模式显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "模式弹出框", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
            self.comWrite(self.lineW, 3, "1、查看弹出框的标题是否为mode\n2、查看模式项是否对应功能dp的枚举数值\n3、模式项显示为：" + enumString)
            self.comWrite(self.lineW, 4, "1、标题显示正确\n2、模式项显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "模式弹出框", "模式枚举项修改校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "模式弹出框", "枚举修改校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
            self.comWrite(self.lineW, 3, "1、修改模式枚举项\n2、查看弹出框模式项更新是否正常\n3、增加模式枚举项\n4、查看弹出框模式项是否增加\n5、删除模式枚举项\n6、查看弹出框模式项是否减少\n7、设置新增枚举的多语言\n8、查看界面多语言显示是否正确")
            self.comWrite(self.lineW, 4, "1、标题显示正确\n2、模式项更新正常\n3、多语言项显示正确\n")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
            for i in range(len(dpEnumData)):
                ele = dpEnumData[i]
                self.comWrite(self.lineW, 0, self.connector(self.product, "模式弹出框", "模式" + ele + "上报下发校验"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "模式弹出框", "控件校验", constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
                self.comWrite(self.lineW, 3, "1、点击开启" + ele + "模式项\n2、确认下发的dp报文正确\n3、确认" + ele + "项会变为高亮状态\n4、确认其他模式项会变为非高亮\n5、确认首页中当前模式图标会变为" + ele + "\n6、将模式切换到非" + ele + "\n7、通过mcu上报模式为" + ele + "的报文\n8、确认模式弹出框中" + ele + "会变为高亮")
                self.comWrite(self.lineW, 4, "1、模式下发报文正常\n2、模式上报后弹出框响应正常")
                if i == 0 or i == (len(dpEnumData) - 1):
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例,\n" + self.product + "公版冒烟用例")
                else:
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P0")
                self.lineW += 1
        elif dpInfo[4] == "enum" and "可下发可上报" in dpInfo[3] and dpInfo[2] == "fan_speed_enum":
            dpAttri = dpInfo[5]
            dpEnumData = dpAttri.split(u"枚举值")[1].split(",")
            enumString = "、".join(dpEnumData)
            self.comWrite(self.lineW, 0, self.connector(self.product, "风速弹出框", "风速档位显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "风速弹出框", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
            self.comWrite(self.lineW, 3, "1、查看弹出框的标题是否为Fan\n2、查看模式项是否对应功能dp的枚举数值\n3、模式项显示为：" + enumString)
            self.comWrite(self.lineW, 4, "1、标题显示正确\n2、风速项显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, "风速弹出框", "风速枚举项修改校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "风速弹出框", "枚举修改校验", constr="|"))
            self.comWrite(self.lineW, 8, "1、打开APP\n2、进入首页界面")
            self.comWrite(self.lineW, 9, "1、修改风速枚举项\n2、查看弹出框模式项更新是否正常\n3、增加风速枚举项\n4、查看弹出框风速项是否增加\n5、删除风速枚举项\n6、查看弹出框风速项是否减少\n7、设置新增枚举的多语言\n8、查看界面多语言显示是否正确")
            self.comWrite(self.lineW, 10, "1、标题显示正确\n2、风速项更新正常\n3、多语言项显示正确\n")
            self.comWrite(self.lineW, 7, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P2")
            self.lineW += 1
            for i in range(len(dpEnumData)):
                ele = dpEnumData[i]
                self.comWrite(self.lineW, 0, self.connector(self.product, "风速弹出框", "风速档位" + ele + "上报下发校验"))
                self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "首页界面", "风速弹出框", "控件校验", constr="|"))
                self.comWrite(self.lineW, 2, "1、打开APP\n2、进入首页界面")
                self.comWrite(self.lineW, 3, "1、点击开启" + ele + "风速项\n2、确认下发的dp报文正确\n3、确认" + ele + "项会变为高亮状态\n4、确认其他风速项会变为非高亮\n5、确认首页中当前风速图标会变为" + ele + "\n6、将风速切换到非" + ele + "\n7、通过mcu上报模式为" + ele + "的报文\n8、确认风速弹出框中" + ele + "会变为高亮")
                self.comWrite(self.lineW, 4, "1、风速下发报文正常\n2、风速上报后弹出框响应正常")
                if i == 0 or i == (len(dpEnumData) - 1):
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例,\n" + self.product + "公版冒烟用例")
                else:
                    self.comWrite(self.lineW, 5, self.product + "公版面板用例")
                self.comWrite(self.lineW, 6, "P0")
                self.lineW += 1

    def writePageCase(self, pageInfo):
        print("Load Page Case")
        if pageInfo == u"首页":
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "文本显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、查看设备名称显示是否正确\n2、查看内容文本是否为：XXXX\n3、底部菜单文本是否为：首页、数据、设置")
            self.comWrite(self.lineW, 4, "1、界面文本显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "图片显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、查看界面中的图片的大小和布局显示是否正确")
            self.comWrite(self.lineW, 4, "1、界面图片显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "返回按钮点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击返回按钮\n2、查看界面是否跳转到涂鸦设备列表界面")
            self.comWrite(self.lineW, 4, "1、界面跳转正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "编辑按钮点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击编辑按钮\n2、查看界面是否跳转到名称设置界面\n3、查看是否能设置设备名称")
            self.comWrite(self.lineW, 4, "1、操作正常显示正常")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "开关按钮校验", "开启"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击开启开关按钮\n2、查看界面中的开关按钮是否开启\n3、查看下发的dp信息是否正确")
            self.comWrite(self.lineW, 4, "1、界面显示正确\n2、dp报文正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "开关按钮校验", "关闭"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击关闭开关按钮\n2、查看界面中的开关按钮是否关闭\n3、查看下发的dp信息是否正确")
            self.comWrite(self.lineW, 4, "1、界面显示正确\n2、dp报文正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "首页按钮点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击底部的首页按钮\n2、查看界面是否加载首页界面")
            self.comWrite(self.lineW, 4, "1、界面会加载首页界面")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "数据按钮点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击底部的数据按钮\n2、查看界面是否加载数据界面")
            self.comWrite(self.lineW, 4, "1、界面会加载数据界面")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "设置按钮点击校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击底部的设置按钮\n2、查看界面是否加载设置界面")
            self.comWrite(self.lineW, 4, "1、界面会加载设置界面")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
        elif pageInfo == u"数据":
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、查看界面标题显示为数据\n2、文本信息为：XXXX")
            self.comWrite(self.lineW, 4, "1、界面文本显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "XX控件校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "数据校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、通过mcu上报XX的dp报文\n2、查看界面中XX的信息是否正常更新")
            self.comWrite(self.lineW, 4, "1、界面数据更新正常")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        elif pageInfo == u"设置":
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "显示校验"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "显示校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、查看界面标题显示为设置\n2、查看功能项是否为：童锁")
            self.comWrite(self.lineW, 4, "1、界面文本显示正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P1")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "童锁行布尔按钮校验", "开启"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击开启童锁行后的布尔按钮\n2、查看下发的dp信息是否正确")
            self.comWrite(self.lineW, 4, "1、界面控件显示正常\n2、dp报文正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
            self.comWrite(self.lineW, 0, self.connector(self.product, pageInfo + "界面", "童锁行布尔按钮校验", "关闭"))
            self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, pageInfo + "界面", "控件校验", constr="|"))
            self.comWrite(self.lineW, 2, "1、打开APP\n2、进入" + pageInfo + "界面")
            self.comWrite(self.lineW, 3, "1、点击关闭童锁行后的布尔按钮\n2、查看下发的dp信息是否正确")
            self.comWrite(self.lineW, 4, "1、界面控件显示正常\n2、dp报文正确")
            self.comWrite(self.lineW, 5, self.product + "公版面板用例")
            self.comWrite(self.lineW, 6, "P0")
            self.lineW += 1
        else:
            pass

    def writeOtherCase(self):
        print("Load other case")
        # 网页跳转
        self.comWrite(self.lineW, 0, self.connector(self.product, "设置界面", "网页跳转入口校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "入口校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、查看面板的设置界面中是否增加了网页跳转的入口\n3、在IoT平台上关闭高级云功能中的跳转网页\n4、查看面板的设备界面中的网页跳转的入口是否消失")
        self.comWrite(self.lineW, 4, "1、开启跳转网页后，设置界面有网页跳转的入口显示\n2、关闭跳转网页后，设备界面没有网页跳转的入口显示")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "设置界面", "单网页跳转校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "跳转校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、设置一项网页跳转链接\n3、查看面板中网页跳转点击后，是否直接跳转到链接页面")
        self.comWrite(self.lineW, 4, "1、点击后界面直接跳转到链接界面")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1
        self.comWrite(self.lineW, 0, self.connector(self.product, "设置界面", "多页跳转校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "网页跳转", "跳转校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、进入设置界面")
        self.comWrite(self.lineW, 3, "1、在IoT平台上开启高级云功能中的跳转网页\n2、设置多个网页跳转链接\n3、查看面板中网页跳转点击后，是否跳转到链接列表界面\n4、点击列表项\n5、查看是否跳转到对应的链接界面")
        self.comWrite(self.lineW, 4, "1、点击跳转网页后，界面会跳转到链接列表界面\n2、点击列表项，界面会跳转到对应的链接界面")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P2")
        self.lineW += 1

        # 新建产品的数据校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "新建产品", "dp校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "新建产品", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、在IoT平台上新建产品\n2、查看dp信息中dpid是否与需求一致\n3、查看dp信息中功能点名称是否与需求一致\n4、查看dp信息中数据类型是否正常\n4、查看dp信息中数值范围是否合理")
        self.comWrite(self.lineW, 4, "1、新建产品中dp信息显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 只有必选功能点的情况下的显示校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "功能定义", "只有必选功能情况下的显示校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "功能定义", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、在IoT平台中将设备中的所有可选功能删除\n2、查看各个界面显示是否正常")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 只有必选功能点的情况下的控件校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "功能定义", "只有必选功能情况下的控件校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "功能定义", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、在IoT平台中将设备中的所有可选功能删除\n2、点击各个按钮\n3、查看操作是否正常")
        self.comWrite(self.lineW, 4, "1、界面控件操作正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 只有必选功能点的情况下的dp上报校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "功能定义", "只有必选功能情况下的dp上报校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "功能定义", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、在IoT平台中将设备中的所有可选功能删除\n2、通过mcu上报必要功能的dp报文\n3、查看界面显示是否正常")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # dp文本信息修改后信息的同步
        self.comWrite(self.lineW, 0, self.connector(self.product, "数据同步", "dp文本信息修改后信息的同步"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "数据同步", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、抽取1个dp项修改文本信息\n2、查看界面显示是否同步更新")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # dp中枚举信息修改后的同步
        self.comWrite(self.lineW, 0, self.connector(self.product, "数据同步", "dp中枚举信息修改的同步"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "数据同步", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、模式中的枚举项中去除部枚举项同时新增部分枚举项\n2、查看界面中对应数据的显示")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 连续请求校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "连续请求", "新增XX界面的保存按钮连续点击"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "连续请求", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、输入模式信息\n2、连续快速的点击保存按钮\n3、查看XX是否只增加一个")
        self.comWrite(self.lineW, 4, "1、操作正常，显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 英文显示
        self.comWrite(self.lineW, 0, self.connector(self.product, "英文显示", "将语言设置为英文"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "英文显示", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、将手机语言设置为英文\n2、查看各个界面显示是否正常")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 手机端兼容性测试
        self.comWrite(self.lineW, 0, self.connector(self.product, "兼容性", "手机兼容性测试"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "手机端兼容性测试", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、需要验证iOS机型：SE（10.2.1）、7（11.2.6）、8P（12.2）、XR（13.2）\n2、需要验证安卓机型：OPPO R9（5.1）、LG 5X（6.0）、三星 C8（7.0）、华为荣耀 8Xmax（8.1）、vivo Y97(8.1)、魅族 16xs(9.0)、一加 7PRO（10）")
        self.comWrite(self.lineW, 4, "1、界面显示正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # 用户场景
        self.comWrite(self.lineW, 0, self.connector(self.product, "用户场景", "用户自定义dp兼容性测试"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "用户场景", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP")
        self.comWrite(self.lineW, 3, "1、在IoT平台上的测试产品中创建自定义dp,包括布尔、数值、枚举\n2、查看APP中设备界面是否新增了该项功能\n3、操作该项控件\n4、查看下发的dp信息是否正确\n5、更新上位机加载的dp数据\n6、上报对应报文\n7、查看状态变化是否正常")
        self.comWrite(self.lineW, 4, "1、界面显示正常\n2、下发的dp数据正常")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例")
        self.comWrite(self.lineW, 6, "P1")
        self.lineW += 1
        # UED校验
        self.comWrite(self.lineW, 0, self.connector(self.product, "UED校验", "用户体验设计校验"))
        self.comWrite(self.lineW, 1, self.connector(self.proLine, self.product, "其他", "UED校验", constr="|"))
        self.comWrite(self.lineW, 2, "1、打开APP\n2、该项需要在Ios和安卓上都进行验证")
        self.comWrite(self.lineW, 3, "1、该用例需要通知UI设计人员执行\n2、UI设计人员来进行用例体验的校验\n3、若校验通过则该用例通过")
        self.comWrite(self.lineW, 4, "1、UED校验通过")
        self.comWrite(self.lineW, 5, self.product + "公版面板用例，\n" + self.product + "公版冒烟用例")
        self.comWrite(self.lineW, 6, "P1")
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
        self.worksheetW1.set_column("D:D", 35)
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






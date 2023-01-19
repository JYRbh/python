#!-*- coding:utf-8 -*-
import xlrd,xlsxwriter
class TestProject():
    def __init__(self):
        self.xlsxInit()
        self.see()
        self.workbookw.close()
    def xlsxInit(self):
        self.workbookR = xlrd.open_workbook("血氧仪测试用例.xlsx")
        self.workbookw = xlsxwriter.Workbook("血氧仪测试用例.xlsx")
    def see(self):
        sheet = self.workbookR.sheet_by_index(0)
        for line in range(sheet.nrows):
            print(sheet.row_values(line))

if __name__ == "__main__":
    A=TestProject()



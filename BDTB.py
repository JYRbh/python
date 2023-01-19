__author__ = 'CQC'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


class BDTB:

    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None

baseURL = 'https://tieba.baidu.com/p/5528987683?fr=ala0&pstaala=1&tpl=5&fid=4536&isgod=0&red_tag=3030416059'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)

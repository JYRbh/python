

# http://www.netbian.com
#desk/25261.htm

import parsel
import requests #请求模块 第三方模块


url = 'http://www.netbian.com/'

#
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36'
}

response = requests.get(url = url,headers = headers)

#出现乱码怎么办？需要转码
#html_data = response.content.decode('gbk')
response.encoding = response.apparent_encoding #自动转码

#获去源代码/获取网页文本数据 respinse.text
#print(html_data)
#print(response.text)

#解析数据
selector = parsel.Selector(response.text)

#CSS选择器 就是根据网页标签内容提取数据
#第一次提取 提取所有的li标签内容
lis = selector.css('.list li')
for li in lis:
    title = li.css('b::text').get()
    if title:
        href = 'http://www.netbian.com/' + li.css('a::attr(href)').get()
        response_1 = requests.get(url=href, headers=headers)
        selector_1 = parsel.Selector(response_1.text)
        img_url = selector_1.css('.pic img::attr(src)').get()

        img_content = requests.get(url = img_url ,headers = headers).content
        with open('img\\'+title+'.jpg',mode='wb') as f:
            f.write(img_content)
            print('正在保存：',title)
















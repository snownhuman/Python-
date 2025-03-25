import requests
from lxml import etree
import re
datas={
    "email":"2494665683@qq.com",
    "password":"18149051566Msc",
    '_token':'',
}
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
url="http://www.glidedsky.com/login"
#使用get请求获得数据使用正则表达式获得'_token'
session=requests.Session()
url_get=session.get(url=url,headers=header).text
r=(r'input type="hidden" name="_token" value="(.*?)">')
res=re.search(r,url_get).group(1)
datas['_token']=res
xiangying=session.post(data=datas,headers=header,url=url)
#iNoUdfzeoRRJe7MpyxM821FSNh0K2XKq3a1tA6Nq
url1='http://www.glidedsky.com/level/web/crawler-basic-1'
number_url=session.get(url=url1,headers=header).text
tree=etree.HTML(number_url)
number_list=tree.xpath('//*[@id="app"]/main/div[1]/div/div/div/div/text()')
number=r'(^\d{1,})$'
b=0
for i in number_list:
    a="".join(i.split())
    b=b+int(a)
print(b)
#E:\python\pac_test\Wanzhandenglu.py
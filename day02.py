import re
import requests
from lxml import etree
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36 Edg/134.0.0.0'
}
old_url='http://glidedsky.com/login'
session=requests.Session()
datas={
    '_token': '',
    'email': '2494665683@qq.com',
    'password': '18149051566Msc'
}
login_page_text=session.get(url=old_url,headers=headers).text
zhengze=r'<meta name="csrf-token" content="(.*?)">'
zimu=re.findall(zhengze,login_page_text)
datas['_token']=zimu[0]
session.post(data=datas,headers=headers,url=old_url)
#http://glidedsky.com/level/web/crawler-basic-2?page=1

c=0
for i in range(1,1001):
    #/html/body/div/main/div[1]/div/div/div/div[1]
    url='http://glidedsky.com/level/web/crawler-basic-2?page='+str(i)
    response=session.get(url=url,headers=headers).text
    tree=etree.HTML(response)
    number_list=tree.xpath('/html/body/div/main/div[1]/div/div/div/div/text()')
    for a in number_list:
        c=c+int(a)
    print(c)

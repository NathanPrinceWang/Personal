# -*- coding: UTF-8 -*-
import smtplib
import time
import urllib2,urllib
import json
from email.mime.text import MIMEText
from email.header import Header
#groups=0&type==3为游客状态下banner接口
url1 = 'http://v.dx168.com/tools-apis/api/app/push/ygzp/getBannerOrPopup'
data1 = {"groups":"0","type":"3"}
data1 = urllib.urlencode(data1)
url2 = urllib2.Request(url1,data1)
#读取该参数执行结果中的“code”
response1 = json.loads(urllib2.urlopen(url2).read())['code']
#比较code值是否等于1如果等于1在output文件中输出success！错误输出fail
if response1 == 1:
    out = "<p>---游客banner：Success--------" 
    output1 = out
else:
    out = "<p>---游客banner：Fail-----------"
    output1 = out
#groups=1&type==3为注册未开户状态下banner接口
data2 = {"groups":"1","type":"3"}
data2 = urllib.urlencode(data2)
url2 = urllib2.Request(url1,data2)
response2 = json.loads(urllib2.urlopen(url2).read())['code']
if response2 == 1:
    out = "<p>---注册未开户banner：Success---" 
    output2 = out
else:
    out = "<p>---注册未开户banner：Fail------"
    output2 = out
#groups=2&type==3为开户未激活状态下banner接口
data3 = {"groups":"2","type":"3"}
data3 = urllib.urlencode(data3)
url2 = urllib2.Request(url1,data3)
response3 = json.loads(urllib2.urlopen(url2).read())['code']
if response3 == 1:
    out = "<p>---开户未激活banner：Success---" 
    output3 = out
else:
    out = "<p>---开户未激活banner：Fail------"
    output3 = out
#groups=3&type==3为激活状态下banner接口
data4 = {"groups":"3","type":"3"}
data4 = urllib.urlencode(data4)
url2 = urllib2.Request(url1,data4)
response4 = json.loads(urllib2.urlopen(url2).read())['code']
if response4 == 1:
    out = "<p>---激活banner：Success--------" 
    output4 = out
else:
    out = "<p>---激活banner：Fail-----------"
    output4 = out
#groups=0&type==4为游客状态下弹窗接口
data5 = {"groups":"0","type":"4"}
data5 = urllib.urlencode(data5)
url2 = urllib2.Request(url1,data5)
response5 = json.loads(urllib2.urlopen(url2).read())['code']
if response5 == 1:
    out = "<p>---游客每日弹窗：Success--------" 
    output5 = out
else:
    out = "<p>---游客每日弹窗：Fail-----------"
    output5 = out
#groups=1&type==4为已注册未开户每日弹窗接口
data6 = {"groups":"1","type":"4"}
data6 = urllib.urlencode(data6)
url2 = urllib2.Request(url1,data6)
response6 = json.loads(urllib2.urlopen(url2).read())['code']
if response6 == 1:
    out = "<p>---已注册未开户每日弹窗：Success--" 
    output6 = out
else:
    out = "<p>---已注册未开户每日弹窗：Fail-----"
    output6 = out
#groups=2&type==4为开户未激活每日弹窗接口
data7 = {"groups":"1","type":"4"}
data7 = urllib.urlencode(data7)
url2 = urllib2.Request(url1,data7)
response7 = json.loads(urllib2.urlopen(url2).read())['code']
if response7 == 1:
    out = "<p>---开户未激活每日弹窗：Success----" 
    output7 = out
else:
    out = "<p>---开户未激活每日弹窗：Fail-------"
    output7 = out
#groups=3&type==4为激活用户每日弹窗接口
data8 = {"groups":"1","type":"4"}
data8 = urllib.urlencode(data8)
url2 = urllib2.Request(url1,data8)
response8 = json.loads(urllib2.urlopen(url2).read())['code']
if response8 == 1:
    out = "<p>---激活用户每日弹窗：Success----" 
    output8 = out
else:
    out = "<p>---激活用户每日弹窗：Fail-------"
    output8 = out

url3 = 'http://v.dx168.com/tools-apis/pushMessageHistory/zp/list'
#游客状态下重要提醒
data9 = {"groupsId":"0"}
data9 = urllib.urlencode(data9)
url2 = urllib2.Request(url3,data9)
response9 = json.loads(urllib2.urlopen(url2).read())['code']
if response9 == 1:
    out = "<p>---游客状态下重要提醒：Success--" 
    output9 = out
else:
    out = "<p>---游客状态下重要提醒：Fail-----"
    output9 = out
#注册未开户状态下重要提醒
data10 = {"groupsId":"1"}
data10 = urllib.urlencode(data10)
url2 = urllib2.Request(url3,data10)
response10 = json.loads(urllib2.urlopen(url2).read())['code']
if response10 == 1:
    out = "<p>---注册未开户重要提醒：Success----" 
    output10 = out
else:
    out = "<p>---注册未开户重要提醒：Fail-------"
    output10 = out
#开户未激活重要提醒
data11 = {"groupsId":"2"}
data11 = urllib.urlencode(data11)
url2 = urllib2.Request(url3,data11)
response11 = json.loads(urllib2.urlopen(url2).read())['code']
if response11 == 1:
    out = "<p>---开户未激活重要提醒：Success----" 
    output11 = out
else:
    out = "<p>---开户未激活重要提醒：Fail-------"
    output11 = out
#激活重要提醒
data12 = {"groupsId":"3"}
data12 = urllib.urlencode(data12)
url2 = urllib2.Request(url3,data12)
response12 = json.loads(urllib2.urlopen(url2).read())['code']
if response12 == 1:
    out = "<p>---激活重要提醒：Success--------" 
    output12 = out
else:
    out = "<p>---激活重要提醒：Fail-----------"
    output12 = out
output = output1+output2+output3+output4+output5+output6+output7+output8+output9+output10+output11+output12
#发送邮件模块
# 第三方 SMTP 服务
#设置服务器
mail_host="smtp.126.com"
#用户名
mail_user="stone9903@126.com"
#口令
mail_pass="wzl62300" 
sender = 'stone9903@126.com'
# 接收邮件邮箱
receivers = '363800664@qq.com'
time = time.strftime("执行时间为：" + "%Y-%m-%d %H:%M:%S", time.localtime())
message = MIMEText(time+output,'html','utf-8')
message['From'] = "QA Automation"+"<"+mail_user+">"
message['To'] =  receivers
subject = '大象中盘后台接口自动化测试'
message['Subject'] = subject
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "Success: 邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
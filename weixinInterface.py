# -*- coding: utf-8 -*-
import hashlib
import httplib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import tool
import database
 
class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.tool = tool.tool()
        self.db = database.database()
 
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="mengxw"
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):        
        datastr = web.data() #获得post来的数据
        xml = etree.fromstring(datastr)#进行XML解析
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text

		#测试获取运动数据
        if msgType == "text":
            content = xml.find("Content").text
            if len(content.split('-', 4)) == 3:
                sportData = self.tool.get_data(content)
                if sportData == {}:
                    return self.render.reply_text(fromUser, toUser, int(time.time()), "该时段没有数据")
                else:
                    return self.render.reply_text(fromUser, toUser, int(time.time()), repr(sportData[0]))
            return self.render.reply_text(fromUser, toUser, int(time.time()), "未知语义")

        #关注/取关事件响应
        if msgType == "event":
            event = xml.find("Event").text
            if event == "subscribe":
                userInfo = self.tool.get_user_msg(fromUser)
                if userInfo == {}:
                    self.db.user.insert(openid = fromUser)
                else:
                    self.db.user.insert(uname = userInfo["nickname"], openid = fromUser, imageurl = userInfo["headimgurl"])
                return self.render.reply_text(fromUser, toUser, int(time.time()), "使用说明")

            if event == "unsubscribe":
                self.db.user.delete(fromUser)
            
            if event == "CLICK":
                key = xml.find("EventKey").text
                if key == "info":
                    return self.render.reply_articles(fromUser,toUser,int(time.time()), fromUser)
                if key == "follower":
                    return self.render.reply_article(fromUser,toUser,int(time.time()), fromUser)

		#推送图文信息
        return self.render.reply_articles(fromUser,toUser,int(time.time()), fromUser)
        
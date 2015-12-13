# -*- coding: utf-8 -*-
import sys
if "test" not in sys.path:
    sys.path.append("test")

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
import random
import datetime

import unittest
import test_database
 
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
        msg_type=xml.find("MsgType").text
        from_user=xml.find("FromUserName").text
        to_user=xml.find("ToUserName").text

		#测试获取运动数据
        if msg_type == "text":
            content = xml.find("Content").text
            
            if content == "test database":
                self.db.weapon.insert(from_user, 15)
                self.db.weapon.insert(from_user, 16)
                self.db.weapon.insert(from_user, 17)
                self.db.weapon.insert(from_user, 18)
                self.db.weapon.insert(from_user, 19)
                suite_1 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_message)
                suite_2 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_user)
                suite_3 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_follower)
                suite_4 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_stranger)
                suite_5 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_bong)
                suite_6 = unittest.TestLoader().loadTestsFromTestCase(test_database.test_database_weapon)
                suite = unittest.TestSuite([])
                unittest.TextTestRunner(verbosity = 2).run(suite)
                return self.render.reply_text(from_user, to_user, int(time.time()), "accept database test")

            if content == "insert data":
                self.tool.get_data_from_txt()
                return self.render.reply_text(from_user, to_user, int(time.time()), "insert ok")

            if len(content.split('-', 4)) == 3:
                sport_data = self.tool.get_data(content)
                if sport_data == {}:
                    return self.render.reply_text(from_user, to_user, int(time.time()), "该时段没有数据")
                else:
                    return self.render.reply_text(from_user, to_user, int(time.time()), repr(sport_data[0]))
            
        
            if content.isdigit():
                uid = self.db.user.get(openid=from_user)
                self.db.stranger.insert(to_user=int(content), from_user=uid["id"])
                return self.render.reply_text(from_user, to_user,int(time.time()), "已将您的好友请求发送。")
            
            return self.render.reply_text(from_user, to_user, int(time.time()), "未知语义")

        #关注/取关事件响应
        if msg_type == "event":
            event = xml.find("Event").text
            if event == "subscribe":
                userInfo = self.tool.get_user_msg(from_user)
                if userInfo == {}:
                    self.db.user.insert(openid = from_user)
                else:
                    self.db.user.insert(openid = from_user, uname = userInfo["nickname"], headimgurl = userInfo["headimgurl"])
                self.db.weapon.insert(from_user, 1)
                return self.render.reply_text(from_user, to_user, int(time.time()), "使用说明")

            if event == "unsubscribe":
                self.db.user.delete(from_user)
                self.db.weapon.delete(from_user)
            
            if event == "CLICK":
                key = xml.find("EventKey").text
                if key == "info":
                    return self.render.reply_articles(from_user,to_user,int(time.time()), from_user)
                if key == "follower":
                    return self.render.reply_article(from_user,to_user,int(time.time()), from_user)
                if key == "rank":
                    return self.render.reply_rank(from_user,to_user,int(time.time()), from_user)
                if key == "signin":
                    last_date = self.db.user.get(openid=from_user)["signin_time"]
                    now_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    if last_date:
                        last_date = last_date.strftime("%Y-%m-%d")
                        if last_date == now_date:
                            return self.render.reply_text(from_user,to_user,int(time.time()), "今日已经签到。")
                    self.db.user.sign_in(from_user)
                    randid = random.randint(1,7)
                    randslogan = {"1":"流水不腐，户枢不蠹，动也。\n——吕不韦", "2":"更高，更快，更强。\n——亨利·马丁·提东", "3":"以自然之道，养自然之身。\n——欧阳修", "4":"生命在于运动。\n——伏尔泰", "5":"运动是一切生命的源泉。\n——达·芬奇", "6":"科学的基础是健康的身体。\n——居里夫人", "7":"为祖国健康工作五十年！"}
                    return self.render.reply_text(from_user,to_user,int(time.time()), randslogan["%d" %randid])
                if key == "pk":
                    return self.render.reply_pkpage(from_user,to_user,int(time.time()), from_user)
                    

		#推送图文信息
        return self.render.reply_articles(from_user,to_user,int(time.time()), from_user)
        
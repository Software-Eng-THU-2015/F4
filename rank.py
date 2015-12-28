# -*- coding: utf-8 -*-
import web
import os
import database
import datetime

class Rank:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        #获取GET请求中OpenID
        row = web.input()
        openid = row.openid
        myself = self.db.user.get(openid = openid)
        myid = myself["id"]
        #在数据库中查询用户运动数据
        date_today = datetime.datetime.now().strftime("%Y-%m-%d")
        newdata = self.db.follower.get(follower = myid)
        friends = []
        for fid in newdata:
            user = self.db.user.get(id = fid)
            if not user:
                break
            person = {}
            person["id"] = fid
            person["name"] = user["nickname"]
            person["openid"] = user["openid"]
            person["steps"] = self.db.bong.get_calories(openid = user["openid"], date = date_today)
            friends.append(person)
   		
        person = {}
        person["id"] = myid
        person["name"] = myself["nickname"]
        person["openid"] = myself["openid"]
        person["steps"] = self.db.bong.get_calories(openid = myself["openid"], date = date_today)
        friends.append(person)
        
        friends.sort(key = lambda e: e['steps'], reverse = True)
        
        #orted(friends, key = lambda person:person.steps, reverse = True)
            
        return self.render.reply_ranks(friends, myid)
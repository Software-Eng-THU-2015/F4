# -*- coding: utf-8 -*-
import web
import os
import database

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
        myid = self.db.user.get(openid=openid)["id"]
        #在数据库中查询用户运动数据
        newdata = self.db.follower.get(follower = myid)
        friends = []
        for fid in newdata:
            person = {}
            person["id"] = fid
            person["name"] = self.db.user.get(id=fid)["nickname"]
            person["openid"] = self.db.user.get(id=fid)["openid"]
            person["steps"] = 300
            friends.append(person)
   		
        person = {}
        person["id"] = myid
        person["name"] = self.db.user.get(id=myid)["nickname"]
        person["openid"] = self.db.user.get(id=myid)["openid"]
        person["steps"] = 1000
        friends.append(person)
        
        #orted(friends, key = lambda person:person.steps, reverse = True)
            
        return self.render.reply_ranks(friends, myid)
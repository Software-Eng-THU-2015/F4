# -*- coding: utf-8 -*-
import web
import os
import database
from settings import SITE_DOMAIN

class Confirm:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        #获取GET请求中OpenID
        row = web.input()
        flrid = row.flrid
        fleid = row.fleid
        mytype = row.type
        flrname = self.db.user.get(id = flrid)["nickname"]
        flename = self.db.user.get(id = fleid)["openid"]

        if row.type == "1":
            if self.db.follower.is_followed(fleid, flrid) == 0:
        	    self.db.follower.insert(fleid, flrid)
            result = "您已通过好友申请"
        else:
            result = "您已拒绝好友申请" 
        self.db.stranger.delete(to_user = fleid, from_user = flrid)
        
        return self.render.reply_confirm(flrname, flename, result, SITE_DOMAIN)
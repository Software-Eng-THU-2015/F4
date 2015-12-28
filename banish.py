# -*- coding: utf-8 -*-
import web
import os
import database
from settings import SITE_DOMAIN

class Banish:
    
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
        flruser = self.db.user.get(openid = flrid)
        fleuser = self.db.user.get(id = fleid)
        flrname = flruser["nickname"]
        flename = fleuser["openid"]
        flrid = flruser["id"]

        if self.db.follower.is_followed(follower_a=flrid, follower_b=fleid):
            self.db.follower.delete(follower_a=flrid, follower_b=fleid)
            result = "好友关系解除。"
        else:
            result = "你们并不是好友。" 
        
        return self.render.reply_confirm(flrname, flename, result, SITE_DOMAIN)
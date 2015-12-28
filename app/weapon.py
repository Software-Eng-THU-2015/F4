# -*- coding: utf-8 -*-
import web
import os
import database
import datetime
import string
from settings import SITE_DOMAIN

class Weapon:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        #获取GET请求中OpenID
        row = web.input()
        uid = row.uid
        wid = row.wid
        my = self.db.user.get(id=uid)
        openid = my["openid"]
        if my["point"] < 100:
            result = 0
            return self.render.reply_weapon(openid, result, SITE_DOMAIN)
        if self.db.weapon.insert(openid, wid) == -1:
            nid = string.atoi(wid) + 7
            if my["point"] < 500:
                result = 0
                return self.render.reply_weapon(openid, result, SITE_DOMAIN)
            self.db.weapon.update(openid, wid, nid)
            point = my["point"] - 500
            self.db.user.update_point(openid, new_point = point)
        else:
            point = my["point"] - 100
            self.db.user.update_point(openid, new_point = point)
        
        result = 1
        return self.render.reply_weapon(openid, result, SITE_DOMAIN)
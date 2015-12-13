# -*- coding: utf-8 -*-
import web
import os
import database
import datetime
import string

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
        openid = self.db.user.get(id=uid)["openid"]
        if self.db.weapon.insert(openid, wid) == -1:
            nid = string.atoi(wid) + 7
            self.db.weapon.update(openid, wid, nid)
        
        return self.render.reply_weapon()
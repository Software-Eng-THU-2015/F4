# -*- coding: utf-8 -*-
import web
import os
import database

class Body:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        row = web.input()
        openid = row.openid
        my = self.db.user.get(openid = openid)
        myy = self.db.plan.get(openid = openid)
        
        myself = {}
        
        myself["Uname"] = my["nickname"]
        myself["id"] = my["id"]
        if myy == {}:
            myself["height"] = 0
            myself["weight"] = 0
        else:
            myself["height"] = myy["height"]
            myself["weight"] = myy["weight"]
        myself["point"] = my["point"]
        myself["total_point"] = my["total_point"]
        
        return self.render.reply_personalInfo(myself)
        
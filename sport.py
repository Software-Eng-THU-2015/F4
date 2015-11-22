# -*- coding: utf-8 -*-
import web
import os
import database

class Sport:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        #获取GET请求中OpenID
        row = web.input()
        openid = row.openid

        #在数据库中查询用户运动数据
        data = self.db.sport.get(openid)
        return self.render.reply_sport(data[0].Step,data[1].Step,data[2].Step,data[3].Step,data[4].Step,data[5].Step,data[6].Step)
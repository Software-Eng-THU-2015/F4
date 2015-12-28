# -*- coding: utf-8 -*-
import web
import os
import database
import datetime

class Sleep:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):

        row = web.input()
        openid = row.openid

        #在数据库中查询用户运动数据
        data = []
        date_today = datetime.datetime.now().strftime("%Y-%m-%d")

        for i in range(7):
            sleeps = self.db.bong.get_sleep(openid, date_today)
            data.append(sleeps)            
            date_today = datetime.datetime.strptime(date_today, "%Y-%m-%d") - datetime.timedelta(days = 1)
            date_today = date_today.strftime("%Y-%m-%d")

        return self.render.reply_sleep(data)
# -*- coding: utf-8 -*-
import web
import os
import database
import datetime
from settings import SITE_DOMAIN

class Info:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):

        row = web.input()
        openid = row.openid
        myid = row.myid
        #在数据库中查询用户运动数据
        data1 = []
        data2 = []
        date_today = datetime.datetime.now().strftime("%Y-%m-%d")

        for i in range(7):
            calories = self.db.bong.get_calories(openid, date_today)
            data1.append(calories)
            date_today = datetime.datetime.strptime(date_today, "%Y-%m-%d") - datetime.timedelta(days = 1)
            date_today = date_today.strftime("%Y-%m-%d")

        for i in range(7):
            sleeps = self.db.bong.get_sleep(openid, date_today)
            data2.append(sleeps)
            date_today = datetime.datetime.strptime(date_today, "%Y-%m-%d") - datetime.timedelta(days = 1)
            date_today = date_today.strftime("%Y-%m-%d")

        return self.render.reply_info(data1, data2, myid, openid, SITE_DOMAIN)
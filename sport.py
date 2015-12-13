# -*- coding: utf-8 -*-
import web
import os
import database
import datetime

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
        data = []
        date_today = "2015-11-17"

        for i in range(7):
        	calories = self.db.bong.get_calories(openid, date_today)
        	data.append(calories)
        	date_today = datetime.datetime.strptime(date_today, "%Y-%m-%d") - datetime.timedelta(days = 1)
        	date_today = date_today.strftime("%Y-%m-%d")
        
        goal_calos = self.db.plan.get(openid=openid)
        if goal_calos:
            goal_calo = goal_calos["goal_calo"]
        else:
            goal_calo = "尚未制定计划"

        return self.render.reply_sport(data, openid, goal_calo)
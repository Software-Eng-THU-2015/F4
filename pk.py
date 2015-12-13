# -*- coding: utf-8 -*-
import web
import os
import database
import datetime

class Pk:
    
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
        friend_data = self.db.follower.get(follower = myid)
        friends = []
        for fid in friend_data:
            person = {}
            person["id"] = fid
            person["name"] = self.db.user.get(id=fid)["nickname"]
            person["openid"] = self.db.user.get(id=fid)["openid"]
            friends.append(person)

        weaponlist = {"1":"拳套", "2":"大刀", "3":"短剑","5":"拳法","6":"长枪","7":"弓箭","8":"天马流星拳","9":"青龙偃月刀","10":"饮血剑","12":"七伤拳","13":"朗基奴斯枪","14":"丘比特之箭","15":"西西弗斯的意志","16":"因果律武器","17":"荆轲刺秦","18":"剪子包袱锤","19":"飞龙探云手"}
        weapons = []
        weapon_tobuy = [1,2,3,5,6,7]
        weapon_data = self.db.weapon.get(openid)
        for weapon in weapon_data:
            w = {}
            w["code"] = weapon
            w["name"] = weaponlist["%d" %weapon]
            if weapon > 7:
                w["upd"] = 0
            else:
                w["upd"] = 1
            weapons.append(w)
            try:
                weapon_tobuy.remove(weapon)
            except:
                pass

            try:
                weapon_tobuy.remove(weapon-7)
            except:
                pass

        newweapons = []
        for weapon in weapon_tobuy:
            w = {}
            w["code"] = weapon
            w["name"] = weaponlist["%d" %weapon]
            newweapons.append(w)

 
        return self.render.reply_pk(friends, weapons, newweapons, myid)
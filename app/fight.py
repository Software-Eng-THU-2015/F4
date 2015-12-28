# -*- coding: utf-8 -*-
import web
import os
import database
import datetime
import random

class Fight:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
        self.db = database.database()
    
    def GET(self):
        #获取GET请求中OpenID
        row = web.input()
        uid = row.uid
        fid = row.fid
        openid_1 = self.db.user.get(id = uid)["openid"]
        fighter_1 = self.db.user.get(id = uid)["nickname"]
        openid_2 = self.db.user.get(id = fid)["openid"]
        fighter_2 = self.db.user.get(id = fid)["nickname"]
        hp_1 = 100
        hp_2 = 100
        list_1 = self.db.weapon.get(openid_1)
        random.shuffle(list_1)
        list_2 = self.db.weapon.get(openid_2)
        random.shuffle(list_2)
        data = []
        hp1 = []
        hp2 = []

        while True:
            index = random.randint(1,10)
            if index < 7: 
                if list_1:
                    weapon = list_1.pop()
                    if weapon == 1:
                        harm = random.randint(5,10)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"用拳头狠揍了" + fighter_2 + u"，造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 2:
                        harm = random.randint(8,12)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"耍出大刀，对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 3:
                        harm = random.randint(7,11)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"抖出剑花，对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 4:
                        harm = random.randint(6,8)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"向" + fighter_2 + u"砸板砖，造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 5:
                        harm = random.randint(4,9)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"用拳头狠揍了" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 6:
                        harm = random.randint(6,11)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"使出霸王枪，对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 7:
                        harm = random.randint(5,9)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"瞄准弓箭，对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 8:
                        harm = random.randint(12,20)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"打出天马流星拳！对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        

                        factor = random.randint(1,10)
                        if factor < 4:
                            harm = random.randint(12,20)
                            hp_2 -= harm
                            sharm = "%d" %harm
                            desc += fighter_1 + u"打出天马流星拳第二段！对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 9:
                        if hp_2 < 36:
                            hp_2 = 0
                            desc = fighter_1 + u"用青龙偃月刀斩杀了" + fighter_2 + u"！"
                        else:
                            harm = random.randint(15,25)
                            hp_2 -= harm
                            sharm = "%d" %harm
                            desc = fighter_1 + u"耍出青龙偃月刀！对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                            data.append(desc)
                    elif weapon == 10:
                        harm = random.randint(18,24)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        hp_1 += 5
                        if hp_1 > 100:
                            hp_1 = 100
                        desc = fighter_1 + u"饮血剑刺出！对" + fighter_2 + u"造成了" + sharm + u"点伤害，恢复自身5点生命"
                        data.append(desc)
                    elif weapon == 12:
                        harm = random.randint(20,30)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        hp_1 -= 5
                        desc = fighter_1 + u"打出了七伤拳！对" + fighter_2 + u"造成了" + sharm + u"点伤害，同时自身损失5点生命"
                        data.append(desc)
                    elif weapon == 13:
                        factor = random.randint(1,2)
                        if factor == 1:
                            hp_2 = 1
                            desc = fighter_1 + u"祭出了朗基努斯枪！使" + fighter_2 + u"进入濒死状态！"
                            data.append(desc)
                        else:
                            harm = random.randint(13,15)
                            hp_2 -= harm
                            sharm = "%d" %harm
                            desc = fighter_1 + u"用朗基奴斯枪对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                            data.append(desc)
                    elif weapon == 14:
                        harm = random.randint(10,15)
                        hp_2 -= harm
                        sharm = "%d" %harm
                        desc = fighter_1 + u"射出爱神丘比特之箭！对" + fighter_2 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 31:
                        hp_1 = 100
                        desc = fighter_1 + u"继承了西西弗斯的意志！生命完全恢复！"
                        data.append(desc)
                    elif weapon == 32:
                        hp_2 = hp_1
                        hp_2 -= 10
                        desc = fighter_1 + u"发动了因果律武器！同时对" + fighter_2 + u"造成了10点伤害"
                        data.append(desc)
                    elif weapon == 33:
                        hp_2 -= hp_1
                        sharm = "%d" %hp_1
                        hp_1 = 1
                        desc = fighter_1 + u"决定荆轲刺秦！要与" + fighter_2 + u"同归于尽！造成" + sharm + u"伤害，自身濒死"
                        data.append(desc)
                    elif weapon == 34:
                        factor = random.randint(1,2)
                        if factor == 1:
                            hp_2 -= 30
                            desc = fighter_1 + u"剪子包袱锤获胜！对" + fighter_2 + u"造成30点伤害"
                            data.append(desc)
                        else:
                            hp_1 -= 5
                            desc = fighter_1 + u"剪子包袱锤失败！损失5点生命"
                            data.append(desc)
                    elif weapon == 35:
                        if list_2:
                            weapon = list_2.pop()
                            list_1.append(weapon)
                            desc = fighter_1 + u"使出飞龙探云手！偷走了" + fighter_2 + u"的一件装备"
                            data.append(desc)
                        else:
                            harm = random.randint(5,10)
                            hp_2 -= harm
                            sharm = "%d" %harm
                            desc = fighter_1 + u"用拳头狠揍了" + fighter_2 + u"，造成了" + sharm + u"点伤害"
                            data.append(desc)

                else:
                    harm = random.randint(5,10)
                    hp_2 -= harm
                    sharm = "%d" %harm
                    desc = fighter_1 + u"用拳头狠揍了" + fighter_2 + u"，造成了" + sharm + u"点伤害"
                    data.append(desc)
            else:
                harm = random.randint(5,10)
                hp_2 -= harm
                sharm = "%d" %harm
                desc = fighter_1 + u"用拳头狠揍了" + fighter_2 + u"，造成了" + sharm + u"点伤害"
                data.append(desc)


            hp1.append(hp_1)
            hp2.append(hp_2)

            if hp_2 < 1:
                result = fighter_1 + u"战胜了" + fighter_2 + u"！"
                hp2[-1] = 0
                break

            if hp_1 < 1:
                result = fighter_2 + u"战胜了" + fighter_1 + u"！"
                hp1[-1] = 0
                break

            index = random.randint(1,10)
            if index < 7: 
                if list_2:
                    weapon = list_2.pop()
                    if weapon == 1:
                        harm = random.randint(5,10)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"用拳头狠揍了" + fighter_1 + u"，造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 2:
                        harm = random.randint(8,12)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"耍出大刀，对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 3:
                        harm = random.randint(7,11)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"抖出剑花，对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 4:
                        harm = random.randint(6,8)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"向" + fighter_1 + u"砸板砖，造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 5:
                        harm = random.randint(4,9)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"用拳头狠揍了" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 6:
                        harm = random.randint(6,11)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"使出霸王枪，对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 7:
                        harm = random.randint(5,9)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"瞄准弓箭，对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 8:
                        harm = random.randint(12,20)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"打出天马流星拳！对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        

                        factor = random.randint(1,10)
                        if factor < 4:
                            harm = random.randint(12,20)
                            hp_1 -= harm
                            sharm = "%d" %harm
                            desc += fighter_2 + u"打出天马流星拳第二段！对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 9:
                        if hp_1 < 36:
                            hp_1 = 0
                            desc = fighter_2 + u"用青龙偃月刀斩杀了" + fighter_1 + u"！"
                        else:
                            harm = random.randint(15,25)
                            hp_1 -= harm
                            sharm = "%d" %harm
                            desc = fighter_2 + u"耍出青龙偃月刀！对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                            data.append(desc)
                    elif weapon == 10:
                        harm = random.randint(18,24)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        hp_2 += 5
                        if hp_2 > 100:
                            hp_2 = 100
                        desc = fighter_2 + u"饮血剑刺出！对" + fighter_1 + u"造成了" + sharm + u"点伤害，恢复自身5点生命"
                        data.append(desc)
                    elif weapon == 12:
                        harm = random.randint(20,30)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        hp_2 -= 5
                        desc = fighter_2 + u"打出了七伤拳！对" + fighter_1 + u"造成了" + sharm + u"点伤害，同时自身损失5点生命"
                        data.append(desc)
                    elif weapon == 13:
                        factor = random.randint(1,2)
                        if factor == 1:
                            hp_1 = 1
                            desc = fighter_2 + u"祭出了朗基努斯枪！使" + fighter_1 + u"进入濒死状态！"
                            data.append(desc)
                        else:
                            harm = random.randint(13,15)
                            hp_1 -= harm
                            sharm = "%d" %harm
                            desc = fighter_2 + u"用朗基奴斯枪对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                            data.append(desc)
                    elif weapon == 14:
                        harm = random.randint(10,15)
                        hp_1 -= harm
                        sharm = "%d" %harm
                        desc = fighter_2 + u"射出爱神丘比特之箭！对" + fighter_1 + u"造成了" + sharm + u"点伤害"
                        data.append(desc)
                    elif weapon == 31:
                        hp_2 = 100
                        desc = fighter_2 + u"继承了西西弗斯的意志！生命完全恢复！"
                        data.append(desc)
                    elif weapon == 32:
                        hp_1 = hp_2
                        hp_1 -= 10
                        desc = fighter_2 + u"发动了因果律武器！同时对" + fighter_1 + u"造成了10点伤害"
                        data.append(desc)
                    elif weapon == 33:
                        hp_1 -= hp_2
                        sharm = "%d" %hp_2
                        hp_2 = 1
                        desc = fighter_2 + u"决定荆轲刺秦！要与" + fighter_1 + u"同归于尽！造成" + sharm + u"伤害，自身濒死"
                        data.append(desc)
                    elif weapon == 34:
                        factor = random.randint(1,2)
                        if factor == 1:
                            hp_1 -= 30
                            desc = fighter_2 + u"剪子包袱锤获胜！对" + fighter_1 + u"造成30点伤害"
                            data.append(desc)
                        else:
                            hp_2 -= 5
                            desc = fighter_2 + u"剪子包袱锤失败！损失5点生命"
                            data.append(desc)
                    elif weapon == 35:
                        if list_1:
                            weapon = list_1.pop()
                            list_2.append(weapon)
                            desc = fighter_2 + u"使出飞龙探云手！偷走了" + fighter_1 + u"的一件装备"
                            data.append(desc)
                        else:
                            harm = random.randint(5,10)
                            hp_1 -= harm
                            sharm = "%d" %harm
                            desc = fighter_2 + u"用拳头狠揍了" + fighter_1 + u"，造成了" + sharm + u"点伤害"
                            data.append(desc)
                else:
                    harm = random.randint(5,10)
                    hp_1 -= harm
                    sharm = "%d" %harm
                    desc = fighter_2 + u"用拳头狠揍了" + fighter_1 + u"，造成了" + sharm + u"点伤害"
                    data.append(desc)
            else:
                harm = random.randint(5,10)
                hp_1 -= harm
                sharm = "%d" %harm
                desc = fighter_2 + u"用拳头狠揍了" + fighter_1 + u"，造成了" + sharm + u"点伤害"
                data.append(desc)

            hp1.append(hp_1)
            hp2.append(hp_2)

            if hp_1 < 1:
                result = fighter_2 + u"战胜了" + fighter_1 + u"！"
                hp1[-1] = 0
                break

            if hp_2 < 1:
                result = fighter_1 + u"战胜了" + fighter_2 + u"！"
                hp2[-1] = 0
                break

        return self.render.reply_fight(fighter_1, fighter_2, data, hp1, hp2, result, len(hp1))
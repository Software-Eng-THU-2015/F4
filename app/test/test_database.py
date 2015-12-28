# -*- coding: utf-8 -*-
import unittest
import database

class test_database_message(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()
		self.test_token = "test_token"
		
	def tearDown(self):
		pass

	def test_message_get_token(self):
		self.assertNotEqual(self.test_class.message.get_token(), "")

	def test_message_get_appid(self):
		self.assertNotEqual(self.test_class.message.get_appid(), "")

	def test_message_get_appsecret(self):
		self.assertNotEqual(self.test_class.message.get_appsecret(), "")

	def test_message_update_token(self):
		self.test_class.message.update_token(self.test_token)
		self.assertEqual(self.test_class.message.get_token(), self.test_token)

class test_database_user(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()
		self.test_user = {"openid": "testuser", "nickname": "username", "headimgurl": "http://baidu.com", "point": 0, "total_point": 0, "signin_time": None}
		self.test_new_user = {"openid": "testuser", "nickname": "new_username", "headimgurl": "new_headimgurl", "point": 0, "total_point": 0, "signin_time": None}

	def tearDown(self):
		pass

	def test_user_insert_get(self):
		self.test_class.user.insert(openid = self.test_user["openid"], uname = self.test_user["nickname"], headimgurl = self.test_user["headimgurl"])
		#通过openid查询
		query_user_openid = self.test_class.user.get(openid = self.test_user["openid"])
		self.test_user["id"] = query_user_openid["id"]
		self.assertEqual(query_user_openid, self.test_user)
		#通过id查询
		query_user_id = self.test_class.user.get(id = query_user_openid["id"])
		self.assertEqual(query_user_id, self.test_user)

		self.test_class.user.delete(openid = self.test_user["openid"])

	def test_user_update(self):
		self.test_class.user.insert(openid = self.test_user["openid"], uname = self.test_user["nickname"], headimgurl = self.test_user["headimgurl"])
		#同时更新uname和headimgurl
		self.test_class.user.update(openid = self.test_user["openid"], uname = self.test_new_user["nickname"], headimgurl = self.test_new_user["headimgurl"])
		query_user = self.test_class.user.get(openid = self.test_user["openid"])
		self.test_new_user["id"] = query_user["id"]
		self.assertEqual(query_user, self.test_new_user)
		#仅更新uname
		self.test_class.user.update(openid = self.test_user["openid"], uname = self.test_user["nickname"])
		self.assertEqual(self.test_class.user.get(openid = self.test_user["openid"])["nickname"], self.test_user["nickname"])
		#仅更新headimgurl
		self.test_class.user.update(openid = self.test_user["openid"], headimgurl = self.test_user["headimgurl"])
		self.assertEqual(self.test_class.user.get(openid = self.test_user["openid"])["headimgurl"], self.test_user["headimgurl"])

		self.test_class.user.delete(openid = self.test_user["openid"])

	def test_user_delete(self):
		self.test_class.user.insert(openid = self.test_user["openid"], uname = self.test_user["nickname"], headimgurl = self.test_user["headimgurl"])
		self.test_class.user.delete(openid = self.test_user["openid"])
		self.assertEqual(self.test_class.user.get(openid = self.test_user["openid"]), {})

	def test_user_sign_in(self):
		self.test_class.user.insert(openid = self.test_user["openid"], uname = self.test_user["nickname"], headimgurl = self.test_user["headimgurl"])
		self.test_class.user.sign_in(openid = self.test_user["openid"])
		self.assertNotEqual(self.test_class.user.get(openid = self.test_user["openid"])["signin_time"], "0000-00-00 00:00:00")
		self.test_class.user.delete(openid = self.test_user["openid"])

class test_database_follower(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()
		self.follower_a = -10000
		self.follower_b = -10001

	def tearDown(self):
		pass

	def test_follower_insert_get(self):
		self.test_class.follower.insert(self.follower_a, self.follower_b)
		self.assertIn(self.follower_b, self.test_class.follower.get(self.follower_a))
		self.assertIn(self.follower_a, self.test_class.follower.get(self.follower_b))
		self.test_class.follower.delete(self.follower_a, self.follower_b)

	def test_follower_delete(self):
		self.test_class.follower.insert(self.follower_a, self.follower_b)
		self.test_class.follower.delete(self.follower_a, self.follower_b)
		self.assertNotIn(self.follower_b, self.test_class.follower.get(self.follower_a))
		self.assertNotIn(self.follower_a, self.test_class.follower.get(self.follower_b))

	def test_follower_is_followed(self):
		self.assertEqual(self.test_class.follower.is_followed(self.follower_a, self.follower_b), 0)
		self.test_class.follower.insert(self.follower_a, self.follower_b)
		self.assertEqual(self.test_class.follower.is_followed(self.follower_a, self.follower_b), 1)
		self.test_class.follower.delete(self.follower_a, self.follower_b)

class test_database_stranger(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()
		self.to_user = -10000
		self.from_user = -10001

	def tearDown(self):
		pass

	def test_stranger_insert_get(self):
		self.test_class.stranger.insert(to_user = self.to_user, from_user = self.from_user)
		self.assertIn(self.from_user, self.test_class.stranger.get(self.to_user))
		self.test_class.stranger.delete(to_user = self.to_user, from_user = self.from_user)

	def test_stranger_delete(self):
		self.test_class.stranger.insert(to_user = self.to_user, from_user = self.from_user)
		self.test_class.stranger.delete(to_user = self.to_user, from_user = self.from_user)
		self.assertNotIn(self.from_user, self.test_class.stranger.get(self.to_user))

class test_database_bong(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()

		self.date_calo = "2029-12-25"
		self.data_calo_1 = {"openid": "calo_test", "startTime": "2029-12-25 0:0:0", "endTime": "2029-12-25 13:13:13", "type": 2, "subType": 2, "calories": 200}
		self.data_calo_2 = {"openid": "calo_test", "startTime": "2029-12-25 13:33:33", "endTime": "2029-12-25 23:33:33", "type": 2, "subType": 2, "calories": 300}
		self.data_calo_3 = {"openid": "calo_test", "startTime": "2029-12-26 0:0:0", "endTime": "2029-12-26 23:33:33", "type": 2, "subType": 2, "calories": 400}

		self.date_sleep = "2029-12-25"
		self.data_sleep_1 = {"openid": "calo_test", "startTime": "2029-12-24 0:0:0", "endTime": "2029-12-25 0:0:0", "type": 1, "subType": 2, "dsNum": 100, "lsNum": 200}
		self.data_sleep_2 = {"openid": "calo_test", "startTime": "2029-12-24 13:33:33", "endTime": "2029-12-25 23:33:33", "type": 1, "subType": 2, "dsNum": 300, "lsNum": 400}
		self.data_sleep_3 = {"openid": "calo_test", "startTime": "2029-12-25 0:0:0", "endTime": "2029-12-26 0:0:0", "type": 1, "subType": 2, "dsNum": 500, "lsNum": 600}

	def tearDown(self):
		self.test_class.bong.delete(self.data_calo_1["openid"])
		self.test_class.bong.delete(self.data_sleep_1["openid"])

	def test_bong_get_calories(self):
		self.test_class.bong.insert(self.data_calo_1)
		self.test_class.bong.insert(self.data_calo_2)
		self.test_class.bong.insert(self.data_calo_3)

		self.assertEqual(self.test_class.bong.get_calories(self.data_calo_1["openid"], self.date_calo), self.data_calo_1["calories"] + self.data_calo_2["calories"])

	def test_bong_get_sleep(self):
		self.test_class.bong.insert(self.data_sleep_1)
		self.test_class.bong.insert(self.data_sleep_2)
		self.test_class.bong.insert(self.data_sleep_3)

		self.assertEqual(self.test_class.bong.get_sleep(self.data_sleep_1["openid"], self.date_sleep), {"dsleep": self.data_sleep_1["dsNum"] + self.data_sleep_2["dsNum"], "lsleep": self.data_sleep_1["lsNum"] + self.data_sleep_2["lsNum"]})

class test_database_weapon(unittest.TestCase):
	def setUp(self):
		self.test_class = database.database()
		self.test_openid = "test_openid"
		self.test_weaponcode = 11
		self.test_new_weaponcode = 22

	def tearDown(self):
		pass

	def test_weapon_insert_get(self):
		self.test_class.weapon.insert(openid = self.test_openid, weaponcode = self.test_weaponcode)
		self.assertEqual(self.test_class.weapon.get(openid = self.test_openid), [self.test_weaponcode])
		self.assertEqual(self.test_class.weapon.insert(openid = self.test_openid, weaponcode = self.test_weaponcode), -1)
		self.test_class.weapon.delete(openid = self.test_openid)

	def test_weapon_update(self):
		self.test_class.weapon.insert(openid = self.test_openid, weaponcode = self.test_weaponcode)
		self.test_class.weapon.update(openid = self.test_openid, old_weaponcode = self.test_weaponcode, new_weaponcode = self.test_new_weaponcode)
		self.assertEqual(self.test_class.weapon.get(openid = self.test_openid), [self.test_new_weaponcode])
		self.test_class.weapon.delete(openid = self.test_openid)

	def test_weapon_delete(self):
		self.test_class.weapon.insert(openid = self.test_openid, weaponcode = self.test_weaponcode)
		self.test_class.weapon.delete(openid = self.test_openid)
		self.assertEqual(self.test_class.weapon.get(openid = self.test_openid), [])
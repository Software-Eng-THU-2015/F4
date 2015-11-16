import web
import sae

class database():
	def __init__(self):
		self.db = web.database(
				dbn="mysql",  
				db=sae.const.MYSQL_DB,  
				user=sae.const.MYSQL_USER,  
				pw=sae.const.MYSQL_PASS,  
				host=sae.const.MYSQL_HOST,  
				port=int(sae.const.MYSQL_PORT),  
			)

	def query_token(self):
		return self.db.query('select * from AccessToken where id=1')[0].Token

	def update_token(self, accessToken):
		self.db.update('AccessToken', where = "id = 1", Token = accessToken)

	def insert_user(self, uname, openid, imageurl):
		self.db.insert('User', Uname = uname, OpenID = openid, ImageUrl = imageurl)

	def delete_user(self, openid):
		self.db.delete("User", where = "OpenID = $id", vars = {"id": openid, })

	def query_sport(self, openid):
		return self.db.query("select * from Sport where UserID = $id", vars = {"id": openid, })
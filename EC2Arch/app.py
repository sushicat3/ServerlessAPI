from flask import Flask
from flask import request
from flask import jsonify

sys.path.append('./lib')
import psycopg2

app = Flask(__name__)

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='musicbrainz.cw2va02rdk2z.us-east-1.rds.amazonaws.com' password='musicbrainz' port='5432'")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			print('cannot connect to database')

	def get_users(self):
		select_command = 'select * from users'
		self.cursor.execute(select_command)
		users = self.cursor.fetchall()
		users_json = {}
		users_json['users'] = []
		for user in users:
			user_json = {}
			user_json['user_id'] = user[0]
			user_json['username'] = user[1]
			user_json['created_on'] = str(user[2])
			users_json['users'].append(user_json)
		
		return users_json

	def add_user(self, username):
		insert_command = "insert into users (username, created_on) values ('" + username + "', current_timestamp);"
		
		try:
			self.cursor.execute(insert_command)
			return self.cursor.statusmessage
		except psycopg2.Error as e:
			return e.pgerror

	def get_posts(self):
		select_command = 'select * from posts'
		self.cursor.execute(select_command)
		posts = self.cursor.fetchall()
		posts_json = {}
		posts_json['posts'] = []
		for post in posts:
			post_json = {}
			post_json['post_id'] = post[0]
			post_json['post'] = post[1]
			post_json['created_on'] = str(post[2])
			post_json['user_id'] = post[3]
			posts_json['posts'].append(post_json)
		
		return posts_json

	def get_posts_by_id(self, id):
		select_command = 'select * from posts where post_id =' + id 
		self.cursor.execute(select_command)
		post = self.cursor.fetchone()
		post_json = {}
		post_json['post_id'] = post[0]
		post_json['post'] = post[1]
		post_json['created_on'] = str(post[2])
		post_json['user_id'] = post[3]
		
		return post_json

	def get_posts_by_user_id(self, id):
		select_command = 'select * from posts where user_id =' + id 
		self.cursor.execute(select_command)
		posts = self.cursor.fetchall()
		posts_json = {}
		posts_json['posts'] = []
		for post in posts:
			post_json = {}
			post_json['post_id'] = post[0]
			post_json['post'] = post[1]
			post_json['created_on'] = str(post[2])
			post_json['user_id'] = post[3]
			posts_json['posts'].append(post_json)
		
		return posts_json

	def add_post(self, post, user_id):
		insert_command = "insert into posts (post, created_on, user_id) values ('" + post + "', current_timestamp, " + str(user_id) + ");"
		
		try:
			self.cursor.execute(insert_command)
			return self.cursor.statusmessage
		except psycopg2.Error as e:
			return e.pgerror

dbConn = DatabaseConnection()

@app.route('/users', methods=['GET', 'POST'])
def users():
	if request.method == 'GET': 
		return jsonify(dbConn.get_users())
	else:
		username = request.args.get('username')
		return jsonify(dbConn.add_user(username))

@app.route('/posts', methods=['GET', 'POST'])
def posts():	
	if request.method == 'GET':	
		return jsonify(dbConn.get_posts())
	else:
		post_json = request.get_json()
		post = post_json['post']
		user_id = post_json['user_id']
		return jsonify(dbConn.add_post(post, user_id))

@app.route('/posts/<int:post_id>', methods=['GET'])
def post_by_idb(post_id):
	return jsonify(get_posts_by_id(post_id))

@app.route('/posts/user/<int:user_id>', methods=['GET'])
def posts_by_user_id(user_id):
	return jsonify(dbConn.get_posts_by_user_id(user_id))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


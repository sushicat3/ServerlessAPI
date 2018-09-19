import json
import sys
import os

sys.path.append('./lib')
import psycopg2

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect("dbname='musicbrainz' user='musicbrainz' host='musicbrainz.cw2va02rdk2z.us-east-1.rds.amazonaws.com' password='musicbrainz' port='5432'")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			print('cannot connect to database')

	def get(self):
		select_command = 'select * from users'
		self.cursor.execute(select_command)

def request_handler(event, context):
	response = {}
	response['isBase64Encoded'] = False
	response['statusCode'] = 200

	headers = {'Content-Type': 'application/json'}
	response['headers'] = headers
	
	body = {}
	body['title'] = 'Come Together'
	body['artist'] = 'The Beatles'
	body['album'] = 'Abbey Road'

	response['body'] = json.dumps(body)

	data_conn = DatabaseConnection()
	print(data_conn.get())

	return response
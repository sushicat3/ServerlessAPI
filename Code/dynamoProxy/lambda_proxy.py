import json
import sys
import os
import boto3

client = boto3.client('dynamodb')

def get_users():
	response = client.scan(
		TableName='users',
		ReturnConsumedCapacity='TOTAL'
	)
	return response

def get_posts():
	response = client.scan(
		TableName='posts',
		ReturnConsumedCapacity='TOTAL'
	)
	return response


def request_handler(event, context):
	response = {}
	response['isBase64Encoded'] = False
	response['statusCode'] = 200

	headers = {'Content-Type': 'application/json'}
	response['headers'] = headers
	

	resources = event['pathParameters']['proxy'].split('/')
	method = event['httpMethod']
	if resources[0] == 'users':
		if method == 'GET':
			response['body'] = json.dumps(get_users())
		else:
			response['body'] = "Resource does not exist"
	elif resources[0] == 'posts':
		if method == 'GET':
			if (len(resources) == 1):
				response['body'] = json.dumps(get_posts())
		else:
			response['body'] = "Resource does not exist"
	else:
		response['body'] = "Resource does not exist"

	return response
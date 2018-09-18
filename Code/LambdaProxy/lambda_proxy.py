import json

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

	return response
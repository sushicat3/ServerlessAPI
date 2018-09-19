# ServerlessAPI

Framework for a Serverless API aimed at enabling and optimizing use of low-traffic & high-availibility microservices.

## Requirements:
* AWS CLI

## Usage

1. Clone the Repository

1. Install dependencies into "lib" folder.
```
cd Code/LambdaProxy
pip install -t lib <module>
cd lib
rm -r *.dist-info
```

	*Special instructions for psycopg2:*
	1. obtain compiled psycopg2 for Amazon Linux here: https://github.com/jkehler/awslambda-psycopg2
	1. follow instructions and copy into "lib" folder


1. Deploy a Cloudformation Stack named "serverless-api"
```
aws s3 mb <BUCKET>
./deploy.sh <BUCKET> serverless-api
```



# ServerlessAPI

Framework for a Serverless API aimed at enabling and optimizing use of low-traffic & high-availibility microservices.

More Info: https://docs.google.com/presentation/d/1ULwpLN9vEpZATCZJdgAa5lp8FK4yvtUE5jUBwgDMvXA/edit?usp=sharing

## Requirements:
* AWS CLI

## Usage

1. Clone the Repository

2. Install dependencies into "lib" folder.
```
cd Code/LambdaProxy
pip install -t lib <module>
cd lib
rm -r *.dist-info
```

3. Deploy a Cloudformation Stack named "serverless-api"
```
aws s3 mb <BUCKET>
./deploy.sh <BUCKET> serverless-api
```

*Special instructions for psycopg2:*
1. obtain compiled psycopg2 for Amazon Linux here: https://github.com/jkehler/awslambda-psycopg2
2. follow instructions and copy into "lib" folder


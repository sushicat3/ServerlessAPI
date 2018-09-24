#!/bin/bash

STACK_NAME=$1

USE_MSG="Usage: deploy.sh STACK_NAME"

if [ -z "$STACK_NAME" ]; then
  echo "Missing STACK_NAME"
  echo $USE_MSG
  exit 1
fi

# copy app to s3
if [ -f package.zip ]; then
	rm package.zip
fi

zip -r package.zip app.py lib

aws s3 cp package.zip s3://server-fwk/app.py

# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html
aws cloudformation create-stack \
	--stack-name $STACK_NAME \
	--template-body file://ELB.yml \
	--parameters \
		ParameterKey=VpcId,ParameterValue=vpc-10c81b6a \
		ParameterKey=Subnets,ParameterValue=subnet-18d78052\\,subnet-a270f0fe \
		ParameterKey=InstanceType,ParameterValue=t2.micro \
		ParameterKey=KeyName,ParameterValue=swetal-IAM-keypair \
	--capabilities CAPABILITY_IAM


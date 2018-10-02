#!/bin/bash

API_TYPE=$1
STACK_NAME=$2

USE_MSG="Usage: deploy.sh BUCKET API_TYPE (ec2|lambda) STACK_NAME"

if [ -z "$API_TYPE" ]; then
  echo "Missing API_TYPE and STACK_NAME"
  echo $USE_MSG
  exit 1
fi

if [ -z "$STACK_NAME" ]; then
  echo "Missing STACK_NAME"
  echo $USE_MSG
  exit 1
fi

# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html
aws cloudformation create-stack \
	--stack-name $STACK_NAME \
	--template-body file://postgresRDS.yml \
	--parameters \
		ParameterKey=apiType,ParameterValue=$API_TYPE
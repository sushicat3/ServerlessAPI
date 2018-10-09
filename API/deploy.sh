#!/bin/bash

BUCKET=$1
STACK_NAME=$2

USE_MSG="Usage: deploy.sh BUCKET STACK_NAME"

if [ -z "$BUCKET" ]; then
  echo "Missing BUCKET and STACK_NAME"
  echo $USE_MSG
  exit 1
fi

if [ -z "$STACK_NAME" ]; then
  echo "Missing STACK_NAME"
  echo $USE_MSG
  exit 1
fi

# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html
aws cloudformation package \
	--template-file serverless.yml \
	--s3-bucket $BUCKET \
	--output-template-file serverless-output.yml

# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/deploy/index.html
aws cloudformation deploy \
	--template-file serverless-output.yml \
	--stack-name $STACK_NAME \
	--capabilities CAPABILITY_IAM

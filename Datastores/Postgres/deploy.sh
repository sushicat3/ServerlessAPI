#!/bin/bash

STACK_NAME=$1

USE_MSG="Usage: deploy.sh BUCKET STACK_NAME"

if [ -z "$STACK_NAME" ]; then
  echo "Missing STACK_NAME"
  echo $USE_MSG
  exit 1
fi

# https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html
aws cloudformation create-stack \
	--stack-name $STACK_NAME \
	--template-body file://postgresRDS.yml
#!/usr/bin/env bash

REGION=eu-west-1
PLATFORM=docker
APP=hackathon-law

AWS_PROFILE="$1"

# Check if AWS_PROFILE is provided
if [ -z "$AWS_PROFILE" ]; then
  echo "Error: AWS_PROFILE parameter is missing."
  echo "Usage: ./create_ebs_application.sh <AWS_PROFILE>"
  exit 1
fi

# Create new application
eb init --profile $AWS_PROFILE --region $REGION --platform "Docker" $APP
echo 'finish'
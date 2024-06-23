#!/usr/bin/env bash

NAME_ENV=hackathon-law
AWS_PROFILE="$1"

# Check if AWS_PROFILE is provided
if [ -z "$AWS_PROFILE" ]; then
  echo "Error: AWS_PROFILE parameter is missing."
  echo "Usage: ./set_env_variables_into_ebs.sh <AWS_PROFILE>"
  exit 1
fi

# Set env variables
eb setenv --profile $AWS_PROFILE $(cat .env.production | xargs)
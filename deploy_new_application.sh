#!/usr/bin/env bash

NAME_ENV=hackathon-law
CNAME=hackathon-data-privacy
AWS_PROFILE="$1"

# Check if AWS_PROFILE is provided
if [ -z "$AWS_PROFILE" ]; then
  echo "Error: AWS_PROFILE parameter is missing."
  echo "Usage: ./deploy_new_application.sh <AWS_PROFILE>"
  exit 1
fi

# Create .ebextensions directory and load_balancer.config file
mkdir -p .ebextensions

cat <<EOL > .ebextensions/load_balancer.config
option_settings:
  aws:elbv2:listener:default:
    80/Protocol: TCP
EOL

# Deploy on t3 micro as it uses less than 1GB of ram
echo 'Deploy version to AWS EBS'
eb create --profile $AWS_PROFILE $NAME_ENV -i t3.small -c $CNAME --elb-type classic --platform "Docker"

# Get env variables
eb setenv --profile $AWS_PROFILE $(cat .env.production | xargs)

# Redeploy again
eb deploy --profile $AWS_PROFILE $NAME_ENV
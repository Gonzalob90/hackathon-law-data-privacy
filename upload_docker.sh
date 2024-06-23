#!/usr/bin/env bash

IMAGE_NAME=data-privacy-hackathon
DOCKER_HUB_IMAGE_NAME=gonzalob90/data-privacy-hackathon

echo 'Tagging image'
docker tag $IMAGE_NAME:latest $DOCKER_HUB_IMAGE_NAME

echo 'Pushing image to Docker Hub'
docker push $DOCKER_HUB_IMAGE_NAME
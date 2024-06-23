#!/usr/bin/env bash

image_name="data-privacy-hackathon"

# Build image with tag
docker build -t $image_name .

# Run container
docker run -p 8008:80 \
            --env-file .env \
            $image_name
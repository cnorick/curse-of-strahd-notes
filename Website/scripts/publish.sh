#!/bin/bash
# Publish site directory to aws s3
# And create invalidation on CloudFront

flags="--delete"

script_full_path=$(dirname "$0")

source "${script_full_path}/.env"

echo cleaning notes
./scripts/clean-notes.sh

echo copying no-spoilers to main folder
cp -r no-spoilers site/

echo syncing to aws
aws s3 sync site "$S3_PATH" $flags

echo invalidating cloudfront
aws cloudfront create-invalidation --distribution-id $CF_ID --paths '/*'

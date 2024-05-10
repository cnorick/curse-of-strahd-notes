#!/bin/bash
# Publish site directory to aws s3
# And create invalidation on CloudFront

flags="--delete"

s3Path="s3://tater-cos-site"

cloudFrontId="EO6PCDBX74WRI"

echo cleaning notes
./scripts/clean-notes.sh

echo copying no-spoilers to main folder
cp -r no-spoilers site/

echo syncing to aws
aws s3 sync site $s3Path $flags

echo invalidating cloudfront
aws cloudfront create-invalidation --distribution-id $cloudFrontId --paths '/*'

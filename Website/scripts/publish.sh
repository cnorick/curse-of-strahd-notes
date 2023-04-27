#!/bin/bash
# Publish site directory to aws s3
# And create invalidation on CloudFront

flags="--delete"

s3Path="s3://tater-cos-site"

cloudFrontId="EO6PCDBX74WRI"

./scripts/clean-notes.sh

#cp 'no-spoilers/Campaign Notes.pdf' no-spoilers/campaign-notes.pdf
cp -r no-spoilers site/

aws s3 sync site $s3Path $flags

aws cloudfront create-invalidation --distribution-id $cloudFrontId --paths '/*'
#!/bin/bash
# Cleans links from the session notes

cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp site/*.js site/*.css no-spoilers/campaign-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/index.html


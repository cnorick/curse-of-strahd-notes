#!/bin/bash
# Cleans links from the session notes

cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp -r site/styles site/scripts no-spoilers/campaign-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/index.html


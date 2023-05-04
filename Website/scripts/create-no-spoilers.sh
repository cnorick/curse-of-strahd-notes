#!/bin/bash
# Creates the no-spoilers part of the site.

cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp -r site/styles site/scripts no-spoilers/campaign-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/index.html

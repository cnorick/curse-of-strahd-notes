#!/bin/bash
# Creates the no-spoilers part of the site.

cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp -r site/styles site/scripts no-spoilers/campaign-notes
cp -r site/session-notes no-spoilers/campaign-notes/session-notes
python3 scripts/create-no-spoilers.py no-spoilers/campaign-notes/index.html no-spoilers/campaign-notes/session-notes


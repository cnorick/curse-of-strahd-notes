#!/bin/bash
# Cleans links from the session notes

rm -r no-spoilers/*
mkdir no-spoilers/campaign-notes
cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp site/new-handouts.html no-spoilers/campaign-notes/new-handouts.html
cp -r site/lib site/scripts no-spoilers/campaign-notes
cp -r site/session-notes no-spoilers/campaign-notes/session-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/index.html no-spoilers/campaign-notes/session-notes no-spoilers
python3 scripts/re-root-urls.py no-spoilers/campaign-notes/new-handouts.html
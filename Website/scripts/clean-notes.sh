#!/bin/bash
# Cleans links from the session notes

rm -r no-spoilers/*
mkdir no-spoilers/campaign-notes
cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp site/new-handouts.html no-spoilers/campaign-notes/new-handouts.html
cp -r site/lib site/scripts no-spoilers/campaign-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/ site
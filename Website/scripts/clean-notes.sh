#!/bin/bash
# Cleans links from the session notes

cp favicon.ico site
cp styles.css site
rm -r no-spoilers/*
mkdir no-spoilers/campaign-notes
cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp site/new-handouts.html no-spoilers/campaign-notes/new-handouts.html
cp site/unlisted-handouts.html no-spoilers/campaign-notes/unlisted-handouts.html
cp -r site/lib no-spoilers/campaign-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/ site
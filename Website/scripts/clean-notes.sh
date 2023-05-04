#!/bin/bash
# Cleans links from the session notes

rm -r no-spoilers/*
cp site/campaign-notes.html no-spoilers/campaign-notes/index.html
cp -r site/styles site/scripts no-spoilers/campaign-notes
cp -r site/session-notes no-spoilers/campaign-notes/session-notes
python3 scripts/clean-notes.py no-spoilers/campaign-notes/index.html no-spoilers/campaign-notes/session-notes
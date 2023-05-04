import shutil
import os
import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], 'r+') as indexFile:
  text = indexFile.read()
  soup = BeautifulSoup(text, 'html.parser')

shutil.copyfile
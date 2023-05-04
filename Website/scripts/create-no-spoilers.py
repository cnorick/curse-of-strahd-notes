import shutil
import os
import sys
from bs4 import BeautifulSoup

with open(sys.argv[1], 'r+') as indexFile:
  text = indexFile.read()
  soup = BeautifulSoup(text, 'html.parser')

  # Make all non-absolute links relative to the root
  for a in soup.find_all('a'):
    if(not a['href'].startswith('http')):
      a['href'] = '/' + a['href']

  sessionAnchors = soup.find(id="Session_Notes").find_all('a')
  for a in sessionAnchors:
    # Make all session note links relative
    a['href'] = a['href'][1:]


# shutil.copyfile
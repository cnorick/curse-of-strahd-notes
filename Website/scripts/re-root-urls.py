import sys
from bs4 import BeautifulSoup

def overwriteFile(file, soup):
  content = str(soup)
  file.seek(0)
  file.write(content)
  file.truncate()

with open(sys.argv[1], 'r+') as handle:
  text = handle.read()
  soup = BeautifulSoup(text, 'html.parser')

  # Make all non-absolute links relative to the root
  print('Fixing no-spoilers index file')
  for a in soup.find_all('a'):
    if(not a['href'].startswith('http')):
      a['href'] = '../../' + a['href']

  overwriteFile(handle, soup)

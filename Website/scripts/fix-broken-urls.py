import os
import sys
from bs4 import BeautifulSoup, Doctype

for root, dirnames, filenames in os.walk(sys.argv[1]):
  for filename in filenames:
    if filename.endswith('.html'):
      fname = os.path.join(root, filename)
      print('Fixing URLs for: {}'.format(fname))
      with open(fname, 'r+') as handle:
        soup = BeautifulSoup(handle.read(), 'html.parser')
        for a in soup.find_all('a'):
          if(not a['href'].startswith('http')):
            # Temp fix for html exporter bug
            a['href'] = a['href'].replace('users/nathan/appdata/local/obsidian', '')
        
        cleanContent = str(soup)

        handle.seek(0)
        handle.write(cleanContent)
        handle.truncate()

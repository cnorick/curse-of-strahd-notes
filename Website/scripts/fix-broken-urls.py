import os
import sys
from bs4 import BeautifulSoup, Doctype

for root, dirnames, filenames in os.walk(sys.argv[1]):
  for filename in filenames:
    if filename.endswith('.html'):
      fname = os.path.join(root, filename)
      print('Filename: {}'.format(fname))
      with open(fname) as handle:
        soup = BeautifulSoup(handle.read(), 'html.parser')
        for item in soup.contents:
          if isinstance(item, Doctype):
            print('Doctype: {}'.format(item))
            break
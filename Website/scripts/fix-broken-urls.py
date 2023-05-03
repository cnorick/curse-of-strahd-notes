import os
from bs4 import BeautifulSoup, Doctype

directory = '/home/brian/Code/sof'
for root, dirnames, filenames in os.walk(directory):
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
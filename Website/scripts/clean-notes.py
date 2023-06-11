import os
import sys
from bs4 import BeautifulSoup

def overwriteFile(file, soup):
  content = str(soup)
  file.seek(0)
  file.write(content)
  file.truncate()

def fixUrls(soup):
  for a in soup.find_all('a', class_='internal-link'):
    a.wrap(soup.new_tag('b'))
    a.unwrap()

def removeSidebar(soup):
  treeContainer = soup.find(class_='tree-container')
  treeContainer.decompose()

def updateIndexFile(filename):
  with open(filename, 'r+') as indexFile:
    text = indexFile.read()
    soup = BeautifulSoup(text, 'html.parser')

    # Make all non-absolute links relative to the root
    print('Fixing no-spoilers index file')
    for a in soup.find_all('a'):
      if(not a['href'].startswith('http')):
        a['href'] = '../../' + a['href']

    sessionAnchors = soup.find(id="Session_Notes").parent.find_next_sibling('div').find_all('a')
    for a in sessionAnchors:
      # Make all session note links relative
      print('Fixing Link to: {}'.format(a.text))
      a['href'] = a['href'][6:]

    overwriteFile(indexFile, soup)

def updateSessionFiles(folder):
  for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.html'):
        fname = os.path.join(root, filename)
        with open(fname, 'r+') as handle:
          soup = BeautifulSoup(handle.read(), 'html.parser')
          print('Fixing URLs for: {}'.format(fname))
          fixUrls(soup)

          print('Removing Sidebar for: {}'.format(fname))
          removeSidebar(soup)

          overwriteFile(handle, soup)


updateIndexFile(sys.argv[1])
updateSessionFiles(sys.argv[2])

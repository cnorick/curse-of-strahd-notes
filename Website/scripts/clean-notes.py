import os
import sys
from bs4 import BeautifulSoup

alreadyFixedLinkClass = 'skip-fix'

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
    # print('Fixing no-spoilers index file')
    # for a in soup.find_all('a'):
    #   if(not a['href'].startswith('http')):
    #     a['href'] = '../../' + a['href']

    sessionAnchors = soup.find(id="Session_Notes").parent.find_next_sibling('div').find_all('a')
    for a in sessionAnchors:
      # Make all session note links relative
      print('Fixing Link to: {}'.format(a.text))
      a['href'] = a['href'][6:]
      a['class'] = a.get('class', []) + [alreadyFixedLinkClass]

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

          overwriteFile(handle, soup)

def updateAllFiles(folder):
  for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.html'):
        fname = os.path.join(root, filename)
        with open(fname, 'r+') as handle:
          soup = BeautifulSoup(handle.read(), 'html.parser')
          print('Removing Sidebar for: {}'.format(fname))
          removeSidebar(soup)

          overwriteFile(handle, soup)

def importLinkedFiles(folder):
  for root, dirnames, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.html'):
        fname = os.path.join(root, filename)
        with open(fname, 'r+') as handle:
          soup = BeautifulSoup(handle.read(), 'html.parser')
          print('Parsing for linked files: {}'.format(fname))

          for a in soup.find_all('a', class_='internal-link'):
            if alreadyFixedLinkClass in a.get('class', []):
              break
            path = '../..' + a['href']




indexFilename = sys.argv[1]
sessionFilesFolder = sys.argv[2]
rootSpoilersFolder = sys.argv[3]
updateIndexFile(indexFilename)
updateSessionFiles(sessionFilesFolder)
importLinkedFiles(rootSpoilersFolder)
updateAllFiles(rootSpoilersFolder)

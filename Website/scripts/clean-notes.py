import os
import sys
import shutil
from bs4 import BeautifulSoup

alreadyFixedLinkClass = 'link-fixed'

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

def updateRootPath(soup, rootPath):
  meta = soup.find(id='root-path')
  meta['root-path'] = '/' + rootPath

def removeLinksInFile(fname):
  with open(fname, 'r+') as handle:
    soup = BeautifulSoup(handle.read(), 'html.parser')
    print('Fixing URLs for: {}'.format(fname))
    fixUrls(soup)

    overwriteFile(handle, soup)

def fixAssetsInFile(fname):
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
          print('Updating Root Path for: {}'.format(fname))
          updateRootPath(soup, folder)

          overwriteFile(handle, soup)

def importLinkedFilesForFolder(spoilersFolder, rootSiteFolder):
  for root, dirnames, filenames in os.walk(spoilersFolder):
    for filename in filenames:
      if filename.endswith('.html'):
        fname = os.path.join(root, filename)
        with open(fname, 'r+') as handle:
          soup = BeautifulSoup(handle.read(), 'html.parser')
          print('Parsing for linked files: {}'.format(fname))

          for a in soup.find_all('a', class_='internal-link'):
            if alreadyFixedLinkClass in a.get('class', []):
              break

            relativePath = os.path.join(*a['href'].split('/'))
            newPath = os.path.join(spoilersFolder, relativePath)
            if os.path.isfile(newPath):
              break
            
            origPath = os.path.join(rootSiteFolder, relativePath)
            print('copying {} -> {}'.format(origPath, newPath))
            os.makedirs(os.path.dirname(newPath), exist_ok=True)
            shutil.copyfile(origPath, newPath)
            removeLinksInFile(newPath)
            fixAssetsInFile(newPath)




rootSpoilersFolder = sys.argv[1]
rootMainSiteFolder = sys.argv[2]
importLinkedFilesForFolder(rootSpoilersFolder, rootMainSiteFolder)
updateAllFiles(rootSpoilersFolder)

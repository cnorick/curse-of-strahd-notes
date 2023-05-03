from bs4 import BeautifulSoup
import sys

cleanContent = ''
with open(sys.argv[1], 'r+') as my_file:
  text = my_file.read()
  soup = BeautifulSoup(text, features='lxml')
  
  # Make all non-absolute links relative to the root
  for a in soup.find_all('a'):
    print(a['href'])
    if(not a['href'].startswith('http')):
      # a['href'] = '/' + a['href']
      # Temp fix for html exporter bug
      a['href'] = a['href'].replace('users/nathan/appdata/local/obsidian', '')

  # Hide all the links in the session notes
  sessionNotes = soup.find(id="Session_1").find_parent(class_='block-language-dataviewjs')
  for a in sessionNotes.find_all('a'):
    a['href'] = '#'

  cleanContent = str(soup)

  my_file.seek(0)
  my_file.write(cleanContent)
  my_file.truncate()
  

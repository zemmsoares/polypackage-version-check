#!/usr/bin/python

import requests 
from bs4 import BeautifulSoup
import subprocess

result = requests.get("https://nodejs.org/en/")
c = result.content

soup = BeautifulSoup(c,"html.parser" );
soup.prettify()

results = soup.findAll("a", {"data-version" : True})
result1 = results[0].attrs['data-version']
node_latest_version = results[1].attrs['data-version'].strip() 

output = subprocess.Popen("node -v",
                           shell=True,
                           stdout=subprocess.PIPE,
                           universal_newlines=True).communicate()[0]

installed_version = output.strip()

if node_latest_version == installed_version:
	print(installed_version +' Latest Version Installed')
elif node_latest_version != installed_version:
	print(installed_version +' New version Available')
else:
	print('Error')

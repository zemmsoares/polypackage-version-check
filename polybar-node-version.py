#!/usr/bin/python

import requests 
from bs4 import BeautifulSoup
import subprocess


try:
	result = requests.get("https://nodejs.org/en/")

	c = result.content

	soup = BeautifulSoup(c,"html.parser" );
	soup.prettify()

	results = soup.findAll("a", {"data-version" : True})
	result1 = results[0].attrs['data-version']
	node_latest_version = results[1].attrs['data-version'].strip() 

	try:
		output = subprocess.check_output("node -v",shell=True, stderr=subprocess.STDOUT)

		installed_version = output.decode("utf-8").strip()

		if node_latest_version == installed_version:
			print(installed_version +' Latest')
		elif node_latest_version != installed_version:
			print(installed_version +' Outdated')
		else:
			print('Error')

	except subprocess.CalledProcessError:
		print("Node not found")


except requests.exceptions.RequestException as e:
    print ('Something went wrong!')



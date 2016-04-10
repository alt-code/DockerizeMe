from dependency_dictionary import requirements_dictionary
import os
import json

if os.path.isfile('requirements.txt'):
	with open ('requirements.txt','r') as f:
		read_data = f.read() 

packages = []
requirement = read_data.splitlines()
for line in requirement:
	packages.append(line.split('==')[0])

for package in packages:
	if package in requirements_dictionary.keys():
		for dependency in requirements_dictionary[package]:
			print "RUN sudo apt-get install -y {0}".format(dependency)

if os.path.isfile('package.json'):
	with open('package.json','r') as f:
		read_data = f.read()

pckg_json =  json.loads(read_data)
for package in pckg_json['dependencies']:
	if package in requirements_dictionary.keys():
		for dependency in requirements_dictionary[package]:
			print "RUN sudo apt-get install -y {0}".format(dependency)
import os
import json
import ConfigParser
import re

conf = ''


def main():
	parseConfig("comp.ini")
	htmlpath = conf._sections['Comp']['html']
	parseHtmltd(htmlpath)

def parseHtmltd(htmlpath):
	terminator = 'Well GPM:'
	tdlist = []
	matchstr = ''
	with open(htmlpath, 'r') as htmlfile:
		for line in htmlfile:
			matchobj = re.match('.*<td.*><B>(.*)</B><.*', line)
			if matchobj:
				matchstr = matchobj.group(1)
				matchstr = re.sub('&nbsp;', '', matchstr[0])
				matchstr = matchstr.strip()
				if matchstr == '': continue
				print matchstr
				tdlist.append(matchstr)

			else:
				matchobj = re.match('.*<td.*>(.*)<.*', line)
				if matchobj:
					matchstr = matchobj.group(1)
					matchstr = matchstr.split('&nbsp;')[:1]
					matchstr[0] = matchstr[0].strip()
					if matchstr[0] == '': continue
					tdlist.append(matchstr[0])
	#print tdlist
	houses = []
	dataDict = {'MLS ID:' : tdlist[0], 'Address:' : tdlist[1]}
	for index, td in enumerate(tdlist):
		if td == terminator:
			houses.append(dataDict)
			try:
				dataDict = {'MLS ID:' : tdlist[index+1], 'Address:' : tdlist[index+2]}
			except IndexError:
				break
		matchobj = re.match('(.*:)$', td)
		if matchobj:
			key = matchobj.group(1)
			value = tdlist[index+1]

			matchobj = re.match('(.*:)$', value)
			if matchobj:
				dataDict[key] = ''
			else:
				dataDict[key] = value
	return houses

def parseConfig(path):
	global conf
	conf = ConfigParser.ConfigParser()
	conf.read(path)


main()
import os
import json
import ConfigParser
import re

class CompParser():
	def __init__(self, configpath="comp.ini"):
		self.configpath = configpath
		self.datadict = {}
		self.whitelist = []

	def parse(self, path=None):
		self.parseConfig(self.configpath)
		self.datadict = self.parseHtmltd(path)
		self.createJson()
	def getData(self):
		return self.datadict
	def parseHtmltd(self, htmlpath):
		
		tdlist = []
		matchstr = ''
		with open(htmlpath, 'r') as htmlfile:
			#begin html parsing of file
			for line in htmlfile:
				#matches for titles that are bold excluding one that starts with a tag [^<]
				#these regex matches are exceptions and their values are in the same td as the key
				matchobj = re.match('.*<td.*><B>([^<].*)</B>(.*)<.*', line)
				if matchobj:
					matchkey = matchobj.group(1)
					matchvalue = matchobj.group(2)
					
					#get rid of whitespace junk on key
					matchkey = re.sub('&nbsp;', '', matchkey)
					matchkey = matchkey.strip()
					if matchkey == '': continue

					#get rid of whitespace junk on value
					matchvalue = re.sub('&nbsp;', '', matchvalue)
					matchvalue = matchvalue.strip()

					#store the key and value back to back
					tdlist.append(matchkey)
					tdlist.append(matchvalue)

				else:
					#line is not an exception so data is between <td> tag
					matchobj = re.match('.*<td.*>(.*)<.*', line)
					if matchobj:
						matchstr = matchobj.group(1)
						matchstr = re.sub('&nbsp;', '', matchstr)
						matchstr = matchstr.strip()
						if matchstr == '': continue
						tdlist.append(matchstr)
		#using the list of td elements we will put each one into a dictionary where:
		#Key = title of item, Value = value of item
		#ex: Key = 'List Price:' Value = '$600,000'
		houses = []
		terminator = 'Location:'
		#a few tds have no title td so we will manually add them to intialize our dict
		dataDict = {'MLS ID:' : tdlist[0], 'Address:' : tdlist[1], 'Status:' : tdlist[3]}

		#go through each td item and keep track of the index
		for index, td in enumerate(tdlist):
			#if we reach a terminator that means one of the houses is done with its data
			if td == terminator:
				#the dict we have made is now added to a list of houses
				houses.append(dataDict)
				#initialize a new dictionary now with the offset of the new house in the tdlist
				try:
					dataDict = {'MLS ID:' : tdlist[index+3], 'Address:' : tdlist[index+4], 'Status:' : tdlist[index+6]}
				except IndexError:
					#if we get and index error all houses have been processed into a dictionary and we are now done
					break
			#if we have colon in the td its a key
			matchobj = re.match('(.*:)$', td)
			if matchobj:
				key = matchobj.group(1)
				#the value of the key always will succeed it if it exists
				value = tdlist[index+1]

				#check to see if the value is actully a key
				matchobj = re.match('(.*:)$', value)
				if matchobj:
					#if match then the key we are processing has no value
					dataDict[key] = ''
				else:
					#other wise this td is our key's value so add it to the dict
					dataDict[key] = value
		return houses
		# for house in houses:
		# 	print house['Status:'],'\n'

	def filterDict(self, datadict):
		#split the list of filters and strip whitespace and put in list
		self.whitelist = [Filter.strip() for Filter in self.conf._sections['Data']['filters'].split(',')]
		datalist = []
		for dictionary in datadict:
			filterdict = {whitekey : dictionary[whitekey] for whitekey in self.whitelist if whitekey in dictionary }
			datalist.append(filterdict)
		return datalist
	def getWhitelist(self):
		return self.whitelist
	def createJson(self):
		jsonpath = self.conf._sections['Comp']['json']
		try: os.remove(jsonpath)
		except: pass

		datalist = self.filterDict(self.datadict)

		with open(jsonpath, 'a') as jsonfile:
			json.dump(datalist, jsonfile, indent=4)

	def parseConfig(self, path):
		self.conf = ConfigParser.ConfigParser()
		self.conf.read(path)

parser = CompParser()
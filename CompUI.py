import os, sys
import wx, re
import CompParser

def driver():
	app = wx.App(False)
	frame = CompFrame(None, 'Comparables')
	app.MainLoop()

class CompFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(450,450), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
		self.parser = CompParser.CompParser()
		self.parser.parse()

		self.InitUI()
	def InitUI(self):
		self.panel = wx.Panel(self)

		#filter the data
		housedata = self.parser.filterDict(self.parser.getData())
		#grab all the keys so we have it handy and outside of the dictionary
		keylist = self.parser.getWhitelist()

		#initiulaze ui elements
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.list = wx.ListCtrl(self.panel, -1, style=wx.LC_REPORT|wx.BORDER_SUNKEN)

		#intializing list control columns
		self.list.InsertColumn(0, 'Attribute', width=140)
		#make a column and label it by address for each house in the dictionary
		for index, house in enumerate(housedata):
			self.list.InsertColumn(index+1, house['Address:'].title(), width=130)

		#populate our listctrl, the populating is handled by row
		for i, key in enumerate(keylist):
			#row is created each time we make a new row, and the first element in the row will be the key
			row = self.list.InsertStringItem(i,key)
			#using the key, we will go through each house and add the key's value to the end of the row
			for h_idx, house in enumerate(housedata):
				try: self.list.SetStringItem(row,h_idx+1,house[key])
				except KeyError: pass

		hbox.Add(self.list, 1, flag=wx.EXPAND|wx.ALL, border=5)
		self.panel.SetSizer(hbox)
		self.Centre()
		self.Show()

driver()
import os, sys
import wx, re
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
from wx.lib.wordwrap import wordwrap
import wx.lib.agw.ultimatelistctrl as ULC  
import CompParser
COL_NUMBER=7
COL_WIDTH=160
WINDOW_WIDTH=COL_NUMBER*COL_WIDTH-20
WINDOW_HEIGHT=550
def driver():
	app = wx.App(False)
	frame = CompFrame(None, 'Comparables')
	app.MainLoop()

class CompFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(WINDOW_WIDTH,WINDOW_HEIGHT), style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
		self.parser = CompParser.CompParser()

		path = self.openDialog()
		if not path:
			sys.exit(0)

		self.parser.parse(path)
		self.panel = ULCPanel(self, self.parser)
		self.Centre()
		self.Show()
	def openDialog(self):
		openFileDialog = wx.FileDialog(self, "Open HTML file", "", "", "*.htm", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)


		if openFileDialog.ShowModal() == wx.ID_CANCEL:
			return 
		else:
			return openFileDialog.GetPath()
	def InitListCtrl(self):
		self.panel = wx.Panel(self)
		listctrl = CompListCtrl(self.panel)
		self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, listctrl)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, listctrl)
		#filter the data
		self.housedata = self.parser.filterDict(self.parser.getData())
		#grab all the keys so we have it handy and outside of the dictionary
		keylist = self.parser.getWhitelist()
		#intializing list control columns
		listctrl.InsertColumn(0, 'Attribute', width=140)
		#make a column and label it by address for each house in the dictionary
		for index, house in enumerate(self.housedata):
			listctrl.InsertColumn(index+1, house['Address:'].title(), width=COL_WIDTH)

		#populate our listctrl, the populating is handled by row
		for i, key in enumerate(keylist):
			#row is created each time we make a new row, and the first element in the row will be the key
			row = listctrl.InsertStringItem(i,key)
			#using the key, we will go through each house and add the key's value to the end of the row
			for h_idx, house in enumerate(self.housedata):
				try: listctrl.SetStringItem(row,h_idx+1,house[key])
				except KeyError: pass
		return listctrl

class CompListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT|wx.LC_HRULES|wx.BORDER_SUNKEN)
		ListCtrlAutoWidthMixin.__init__(self)

class ULCPanel(wx.Panel):
	def __init__(self, parent, parser):
		wx.Panel.__init__(self, parent, style=wx.WANTS_CHARS)
		self.parser = parser
		
		listctrl = ULC.UltimateListCtrl(self, agwStyle=ULC.ULC_REPORT|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT|ULC.ULC_HRULES)
		
		#filter the data
		self.housedata = self.parser.filterDict(self.parser.getData())
		#grab all the keys so we have it handy and outside of the dictionary
		keylist = self.parser.getWhitelist()
		#intializing list control columns
		listctrl.InsertColumn(0, 'Attribute', width=COL_WIDTH)
		#make a column and label it by address for each house in the dictionary
		for index, house in enumerate(self.housedata):
			listctrl.InsertColumn(index+1, house['Address:'].title(), width=COL_WIDTH)

		#populate our listctrl, the populating is handled by row
		for i, key in enumerate(keylist):
			if key == 'Address:': continue
			#row is created each time we make a new row, and the first element in the row will be the key
			row = listctrl.InsertStringItem(i,key)
			#using the key, we will go through each house and add the key's value to the end of the row
			for h_idx, house in enumerate(self.housedata):
				try: 
					content = wordwrap(house[key], COL_WIDTH-15, wx.ClientDC(self))
					listctrl.SetStringItem(row,h_idx+1,content)
				except KeyError: pass

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(listctrl, 1, flag=wx.EXPAND|wx.ALL, border=5)
		self.SetSizer(sizer)

driver()
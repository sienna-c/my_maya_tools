class huoys_cfxTool(object):
	def __init__(self):
		self.window='huoys_cfxTool'
		self.title="Sienna's CFX tools"
		self.size=(546, 350)
		self.supportsToolAction=False
	def create(self):
		if mc.window(self.window, exists=True):
			mc.deleteUI(self.window, window=True)
		self.window=mc.window(self.window, title=self.title, wh=self.size)
		mc.showWindow()
	def commonMenu(self):
		self.editMenu=mc.menu(l='Edit')
		self.editMenuSave=mc.menuItem(l='Save Settings')
		self.editMenuReset=mc.menuItem(l='Reset Settings')
		self.editMenuDiv=mc.menuItem(d=True)
		self.editMenuRadio=mc.radioMenuItemCollection()
		self.editMenuTool=mc.menuItem(l='As Tool', rb=True, en=self.supportsToolAction)
		self.editMenuAction=mc.menuItem(l='As Action', rb=True, en=self.supportsToolAction)
		self.helpMenu=mc.menu(l='Help')
		self.helpMenuItem=mc.menuItem(l='Help on %s ' %self.title)
    
    
# in another tab input
testWindow=huoys_cfxTool()
testWindow.create()

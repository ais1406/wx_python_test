#!/usr/bin/env python
import wx
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600,600))
        self.control = wx.TextCtrl(self, style= wx.TE_MULTILINE)
        self.CreateStatusBar() # a statusbar in the bottom of the window
        
        #setting up the menu
        filemenu = wx.Menu()
        
        #wx.ID_About and wx.ID_EXIT are standard IDs provided by wxWidgets
        filemenu.Append(wx.ID_ABOUT, "&About","Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit","terminate the program")
        
        # creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") #adding the "filemenu" to the Menubar
        self.SetMenuBar(menuBar) #adding the menubar to the frame content
        self.Show(True)
                
class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, 'Small editor')
app.MainLoop()
        
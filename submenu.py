import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example,self).__init__(*args, **kwargs)
        
        self.InitUI()
        
    def InitUI(self):
        
        menubar = wx.MenuBar()
        
        filemenu = wx.Menu()
        #filemenu.Append(wx.ID_NEW, '&New')
        
        
        
        nmi = wx.MenuItem(filemenu, wx.ID_NEW , '&New\tCtrl+N')
        nmi.SetBitmap(wx.Bitmap('img/new.png')) #icon img source
        filemenu.AppendItem(nmi)
        
        omi = wx.MenuItem(filemenu, wx.ID_OPEN, '&Open\tCtrl+O')
        omi.SetBitmap(wx.Bitmap('img/open.png')) #icon img source
        filemenu.AppendItem(omi)
        
        
        smi = wx.MenuItem(filemenu,wx.ID_SAVE, '&SAVE\tCtrl+S')
        smi.SetBitmap(wx.Bitmap('img/save.png')) #icon img source
        filemenu.AppendItem(smi)
        
        filemenu.AppendSeparator()
        
       
        
        
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list....')
        imp.Append(wx.ID_ANY, 'Import bookmark list....')
        imp.Append(wx.ID_ANY, 'Import mail....')
        
        filemenu.AppendMenu(wx.ID_ANY,'I&mport',imp)
        
        qmi = wx.MenuItem(filemenu, wx.ID_EXIT, '&Quit\tCtrl+X')
        qmi.SetBitmap(wx.Bitmap('img/exit.png'))
        filemenu.AppendItem(qmi)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
        self.SetSize((600,600))
        self.SetTitle('Submenu test')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self,e):
        self.Close()
        

def main():
    ex = wx.App(False)
    Example(None)
    ex.MainLoop()
    
    
if __name__ == '__main__':
    main()
        
        
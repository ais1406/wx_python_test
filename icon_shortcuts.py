import wx

APP_EXIT = 1

class Example(wx.Frame):
    
    def __init__ (self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        
        self.InitUI()
        
    def InitUI(self):
        
        menubar = wx.MenuBar() #�޴��� �޽�� ���� ����
        filemenu = wx.Menu()
        qmi = wx.MenuItem(filemenu,APP_EXIT, '&Quit\tCtrl+Q')  # ����Ű����
        qmi.SetBitmap(wx.Bitmap('exit.png'))  # �޴��� �̹��� �޽��
        filemenu.AppendItem(qmi) #�޴��� �߰��ϱ� 
        
        self.Bind(wx.EVT_MENU,self.OnQuit, id=APP_EXIT) #�̺�Ʈ ����
        
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
        self.SetSize((250,200))
        self.SetTitle('Icons & Shortcuts')
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
        
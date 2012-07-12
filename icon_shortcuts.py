import wx

APP_EXIT = 1

class Example(wx.Frame):
    
    def __init__ (self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        
        self.InitUI()
        
    def InitUI(self):
        
        menubar = wx.MenuBar() #메뉴바 메써드 변수 선언
        filemenu = wx.Menu()
        qmi = wx.MenuItem(filemenu,APP_EXIT, '&Quit\tCtrl+Q')  # 단축키설정
        qmi.SetBitmap(wx.Bitmap('exit.png'))  # 메뉴바 이미지 메써드
        filemenu.AppendItem(qmi) #메뉴바 추가하기 
        
        self.Bind(wx.EVT_MENU,self.OnQuit, id=APP_EXIT) #이벤트 설정
        
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
        
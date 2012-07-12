import wx
class Example(wx.Frame):
    def __init__(self,parent, title):
        super(Example,self).__init__(parent, title=title, size= (300,200))
        
        self.Centre()
        self.show()
       
       

    app = wx.App(False)

    app.MainLoop()

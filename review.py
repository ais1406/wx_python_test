# -*- coding: utf-8 -*-
import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(300, 250))
            
        self.InitUI()
        self.Centre()
        self.Show()     
        
        
    def InitUI(self):
        
        panel = wx.Panel(self)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        fgs = wx.FlexGridSizer(3,2,10,10)
        
        title = wx.StaticText(panel, label = "Title")
        author = wx.StaticText(panel, label = "author")
        review = wx.StaticText(panel, label = 'Review')
        
        
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
        
        fgs.AddMany([(title), (tc1, 1, wx.EXPAND), 
                     (author),  (tc2, 1, wx.EXPAND), 
                     (review, 1, wx.EXPAND), 
                     (tc3, 1, wx.EXPAND)
                     ])

        # row는 수직 col은 수평 
        fgs.AddGrowableRow(2,1)   # 텍스트박스 맨 마지막것을 끝까지 늘린다.
        fgs.AddGrowableCol(1,0) # 텍스트박스의 모든것들을 다 늘린다  한개늘리면 따라서 다 growable 됨. (1, 아무숫자) 도 가능
        
        """
        0,0  0,1
        1,0  1,1
        2,0  2,1
        
        """
        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

        
if __name__ == '__main__':
  
    app = wx.App(False)
    Example(None, title='Review')
    app.MainLoop()   
                     
                     
                     
                     
       
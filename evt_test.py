import wx

########################################################################
class MyDlg(wx.Dialog):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Dialog.__init__(self, None, title="I'm a dialog!")

        lbl = wx.StaticText(self, label="Hi from the panel's init!")
        btn = wx.Button(self, id=wx.ID_OK, label="Close me")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL, 5)
        self.SetSizer(sizer)


########################################################################
class MyPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        # show a custom dialog
        dlg = MyDlg()
        dlg.ShowModal()
        dlg.Destroy()

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        pdc = wx.PaintDC(self)
        try:
            dc = wx.GCDC(pdc)
        except:
            dc = pdc
        rect = wx.Rect(0,0, 100, 100)
        for RGB, pos in [((178,  34,  34), ( 50,  90)),
                         (( 35, 142,  35), (110, 150)),
                         ((  0,   0, 139), (170,  90))
                         ]:
            r, g, b = RGB
            penclr   = wx.Colour(r, g, b, wx.ALPHA_OPAQUE)
            brushclr = wx.Colour(r, g, b, 128)   # half transparent
            dc.SetPen(wx.Pen(penclr))
            dc.SetBrush(wx.Brush(brushclr))
            rect.SetPosition(pos)
            dc.DrawRoundedRectangleRect(rect, 8)

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Example frame")

        # show a MessageDialog
        style = wx.OK|wx.ICON_INFORMATION
        dlg = wx.MessageDialog(parent=None, 
                               message="Hello from the frame's init", 
                               caption="Information", style=style)
        dlg.ShowModal()
        dlg.Destroy()

        # create panel
        panel = MyPanel(self)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
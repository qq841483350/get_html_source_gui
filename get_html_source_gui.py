#coding:utf8
#获取网页源代码GUI工具
import wx,requests,re
def get_source(event):
    contents2.Clear()  #清空内容
    url=contents1.GetValue()  #获取contents1里的内容
    url=''.join(url.split()).encode('utf8')    #去除中间的空格与回车
    html=requests.get(url).content
    # contents2.SetValue(word)   #设置contents里的内容
    contents2.AppendText(html+'\n')   #添加contents里的内容

app = wx.App()
win = wx.Frame(None,title = "获取网页源代码工具,开发者：李亚涛 wx:841483350".decode('utf8'),size=(1200,1000))

# icon = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO)   #绑定ico
# win.SetIcon(icon)
win.Show()

wx.StaticText(win,label="请输入网址(一定要带http://)：",pos=(150,10),size=(200,30))
contents1 = wx.TextCtrl(win, pos = (350,5),size = (300,30), style = wx.TE_MULTILINE | wx.TE_RICH)
contents2 = wx.TextCtrl(win, pos = (100,40),size = (1000,600), style = wx.TE_MULTILINE | wx.TE_RICH)

loadButton = wx.Button(win, label = '获取网页源代码'.decode('utf8'),pos = (700,5),size = (100,30))
loadButton.Bind(wx.EVT_BUTTON,get_source)  #这个按钮绑定 get_source 这个函数
app.MainLoop()


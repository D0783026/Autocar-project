import wx
import cv2
import time
import numpy
import socket

TCP_IP = "192.168.43.241"
TCP_PORT = 9090

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

##receive all
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

class TestOpenCV ( wx.Frame ):
    windowWidth = 500
    windowHeight = 320

    ##建構子
    def __init__( self, parent=None ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"單一視訊畫面", pos = wx.DefaultPosition, size = wx.Size( self.windowWidth, self.windowHeight), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.stbmp1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.stbmp1, 1, wx.ALL|wx.EXPAND, 5 )
##        self.stbmp1.SetBitmap(wx.Bitmap( u"../image/heats1-f1-02_gray_pressed.png", wx.BITMAP_TYPE_ANY ))

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)
        newimg = wx.BitmapFromImage(image)
        return newimg

    def updateImage(self, bitmap):
        # 縮小圖片符合視窗的大小
        newbitmap = self.scale_bitmap(bitmap, self.windowWidth-10, self.windowHeight-30)
        self.stbmp1.SetBitmap(newbitmap)

class App(wx.App):
    """Application class."""

    def OnInit(self):
        self.frame = TestOpenCV()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        self.run()
        return True

    def rot90(self, img, angle):
        if(angle == 270 or angle == -90):
            img = cv2.transpose(img)
            img = cv2.flip(img, 0)  # transpose+flip(0)=CCW
        elif (angle == 180 or angle == -180):
            img = cv2.flip(img, -1)  # transpose+flip(-1)=180
        elif (angle == 90 or angle == -270):
            img = cv2.transpose(img)
            img = cv2.flip(img, 1)  # transpose+flip(1)=CW
        elif (angle == 360 or angle == 0 or angle == -360):
            pass
        else :
            raise Exception("Unknown rotation angle({})".format(angle))
        return img

    def run(self):

        while True:
            length = recvall(sock,16)
            stringData = recvall(sock, int(length))
            data = numpy.fromstring(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,1)
            cv2.waitKey(1)
               
    cv2.destroyAllWindows()


def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
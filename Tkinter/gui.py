import wx
import cv2
import time

class TestOpenCV ( wx.Frame ):
    windowWidth = 500
    windowHeight = 320

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

        cap = cv2.VideoCapture(0);

        while True:
            ret, frame = cap.read()

            if ret == True:
                # 畫面旋轉 90度
                srcBGR = self.rot90(frame, 0)

                # wxPython 只能處理 RGB 的圖片，要從 BGR 轉 RGB
                srcRGB = cv2.cvtColor(srcBGR, cv2.COLOR_BGR2RGB)

                #print dst.shape  w=720, h=1280
                w, h = srcRGB.shape[:2]

                #dst = cv2.resize(srcRGB, (h/2,w/2), interpolation = cv2.INTER_AREA)
                #wxImage = wx.ImageFromBuffer(h/2, w/2, dst)
                wxImage = wx.ImageFromBuffer(h, w, srcRGB)
                bitmap = wx.BitmapFromImage(wxImage)

                # 更新 視窗上的圖片
                self.frame.updateImage(bitmap)

                #cv2.imshow('frame', dst)
                #if cv2.waitKey(30) & 0xFF == ord('q'):
                #    break

                # sleep 30ms
                time.sleep(0.03)

            else:
                break

        cap.release()
        cv2.destroyAllWindows()


def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()
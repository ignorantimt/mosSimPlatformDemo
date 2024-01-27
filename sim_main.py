import os
import sys
import csv
from PyQt5 import QtWidgets, QtWebEngineWidgets
from mainWindow import Ui_MainWindow

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.listWidget.itemClicked.connect(self.update_title)
        self.listWidget.itemClicked.connect(self.switch_stacked_widget_page)

        self.videoPlayer = QMediaPlayer(self)
        self.videoPlayer.error.connect(self.handleMediaError)

        self.label_descrs = []
        self.loadCsv(f'./resource/labels.csv')
        self.label_descr.setText(self.label_descrs[0])
        self.setLayoutStretch(self.verticalLayout, [1,0,6])

        self.operations = {
            1: self.playVideo, 
            4: self.showPDF, 5: self.showPDF, 6: self.playVideo,
            7: self.showPDF, 9: self.playVideo,
            11: self.playVideo, 12: self.playVideo,
            14: self.playVideo, 15: self.playVideo,
            16: self.playVideo, 17: self.playVideo
        }
        
    def update_title(self, item):
        self.label_title.setText(item.text())
        index = self.listWidget.row(item)
        self.label_descr.setText(self.label_descrs[index])

    def switch_stacked_widget_page(self, item):
        index = self.listWidget.row(item)
        self.stackedWidget.setCurrentIndex(index)
        if index != 0:
            self.setLayoutStretch(self.verticalLayout, [1,5,2])
            if index in self.operations:
                operation = self.operations[index]
                fileType = 'mp4' if operation == self.playVideo else 'pdf'
                widget = getattr(self, f'widget_{index}')
                operation(f'./resource/Lab{index}.{fileType}', widget)
        
    
    def showPDF(self, pdfPath, widget):
        pdfPath = os.path.abspath(pdfPath)
        se = widget.settings()
        se.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        widget.load(QUrl.fromLocalFile(pdfPath))
        widget.show()

    def playVideo(self, videoPath, widget):
        videoPath = os.path.abspath(videoPath)
        self.videoPlayer.setVideoOutput(widget)
        self.videoPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(videoPath)))
        self.videoPlayer.play()

    def loadCsv(self, csvPath):
        with open(csvPath, newline='', encoding='gb2312') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            next(csvReader)
            for row in csvReader:
                self.label_descrs.append(row[1])
                # print(row[1])

    def setLayoutStretch(self, layout, stretchList):
        for index, sL in enumerate(stretchList):
            layout.setStretch(index, sL)

    def showingStatusChange(self, comps_hide, comps_show):
        for comp in comps_hide:
            comp.setVisible(False)
        for comp in comps_show:
            comp.setVisible(True)

    def handleMediaError(self):
        print("Media Player Error: ", self.videoPlayer.errorString())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

import os
import sys
import csv
from PyQt5 import QtWidgets, QtWebEngineWidgets
from mainWindow import Ui_MainWindow

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QWidget

from ilabx_api import ApiConfig
from upload_dialog import UploadDialog

from walking_sample import walking_sim_demo

from control import matlab, c2d, dare

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
        self.setLayoutStretch(self.verticalLayout, [1,6,0])

        self.showPic('./resource/logo/MOS.png', self.label_MOS, True, True)
        self.showPic('./resource/logo/THU.png', self.label_THU, True, True)
        self.label_depend.setStyleSheet('color: red; font-weight: bold')

        self.operations = {
            1: self.playVideo, 
            4: self.showPDF, 5: self.showPDF,
            7: self.showPDF, 9: self.playVideo,
            11: self.playVideo, 12: self.playVideo,
            14: self.playVideo, 15: self.playVideo,
            16: self.playVideo, 17: self.playVideo
        }

        # Lab 2
        self.pushButton_py_code.clicked.connect(self.showPyCode)
        self.pushButton_py_res.clicked.connect(self.showPyRes)
        self.pushButton_py_next.clicked.connect(self.pyNext)

        # Lab 3
        for i in range(1, 6):
            pb = getattr(self, f'pushButton_ubuntu_{i}')
            pb.clicked.connect(lambda _, i=i: self.showUbuntu(i))

        # Lab 6
        self.pushButton_cv_code.clicked.connect(self.showCvCode)
        self.pushButton_cv_1.clicked.connect(self.showCvIni)
        self.showCvFlag = 0
        self.pushButton_cv_2.clicked.connect(self.showCvContinue)
        self.pushButton_cv_2.setEnabled(False)

        # Lab 8
        self.pushButton_pf_code.clicked.connect(self.showPfCode)
        self.pushButton_pf_res.clicked.connect(self.showPfRes)

        # Lab 13
        self.pushButton_run_sim.clicked.connect(self.run_simulation)

        # Upload
        self.action_upload.triggered.connect(self.open_upload_dialog)
        # 设置API配置信息
        self.api_config = ApiConfig(
            api_base='你的API基础地址',
            appid='你的APPID',
            secret='你的密钥'
        )
        
        
    def update_title(self, item):
        self.label_title.setText(item.text())
        index = self.listWidget.row(item)
        self.label_descr.setText(self.label_descrs[index])

    def switch_stacked_widget_page(self, item):
        index = self.listWidget.row(item)
        self.stackedWidget.setCurrentIndex(index)
        if index == 0:
            self.setLayoutStretch(self.verticalLayout, [1,6,0])
        else:
            self.setLayoutStretch(self.verticalLayout, [1,2,15])
            if index in self.operations:
                operation = self.operations[index]
                fileType = 'mp4' if operation == self.playVideo else 'pdf'
                widget = getattr(self, f'widget_{index}')
                operation(f'./resource/Lab{index}.{fileType}', widget)
            elif index == 2:
                self.pyQuestions = []
                self.loadPyQuestions('./resource/Lab2/questions.txt')
                self.pyIndex = 1
                self.label_lab2_qs.setText(self.pyQuestions[0])
            elif index == 6:
                self.showCvIni()
            elif index == 10:
                self.showingStatusChange([self.textBrowser_cv_code],[self.label_cv_img])
                self.showPic('./resource/Lab10.png', self.label_lab10_img)
                

    def showPic(self, picPath, widget, scaled = True, transP = True):
        ImgPath = os.path.abspath(picPath)
        pixmap = QPixmap(ImgPath)

        if transP:
            # 将白色背景变为透明的
            mask = pixmap.createMaskFromColor(Qt.white, Qt.MaskInColor)
            pixmap.setMask(mask)

        widget.setPixmap(pixmap)
        widget.setScaledContents(scaled)
        
    
    def showPDF(self, pdfPath, widget):
        pdfPath = os.path.abspath(pdfPath)
        se = widget.settings()
        se.setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        # se.setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptCanOpenWindows, False)
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
    
    def loadPyQuestions(self, pyQsPath):
        with open(pyQsPath, 'r', encoding='utf-8') as file:
            for line in file:
                # 使用strip()方法去除每行末尾可能存在的换行符或空格
                self.pyQuestions.append(line.strip())

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

    def showPyCode(self):
        self.showPic(f'./resource/Lab2/Code{self.pyIndex}.jpg', self.label_py)
    def showPyRes(self):
        self.showPic(f'./resource/Lab2/Result{self.pyIndex}.jpg', self.label_py)
    def pyNext(self):
        self.pyIndex = self.pyIndex + 1 if self.pyIndex < 5 else 1
        self.label_lab2_qs.setText(self.pyQuestions[self.pyIndex-1])

    def showUbuntu(self, button_index):
        self.playVideo(f'./resource/Lab3/{button_index}.mp4', self.widget_ubuntu)

    def showCvCode(self):
        self.showingStatusChange([self.label_cv_img],[self.textBrowser_cv_code])

    def showCvIni(self):
        self.showingStatusChange([self.textBrowser_cv_code],[self.label_cv_img])
        self.showPic('./resource/Lab6/ball_image.jpg', self.label_cv_img)
        self.showCvFlag = 0
        self.pushButton_cv_2.setEnabled(True)

    def showCvContinue(self):
        self.showingStatusChange([self.textBrowser_cv_code],[self.label_cv_img])
        if self.showCvFlag == 0:
            image_path = './resource/Lab6/ball_image_gray.jpg'
        elif self.showCvFlag == 1:
            image_path = './resource/Lab6/ball_image_median.jpg'
        elif self.showCvFlag == 2:
            image_path = './resource/Lab6/ball_image_detected.jpg'
        elif self.showCvFlag == 3:
            image_path = './resource/Lab6/ball_image.jpg'
        self.showPic(image_path, self.label_cv_img)
        self.showCvFlag = self.showCvFlag + 1 if self.showCvFlag < 3 else 0

    def showPfCode(self):
        self.showPic(f'./resource/Lab8/Code.jpg', self.label_pf)
    def showPfRes(self):
        self.showPic(f'./resource/Lab8/Result.jpg', self.label_pf)

    def run_simulation(self):
        # 当按钮被按下时，获取所有doubleSpinBox的值
        speed_value = self.doubleSpinBox_1.value()
        target_x_value = self.doubleSpinBox_2.value()
        target_y_value = self.doubleSpinBox_3.value()
        target_theta_value = self.doubleSpinBox_4.value()

        # 调用walking_sim_demo函数，并传入收集的值
        walking_sim_demo(speed_value, target_x_value, target_y_value, target_theta_value)

    def open_upload_dialog(self):
        # 创建并显示上传对话框
        self.upload_dialog = UploadDialog(self)
        self.upload_dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

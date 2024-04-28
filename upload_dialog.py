import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from ilabx_api import extract_ticket, get_token, post_data_upload, ApiConfig
import json

# 你的API配置信息
api_config = ApiConfig(
    api_base='https://www.ilab-x.com',
    appid='109011',
    secret='vi+dzeDA9gQrYklnGZVe8ezTRes3pWQmwES6NbKfWIA='
    # api_base='http://39.105.173.29',
    # appid='10000',
    # secret='DDO7jw9TAZlLwRLRKSpBWXIlYZe9PKaD5Wc1S5ZQ0U8='
)


class UploadDialog(QDialog):
    def __init__(self, parent=None):
        super(UploadDialog, self).__init__(parent)
        self.init_ui()
        self.access_token = ''
        self.url = ''
        self.resize(320, 240)

    def init_ui(self):
        self.setWindowTitle('成绩上传')

        layout = QVBoxLayout(self)

        # 添加URL输入框
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('请输入URL')
        layout.addWidget(self.url_input)

        # 解析URL按钮
        parse_button = QPushButton('解析URL', self)
        parse_button.clicked.connect(self.parse_url)
        layout.addWidget(parse_button)

        # 上传数据按钮
        upload_button = QPushButton('回传', self)
        upload_button.clicked.connect(self.upload_data)
        layout.addWidget(upload_button)

    def parse_url(self):
        try:
            self.url = self.url_input.text()
            ticket = extract_ticket(self.url)
            # print(f"ticket: {ticket}")
            res_code, token_response = get_token(ticket, api_config)
            print(f"Response code: {res_code}\nToken response: {token_response}")
            if res_code == 200:
                self.access_token = token_response['access_token']
                self.startTime = token_response['create_time']
                QMessageBox.information(self, '成功', 'URL解析成功，Token已获取')
            else:
                QMessageBox.warning(self, '错误', '获取Token失败')
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))

    def upload_data(self):
        if not self.access_token:
            QMessageBox.warning(self, '错误', '无解析的URL或Token未获取')
            return
        data = {
            "username": "mj_2024jqr",
            "title": "仿人足球机器人综合实践",
            "childProjectTitle": "子实验/模块名称",
            "status": 1,
            "score": 100,
            "startTime": self.startTime,
            "endTime": self.startTime+120*1000,
            "timeUsed": 120,
            "appid": "109011",
            "originId": "1008611",
            "steps": [
                {
                    "seq": 1,
                    "title": "实验步骤1",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 2,
                    "title": "实验步骤2",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 3,
                    "title": "实验步骤3",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 4,
                    "title": "实验步骤4",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 5,
                    "title": "实验步骤5",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 6,
                    "title": "实验步骤6",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 7,
                    "title": "实验步骤7",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 8,
                    "title": "实验步骤8",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 9,
                    "title": "实验步骤9",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
                {
                    "seq": 10,
                    "title": "实验步骤10",
                    "startTime": self.startTime,
                    "endTime": self.startTime+120*1000,
                    "timeUsed": 120,
                    "expectTime": 2,
                    "maxScore": 10,
                    "score": 10,
                    "repeatCount": 1,
                    "evaluation": "优",
                    "scoringModel": "赋分模型",
                    "remarks": "备注"
                },
            ]
        }
        try:
            res_code = post_data_upload(data, self.access_token, api_config['api_base'])
            if res_code == 200:
                QMessageBox.information(self, '成功', '数据上传成功')
            else:
                QMessageBox.warning(self, '错误', '数据上传失败')
                print(f"Response code: {res_code}")
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UploadDialog()
    dialog.show()
    sys.exit(app.exec_())

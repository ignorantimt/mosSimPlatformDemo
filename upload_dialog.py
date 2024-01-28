import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from ilabx_api import extract_ticket, get_token, post_data_upload, ApiConfig

# 你的API配置信息
api_config = ApiConfig(
    api_base='你的API基础地址',
    appid='你的APPID',
    secret='你的密钥'
)

# 上传数据的示例payload
example_payload = [1,2]

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
            token_response = get_token(ticket, api_config)
            if token_response.get('code') == 200:
                self.access_token = token_response['access_token']
                QMessageBox.information(self, '成功', 'URL解析成功，Token已获取')
            else:
                QMessageBox.warning(self, '错误', '获取Token失败')
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))

    def upload_data(self):
        if not self.access_token:
            QMessageBox.warning(self, '错误', '无解析的URL或Token未获取')
            return

        try:
            upload_response = post_data_upload(example_payload, self.access_token, api_config['api_base'])
            if upload_response.get('code') == 200:
                QMessageBox.information(self, '成功', '数据上传成功')
            else:
                QMessageBox.warning(self, '错误', '数据上传失败')
        except Exception as e:
            QMessageBox.warning(self, '错误', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UploadDialog()
    dialog.show()
    sys.exit(app.exec_())

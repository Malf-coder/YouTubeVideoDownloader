import sys  # sys нужен для передачи argv в QApplication
import pytube
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import Qt
import UIYouTubeVideo


class ExampleAppWin2(QtWidgets.QMainWindow, UIYouTubeVideo.Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.stream = None
        self.res = None
        self.file_size = None
        self.highest_resolution_stream = None
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Data/77834-play-icons-button-youtube-computer-logo.png'))
        self.dowloand_label.setAlignment(Qt.AlignCenter)
        for i in window.dataStream:
            self.size = window.yt.streams.filter(resolution=i,
                                                 mime_type="video/mp4").first().filesize
            self.comboBox.addItem(f"{i}  {round(self.size / 1024 / 1024)}мб")

        self.dowloand_button.clicked.connect(self.Download)

    def Download(self):

        if self.comboBox.currentText()[:3] == '108':
            self.res = self.comboBox.currentText()[:5]
        else:
            self.res = self.comboBox.currentText()[:4]

        self.file_size = window.yt.streams.filter(resolution=self.res,
                                                  mime_type="video/mp4").first().filesize
        print(self.file_size)
        self.highest_resolution_stream = window.yt.streams.filter(resolution=self.res,
                                                                  mime_type="video/mp4").first()

        self.stream = window.yt.streams.get_by_itag(self.highest_resolution_stream.itag)
        print(self.highest_resolution_stream)
        print(self.stream)
        self.dowloand_label.setText("Загрузка...")
        QApplication.processEvents()
        self.stream.download(output_path=window.directory)
        self.dowloand_label.setText("Загрузка завершена")


class ExampleAppWin1(QtWidgets.QMainWindow, UIYouTubeVideo.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        super().__init__()

        self.dataStream = []
        self.retval = None
        self.url = None
        self.window2 = None
        self.directory = None
        self.stream = None
        self.yt = None

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('Data/77834-play-icons-button-youtube-computer-logo.png'))
        self.msg_box_name = QMessageBox()
        self.pushButton_3.clicked.connect(self.selectDirectory)
        self.pushButton_2.clicked.connect(self.btn_download)
        self.label.setAlignment(Qt.AlignCenter)

    def selectDirectory(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        self.label.setText(f"Путь к папке выбран:\n{self.directory}")

    def btn_download(self):

        if self.lineEdit.text()[:23] == "https://www.youtube.com":
            self.url = self.lineEdit.text()
            if len(self.directory) >= 3:
                self.label.setText("Загрузка информации о видео...\nНе нажимайте кнопки!")

                self.YouVideo()

            else:
                self.Errors("Не выбрана папка для скачивания")

        else:
            self.Errors("Введите правельную ссылку")

    def Errors(self, error):
        self.msg_box_name.setIcon(QMessageBox.Information)
        self.msg_box_name.setText(error)
        self.msg_box_name.setStandardButtons(QMessageBox.Ok)
        self.retval = self.msg_box_name.exec_()

    def YouVideo(self):
        QApplication.processEvents()
        self.yt = pytube.YouTube(self.url)
        self.stream = self.yt.streams.filter(mime_type="video/mp4")

        for stream in self.stream:
            if stream.resolution is not None:
                self.dataStream.append(stream.resolution)
        self.dataStream = list(set(self.dataStream))
        self.hide()
        self.window2 = ExampleAppWin2()
        self.window2.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleAppWin1()
    window.show()
    app.exec_()

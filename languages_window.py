from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from languages import languages_list


class Languages_Window(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.initUi()
        self.parent = parent

    def initUi(self):
        self.move(300 + 10, 100 + 170)
        self.setFixedSize(800, 300)
        self.setWindowTitle('Выбор языка')

        self.scroll = QScrollArea(self)
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        for i in range(len(languages_list)):
            btn = QPushButton(self.gridLayoutWidget)
            btn.setText(languages_list[i])
            btn.setStyleSheet(
                "font-size:15px;"
                "border:1px;"
                "background-color: #D7D7D7;"
            )
            self.gridLayout.addWidget(btn, i % 20, i // 20, 1, 1)
            btn.clicked.connect(lambda x: self.push_thebutton())

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.gridLayoutWidget)
        self.setCentralWidget(self.scroll)

    def push_thebutton(self):
        self.parent.setText(self.sender().text())
        self.hide()

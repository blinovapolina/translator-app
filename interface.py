from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Interface:
    def initUi(self):
        self.move(300, 100)
        self.setFixedSize(1000, 700)
        self.setWindowTitle('Переводчик')

        self.languages_window = None

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 229))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(
            "background-color: rgb(229, 229, 229);"
            "font: 20px \"Microsoft Tai Le\";"
        )
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 100))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.tab_2 = QtWidgets.QWidget()

        for i in range(2):
            if i == 0:
                self.background_widget = QtWidgets.QLabel(self.tab_1)
            else:
                self.background_widget = QtWidgets.QLabel(self.tab_2)
            self.background_widget.setGeometry(QtCore.QRect(0, 0, 1000, 700))
            self.background_widget.setText("")
            self.background_widget.setPixmap(QtGui.QPixmap("images/imgonline-com-ua-Resize-uaNtAByjGwL.jpg"))

        for i in range(2):
            if i == 0:
                self.choose_translated_lang_label = QtWidgets.QLabel(self.tab_1)
            else:
                self.choose_translated_lang_label = QtWidgets.QLabel(self.tab_2)
            self.choose_translated_lang_label.setGeometry(QtCore.QRect(520, 51, 426, 48))
            self.choose_translated_lang_label.setText("")
            self.choose_translated_lang_label.setPixmap(QtGui.QPixmap("images/Rectangle 7.png"))

        for i in range(2):
            if i == 0:
                self.choose_original_lang_label = QtWidgets.QLabel(self.tab_1)
            else:
                self.choose_original_lang_label = QtWidgets.QLabel(self.tab_2)
            self.choose_original_lang_label.setGeometry(QtCore.QRect(54, 51, 426, 48))
            self.choose_original_lang_label.setText("")
            self.choose_original_lang_label.setPixmap(QtGui.QPixmap("images/Rectangle 6.png"))

        for i in range(2):
            if i == 0:
                self.translated_text_label = QtWidgets.QLabel(self.tab_1)
            else:
                self.translated_text_label = QtWidgets.QLabel(self.tab_2)
            self.translated_text_label.setGeometry(QtCore.QRect(559, 140, 377, 446))
            self.translated_text_label.setStyleSheet("background: none;")
            self.translated_text_label.setText("")
            self.translated_text_label.setPixmap(QtGui.QPixmap("images/Rectangle 5.png"))

        for i in range(2):
            if i == 0:
                self.original_text_label = QtWidgets.QLabel(self.tab_1)
            else:
                self.original_text_label = QtWidgets.QLabel(self.tab_2)
            self.original_text_label.setGeometry(QtCore.QRect(66, 140, 376, 446))
            self.original_text_label.setStyleSheet("background-color: none;")
            self.original_text_label.setText("")
            self.original_text_label.setPixmap(QtGui.QPixmap("images/Rectangle 4.png"))

        self.photo_tab2 = QtWidgets.QLabel(self.tab_2)
        self.photo_tab2.setGeometry(QtCore.QRect(430, 40, 131, 71))
        self.photo_tab2.setStyleSheet("background-color: none;")
        self.photo_tab2.setText("")
        self.photo_tab2.setPixmap(QtGui.QPixmap("images/11zon_resized (1).png"))

        self.original_text_tab1 = QtWidgets.QTextEdit(self.tab_1)
        self.original_text_tab1.setPlaceholderText('Начните писать текст')
        self.original_text_tab1.setGeometry(QtCore.QRect(100, 198, 311, 330))
        self.original_text_tab1.setStyleSheet(
            "background-color: rgb(255, 252, 246);"
            "font: 18px \"MS Shell Dlg 2\";"
            "border: 1px dotted;"
        )
        self.original_text_tab1.setAcceptRichText(False)

        self.original_text_tab2 = QtWidgets.QTextEdit(self.tab_2)
        self.original_text_tab2.setPlaceholderText('После загрузки файла здесь появится его содержимое')
        self.original_text_tab2.setReadOnly(True)
        self.original_text_tab2.setGeometry(QtCore.QRect(100, 198, 311, 330))
        self.original_text_tab2.setStyleSheet(
            "background-color: rgb(255, 252, 246);"
            "font: 18px \"MS Shell Dlg 2\";"
            "border: 1px dotted;"
        )
        self.original_text_tab2.setAcceptRichText(False)

        self.translated_text_tab1 = QtWidgets.QTextEdit(self.tab_1)
        self.translated_text_tab1.setGeometry(QtCore.QRect(593, 198, 300, 330))
        self.translated_text_tab1.setStyleSheet(
            "background-color: rgb(202, 199, 255);"
            "font: 18px \"MS Shell Dlg 2\";"
            "border: 1px dotted;"
        )
        self.translated_text_tab1.setReadOnly(True)
        self.translated_text_tab1.setPlaceholderText('Здесь появится перевод')

        self.translated_text_tab2 = QtWidgets.QTextEdit(self.tab_2)
        self.translated_text_tab2.setGeometry(QtCore.QRect(593, 198, 300, 330))
        self.translated_text_tab2.setStyleSheet(
            "background-color: rgb(202, 199, 255);"
            "font: 18px \"MS Shell Dlg 2\";"
            "border: 1px dotted;"
        )
        self.translated_text_tab2.setReadOnly(True)
        self.translated_text_tab2.setPlaceholderText('Здесь появится перевод')

        self.microphone_btn = QtWidgets.QPushButton(self.tab_1)
        self.microphone_btn.setGeometry(QtCore.QRect(129, 541, 26, 26))
        self.microphone_btn.setStyleSheet(
            "border: none;"
            "background-color: none;"
        )
        self.microphone_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/microphone-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.microphone_btn.setIcon(icon)
        self.microphone_btn.setIconSize(QtCore.QSize(26, 26))
        self.microphone_btn.setToolTip('Голосовой ввод')

        self.sound_original_btn = QtWidgets.QPushButton(self.tab_1)
        self.sound_original_btn.setGeometry(QtCore.QRect(86, 539, 30, 30))
        self.sound_original_btn.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.sound_original_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/sound-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound_original_btn.setIcon(icon2)
        self.sound_original_btn.setIconSize(QtCore.QSize(30, 30))
        self.sound_original_btn.setToolTip('Озвучить')

        self.sound_translated_btn = QtWidgets.QPushButton(self.tab_1)
        self.sound_translated_btn.setGeometry(QtCore.QRect(579, 538, 30, 30))
        self.sound_translated_btn.setStyleSheet(
            "border: none; "
            "background: none;"
        )
        self.sound_translated_btn.setText("")
        self.sound_translated_btn.setIcon(icon2)
        self.sound_translated_btn.setIconSize(QtCore.QSize(30, 30))
        self.sound_translated_btn.setToolTip('Озвучить')

        self.copy_original_btn = QtWidgets.QPushButton(self.tab_1)
        self.copy_original_btn.setGeometry(QtCore.QRect(168, 539, 31, 31))
        self.copy_original_btn.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.copy_original_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/copy-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy_original_btn.setIcon(icon1)
        self.copy_original_btn.setIconSize(QtCore.QSize(31, 31))
        self.copy_original_btn.setToolTip('Копировать')

        self.copy_translated_btn = QtWidgets.QPushButton(self.tab_1)
        self.copy_translated_btn.setGeometry(QtCore.QRect(890, 155, 31, 31))
        self.copy_translated_btn.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.copy_translated_btn.setText("")
        self.copy_translated_btn.setIcon(icon1)
        self.copy_translated_btn.setIconSize(QtCore.QSize(31, 31))
        self.copy_translated_btn.setToolTip('Копировать')

        self.change_lang_direction_btn = QtWidgets.QPushButton(self.tab_1)
        self.change_lang_direction_btn.setEnabled(True)
        self.change_lang_direction_btn.setGeometry(QtCore.QRect(440, 45, 118, 60))
        self.change_lang_direction_btn.setMouseTracking(False)
        self.change_lang_direction_btn.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.change_lang_direction_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Group 14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_lang_direction_btn.setIcon(icon3)
        self.change_lang_direction_btn.setIconSize(QtCore.QSize(118, 60))
        self.change_lang_direction_btn.setToolTip('Переключить направление')

        self.delete_original_btn_tab1 = QtWidgets.QPushButton(self.tab_1)
        self.delete_original_btn_tab1.setGeometry(QtCore.QRect(400, 160, 21, 21))
        self.delete_original_btn_tab1.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.delete_original_btn_tab1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Group 5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_original_btn_tab1.setIcon(icon4)
        self.delete_original_btn_tab1.setIconSize(QtCore.QSize(21, 21))
        self.delete_original_btn_tab1.setToolTip('Очистить')

        self.delete_original_btn_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.delete_original_btn_tab2.setGeometry(QtCore.QRect(400, 160, 21, 21))
        self.delete_original_btn_tab2.setStyleSheet(
            "border: none;"
            "background: none;"
        )
        self.delete_original_btn_tab2.setText("")
        self.delete_original_btn_tab2.setIcon(icon4)
        self.delete_original_btn_tab2.setIconSize(QtCore.QSize(21, 21))
        self.delete_original_btn_tab2.setToolTip('Очистить')

        self.choose_original_lang_btn = QPushButton('Выбрать язык', self.tab_1)
        self.choose_original_lang_btn.setStyleSheet(
            "font-size:20px;"
            "border: 1.2px dotted;"
            "background: none;"
        )
        self.choose_original_lang_btn.setGeometry(70, 57, 350, 40)

        self.choose_translated_lang_btn_tab1 = QPushButton('Выбрать язык', self.tab_1)
        self.choose_translated_lang_btn_tab1.setStyleSheet(
            "font-size:20px;"
            "border: 1.2px dotted;"
            "background: none;"
        )
        self.choose_translated_lang_btn_tab1.setGeometry(570, 57, 350, 40)

        self.choose_translated_lang_btn_tab2 = QPushButton('Выбрать язык', self.tab_2)
        self.choose_translated_lang_btn_tab2.setStyleSheet(
            "font-size:20px;"
            "border: 1.2px dotted;"
            "background: none;"
        )
        self.choose_translated_lang_btn_tab2.setGeometry(570, 57, 350, 40)

        self.open_file_button = QPushButton('Выбрать файл (*.txt)', self.tab_2)
        self.open_file_button.setStyleSheet(
            "font-size:20px;"
            "border: 1.2px dotted;"
            "background-color: #A29CFF;"
        )
        self.open_file_button.setGeometry(70, 57, 350, 40)

        self.translate_btn_tab1 = QPushButton('Перевести', self.tab_1)
        self.translate_btn_tab1.setStyleSheet('font-size:20px;')
        self.translate_btn_tab1.setGeometry(430, 600, 120, 40)

        self.translate_btn_tab2 = QPushButton('Перевести', self.tab_2)
        self.translate_btn_tab2.setStyleSheet('font-size:20px;')
        self.translate_btn_tab2.setGeometry(430, 600, 120, 40)

        self.tabWidget.addTab(self.tab_1, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), "Текст")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Документ")

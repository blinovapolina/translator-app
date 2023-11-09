import sys
from PyQt5.QtWidgets import *
from functional_buttons import Functional


class Window(QMainWindow, Functional):
    def __init__(self):
        super(Window, self).__init__()
        self.initUi()

        self.copy_original_btn.clicked.connect(lambda x: self.copy_text())
        self.copy_translated_btn.clicked.connect(lambda x: self.copy_text())
        self.delete_original_btn_tab1.clicked.connect(lambda x: self.delete_text())
        self.delete_original_btn_tab2.clicked.connect(lambda x: self.delete_text())
        self.choose_original_lang_btn.clicked.connect(lambda x: self.choose_lang())
        self.choose_translated_lang_btn_tab1.clicked.connect(lambda x: self.choose_lang())
        self.choose_translated_lang_btn_tab2.clicked.connect(lambda x: self.choose_lang())
        self.translate_btn_tab1.clicked.connect(self.translate_text)
        self.translate_btn_tab2.clicked.connect(self.translate_text)
        self.microphone_btn.clicked.connect(lambda x: self.microphone())
        self.sound_original_btn.clicked.connect(lambda x: self.sound_text())
        self.sound_translated_btn.clicked.connect(lambda x: self.sound_text())
        self.open_file_button.clicked.connect(self.open_file_dialog)
        self.change_lang_direction_btn.clicked.connect(lambda x: self.change_direction())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())

from PyQt5.QtWidgets import *
from googletrans import Translator
import speech_recognition as sr
import gtts
from gtts import gTTS
import os
from playsound import playsound
from languages import languages_dict
from languages_window import Languages_Window
from interface import Interface


class Functional(Interface):
    def translate_text(self):
        try:
            if self.sender() == self.translate_btn_tab1:
                if self.choose_translated_lang_btn_tab1.text() == 'Выбрать язык' or \
                        self.choose_original_lang_btn.text() == 'Выбрать язык':
                    QMessageBox.information(self, "Информация", "Выберите язык перед переводом")
                elif set(self.original_text_tab1.toPlainText()) == {' '} or self.original_text_tab1.toPlainText() == '':
                    QMessageBox.information(self, "Информация", "Введите минимум 1 символ для перевода")
                else:
                    text = self.original_text_tab1.toPlainText()
                    translator = Translator()
                    translation = translator.translate(text,
                                                       dest=languages_dict[self.choose_translated_lang_btn_tab1.text()],
                                                       str=languages_dict[self.choose_original_lang_btn.text()])
                    self.translated_text_tab1.setPlainText(translation.text)
            elif self.sender() == self.translate_btn_tab2:
                if self.choose_translated_lang_btn_tab2.text() == 'Выбрать язык':
                    QMessageBox.information(self, "Информация", "Выберите язык перед переводом")
                elif set(self.original_text_tab2.toPlainText()) == {' '} or self.original_text_tab2.toPlainText() == '':
                    QMessageBox.information(self, "Информация", "Загрузите файл для перевода")
                else:
                    text = self.original_text_tab2.toPlainText()
                    translator = Translator()
                    translation = translator.translate(text,
                                                       dest=languages_dict[self.choose_translated_lang_btn_tab2.text()])
                    self.translated_text_tab2.setPlainText(translation.text)
        except Exception as e:
            QMessageBox.information(self, "Информация", "Ошибка при переводе")

    def choose_lang(self):
        if not self.languages_window:
            self.languages_window = Languages_Window(self.sender())
        self.languages_window.show()
        self.languages_window = None

    def microphone(self):
        try:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            sr.LANGUAGE = languages_dict[self.choose_original_lang_btn.text()]

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language=languages_dict[self.choose_original_lang_btn.text()])
                self.original_text_tab1.setText(text)
        except KeyError:
            self.original_text_tab1.clear()
            QMessageBox.information(self, "Информация", "Выберите язык перед голосовым вводом")
        except sr.exceptions.UnknownValueError:
            self.original_text_tab1.clear()
            QMessageBox.information(self, "Информация", "Ошибка при голосовом вводе. "
                                                        "Нажмите на кнопку и повторите фразу")
        except Exception as e:
            QMessageBox.information(self, "Информация", "Ошибка при голосовом вводе")

    def sound_text(self):
        try:
            item_text = self.original_text_tab1 if self.sender() == self.sound_original_btn \
                else self.translated_text_tab1
            item_lang = languages_dict[self.choose_original_lang_btn.text()] \
                if self.sender() == self.sound_original_btn \
                else languages_dict[self.choose_translated_lang_btn_tab1.text()]
            if item_lang not in gtts.lang.tts_langs().keys():
                QMessageBox.information(self, "Информация", "Выбранный язык пока не может быть озвучен")
            else:
                tts = gTTS(item_text.toPlainText(), lang=item_lang)
                tts.save('output.mp3')
                playsound('output.mp3')
                os.remove('output.mp3')
        except KeyError:
            QMessageBox.information(self, "Информация", "Выберите язык перед озвучиванием")
        except AssertionError:
            QMessageBox.information(self, "Информация", "Введите минимум 1 символ для озвучивания")
        except Exception as e:
            QMessageBox.information(self, "Информация", "Ошибка при озвучивании")

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.original_text_tab1.toPlainText()) if self.sender() == self.copy_original_btn \
            else clipboard.setText(self.translated_text_tab1.toPlainText())
        QMessageBox.information(self, "Информация", "Текст скопирован в буфер обмена") if clipboard.text() != '' \
            else QMessageBox.information(self, "Информация", "Введите текст, чтобы его скопировать")

    def delete_text(self):
        if self.sender() == self.delete_original_btn_tab1:
            self.original_text_tab1.clear()
            self.translated_text_tab1.clear()
        elif self.sender() == self.delete_original_btn_tab2:
            self.original_text_tab2.clear()
            self.translated_text_tab2.clear()

    def open_file_dialog(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текстовый файл (*.txt)')[0]
            with open(fname, 'r', encoding='utf-8') as file:
                file_contents = file.readlines()
                self.original_text_tab2.setPlainText(''.join(file_contents))
        except FileNotFoundError:
            QMessageBox.information(self, "Информация", "Вы не выбрали файл")
        except UnicodeDecodeError as e:
            QMessageBox.information(self, "Информация", "Не удалось успешно декодировать файл")
        except Exception as e:
            QMessageBox.information(self, "Информация", "Ошибка при прочтении файла")

    def change_direction(self):
        try:
            if self.choose_translated_lang_btn_tab1.text() == 'Выбрать язык' or \
                    self.choose_original_lang_btn.text() == 'Выбрать язык':
                QMessageBox.information(self, "Информация", "Выберите язык")
            else:
                original_language = self.choose_original_lang_btn.text()
                self.choose_original_lang_btn.setText(self.choose_translated_lang_btn_tab1.text())
                self.choose_translated_lang_btn_tab1.setText(original_language)
                self.original_text_tab1.clear()
                self.translated_text_tab1.clear()
        except Exception as e:
            pass

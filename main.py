import ui
import sys
import googletrans
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

langs = {
'South African Dutch': 'af',
'Albanian': 'sq',
'Amharic': 'am',
'Arabic': 'ar',
'Armenian': 'hy',
'Azerbaijani': 'az',
'Basque': 'eu',
'Black language': 'be',
'Bengali': 'bn',
'Bosnian': 'bs',
'Bulgarian': 'bg',
'Catalan': 'ca',
"The Cebu Language": "ceb",
'Chinese': 'zh',
'Chinese': 'zh-TW',
'Cosica': 'co',
'Croatian': 'hr',
'Czech': 'cs',
'Danish': 'da',
'Dutch': 'nl',
'English': 'en',
'Worn': 'eo',
'Estonian': 'et',
'Finnish': 'fi',
"French": "fr",
'Friesi': 'fy',
'Galicia': 'gl',
'George': 'ka',
'German': 'de',
'Greek': 'el',
'Gujrat': 'gu',
'Haitian Creole': 'ht',
'Husa': 'ha',
'Hawaiian': 'haw',
'Indian': 'hi',
'Hungarian': 'hu',
'Icelandic': 'is',
'Ibo language': 'ig',
'Indonesian': 'id',
'Irish': 'ga',
"Italian": 'it',
'Japanese': 'ja',
'Javan': 'jw',
'Kanada': 'kn',
'Kazakh': 'kk',
'Khmer': 'km',
'Korean': 'ko',
'Kurdish': 'ku',
'Kyrgyz': 'ky',
'Lao': 'lo',
'Latin': 'la',
'Latvian': 'lv',
'Lithuanian': 'lt',
'Luxemburger': 'lb',
'Macedonian': 'mk',
'Margash': 'mg',
'Marais': 'ms',
'Marayalam': 'ml',
'Maltese': 'mt',
'Māori': 'mi',
'Marathi': 'mr',
'Mongolian': 'mn',
'Myanmar': 'my',
'Nepali': 'ne',
'Norwegian': 'no',
'Niyanza (Sicheva)': 'ny',
"Pashto": "ps",
'Persia': 'fa',
'Polish': 'pl',
'Portuguese': 'pt',
'Punjabi': 'pa',
'Romanian': 'ro',
'Russian': 'ru',
'Samoa': 'sm',
'Scotland Gaelic': 'gd',
'Serbian': 'sr',
'Sesotho': 'st',
'Shona': 'sn',
'Twiss German': 'sd',
'Sanjaro': 'si',
'Slovak': 'sk',
'Slovene': 'sl',
'Somali': 'so',
'Spanish': 'es',
"Photo": "su",
'Swahili': 'sw',
"Swedish": 'sv',
"Tagalo": "tl",
"Tajik": 'tg',
'Tamil': 'ta',
'Terugu': 'te',
'Thai': 'th',
'Turkish': 'tr',
'Ukrainian': 'uk',
'Urdu': 'ur',
'Uzbek': 'uz',
'Vietnamese': 'vi',
'Welsh': 'cy',
'Bantu': 'xh',
'Yiddish': 'yi',
'Yoruba': 'yo',
"Zulu": "zu"
}

class Main(QtWidgets.QMainWindow, ui.Ui_Form):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.add_languages()
        self.pushButton.clicked.connect(self.translate)

    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())
            self.comboBox_2.addItem(x.capitalize())

    def translate(self):
        try:
            text_1 = self.textEdit.toPlainText()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()
            translator = googletrans.Translator()
            translate = translator.translate(text_1, src=lang_1, dest=lang_2)
            self.textEdit_2.setText(translate.text)
            langvalue = translator.detect(text_1).lang
            for key, value in langs.items():
                if value == langvalue:
                    lang_1 = self.comboBox.setCurrentText(key)
        except Exception as e:
            self.error_message(e)

    def error_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('error')
        msg.setText(str(text))
        msg.exec_()


if __name__ == '__main__':
    a = QtWidgets.QApplication(sys.argv)
    app = Main()
    app.show()
    a.exec_()

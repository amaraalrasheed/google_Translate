from googletrans import Translator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.uic import loadUiType
from os import path
import sys
import re
from gui import Ui_MainWindow as gui
#UI conductor
#FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__),"main.ui"))
class MainApp(QMainWindow,gui):
        def __init__(self, parent=None):
              super(MainApp,self).__init__(parent)
              QMainWindow.__init__(self)
              self.setupUi(self)
              self.buttons()
              self.setWindowTitle("Translate from Google")

#Programm Core
        def main(self):
            the_text= self.lineEdit.text()
            translator = Translator()
            translations = translator.translate(the_text, dest='ar')
            translations = str(translations)
            #the arabic text:
            arabic_script = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', translations)
            full_script = translations.split(",")
            self.textEdit.setText(arabic_script)
            # detect language
            det_lang= full_script[0].split("=")
            self.label_2.setText(det_lang[1])
        def clear(self):
            self.lineEdit.setText("insert the English Text here")
            self.textEdit.setText(" ")

        def quits(self):
            sys.exit()
        def buttons(self):
            self.pushButton.clicked.connect(self.main)
            self.pushButton_2.clicked.connect(self.clear)
            self.pushButton_3.clicked.connect(self.quits)
        
def main():       
       app = QApplication(sys.argv)
       window = MainApp()
       window.show()
       app.exec_()
main()
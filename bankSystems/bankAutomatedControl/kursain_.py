#!/usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItems(["age", "job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week", "duration", "campaign", "pdays", "previous", "poutcome", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m", "nr_employed", "y"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
      self.button = QPushButton('Test', self)
      self.button.clicked.connect(self.handleButton)
      layout = QVBoxLayout(self)

      self.textFeild = QTextEdit(parent)
      # self.textFeild.setReadOnly(True)
      self.textFeild.setLineWrapMode(QTextEdit.NoWrap)
      self.textFeild.insertPlainText("hello from the other sideee")
      
      font = self.textFeild.font()
      font.setFamily("Courier")
      font.setPointSize(10)

      layout.addWidget(self.cb)
      layout.addWidget(self.textFeild)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print "Items in the list are :"
		
      for count in range(self.cb.count()):
         print self.cb.itemText(count)
      print "Current index",i,"selection changed ",self.cb.currentText()
   def handleButton(self):
      print ('Hello World')
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()

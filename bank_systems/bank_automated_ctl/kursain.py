#!/usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import LogisticRegression

class combodemo(QWidget):
    def __init__(self, parent = None):
        super(combodemo, self).__init__(parent)
        
        layout = QHBoxLayout()
        # self.cb = QComboBox()
        data_feild= ["age", "job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week", "duration", "campaign", "pdays", "previous", "poutcome", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m", "nr_employed", "y"]
        # self.cb.addItems(data_feild)

        user_submission_field = data_feild[:] # copy not reference
        self.textboxSubmitList = []
        for data_field_item in data_feild:
             # print(data_feild.index(data_field_item))
             # self.textFeild = QTextEdit(parent)
             # self.textFeild.setReadOnly(True)
             # self.textFeild.setLineWrapMode(QTextEdit.NoWrap)
             # self.textFeild.insertPlainText(data_field_item)
             # self.textFeild.resize(10,10);
             # font = self.textFeild.font()
             # font.setFamily("Courier")
             # font.setPointSize(10)
             self.textboxData = QLabel(self)
             self.textboxData.move(100, 40 * data_feild.index(data_field_item))
             self.textboxData.resize(200,40)
             self.textboxData.setText(data_field_item)

             self.textboxSubmit = QLineEdit(self)
             self.textboxSubmit.move(350, 40 * data_feild.index(data_field_item))
             self.textboxSubmit.resize(230,40)
             self.textboxSubmit.setText(data_field_item)
             self.textboxSubmitList.append(self.textboxSubmit)

             layout.addWidget(self.textboxSubmit)
             layout.addWidget(self.textboxData)

        print(self.textboxSubmitList[:])
        # button push
        # self.cb.currentIndexChanged.connect(self.selectionchange)
        self.button = QPushButton('Test', self)
        self.button.move(200, 900)
        self.button.resize(200,50)
        self.button.clicked.connect(self.handleButton)
        self.showMaximized() # fullscreen
     
        # self.textFeild = QTextEdit(parent)
        # # self.textFeild.setReadOnly(True)
        # self.textFeild.setLineWrapMode(QTextEdit.NoWrap)
        # self.textFeild.insertPlainText("hello from the other sideee")

        # layout.addWidget(self.textFeild)
        # layout.addWidget(self.textbox)
        # layout.addWidget(self.cb)
        layout.addWidget(self.button)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

    # def selectionchange(self,i):
    #     print "Items in the list are :"
    #       	
    #     for count in range(self.cb.count()):
    #        print self.cb.itemText(count)
    #     print "Current index",i,"selection changed ",self.cb.currentText()

    def handleButton(self):
        print("test:", str(self.get_textbox_value(1)))

    def get_textbox_value(self, i):
        return self.textboxSubmitList[i].displayText()
		
def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

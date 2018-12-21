#!/usr/bin/python3
import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from LogisticRegression import logic

class combodemo(QWidget):
    def __init__(self, parent = None):
        super(combodemo, self).__init__(parent)
        self.model_ = logic()
        self.layout = QHBoxLayout()
        # self.cb = QComboBox()
        # inference_data_names = ["age", "duration", "campaign", "pdays", "previous", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m", "nr_employed", "y"]
        inference_data_names =       ['previous', 'euribor3m', 'job_blue-collar', 'job_retired','job_services', 'job_student', 'default_no', 'month_aug', 'month_dec', 'month_jul', 'month_nov', 'month_oct', 'month_sep', 'day_of_week_fri', 'day_of_week_wed', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success']
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        # self.cb.addItems(inference_data_names)
        inference_data_values = list(self.model_.getDataSampleValue().values)
        inference_data_values = list(inference_data_values[0])
        print("*&************************ inference_data_values: ", inference_data_values)
        user_submission_field = inference_data_names[:] # copy not reference
        self.textboxSubmitList = []
        for inference_data_names_item in inference_data_names:
            self.textboxData = QLabel(self)
            self.textboxData.move(100, 40 * inference_data_names.index(inference_data_names_item))
            self.textboxData.resize(200,40)
            self.textboxData.setText(inference_data_names_item)
            self.layout.addWidget(self.textboxData)
        
        draw_index = 0

        for inference_data_values_item in inference_data_values:
            self.textboxSubmit = QLineEdit(self)
            self.textboxSubmit.move(350, 40 * draw_index)
            self.textboxSubmit.resize(230,40)
            self.textboxSubmit.setText(str(inference_data_values_item))
            self.textboxSubmitList.append(self.textboxSubmit.text())
            self.layout.addWidget(self.textboxSubmit)
            draw_index += 1
            print(inference_data_values_item)

        print(self.textboxSubmitList[:])
        # button push
        # self.cb.currentIndexChanged.connect(self.selectionchange)
        self.buttonTrain = QPushButton('Train', self)
        self.buttonTrain.move(200, 900)
        self.buttonTrain.resize(200,50)
        self.buttonTrain.clicked.connect(self.handleButtonTrain)
     
        self.buttonInference = QPushButton('Inference', self)
        self.buttonInference.move(400, 900)
        self.buttonInference.resize(200,50)
        self.buttonInference.clicked.connect(self.handleButtonInference)


        self.showMaximized() # fullscreen
        # self.textFeild = QTextEdit(parent)
        # # self.textFeild.setReadOnly(True)
        # self.textFeild.setLineWrapMode(QTextEdit.NoWrap)
        # self.textFeild.insertPlainText("hello from the other sideee")

        # self.layout.addWidget(self.textFeild)
        # self.layout.addWidget(self.textbox)
        # self.layout.addWidget(self.cb)
        self.layout.addWidget(self.buttonTrain)
        self.layout.addWidget(self.buttonInference)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.setWindowTitle("combo box demo")

    # def selectionchange(self,i):
    #     print "Items in the list are :"
    #       	
    #     for count in range(self.cb.count()):
    #        print self.cb.itemText(count)
    #     print "Current index",i,"selection changed ",self.cb.currentText()

    def access_widget(self, i):
        item = self.layout.itemAt(11)
        print("type: ", type(self.layout))
        line_edit = item.parentWidget()
        return line_edit

    def handleButtonTrain(self):
        self.model_.train()
        print("successfully trained") 
    def handleButtonInference(self):
        self.model_.setTestData(np.array(self.model_.getDataSampleValue()))
        print("debug: ", np.array(self.model_.getDataSampleValue()))
        data_ = np.array([[]])
        print("debug0: ", data_.shape)
        # data_ = np.append(data_, np.array((self.textboxSubmitList[:])))
        # data_ = np.append(data_, np.array(self.textboxSubmitList[:]), axis=0)
        # index = 0
        # for i in range(10):
        #     print("access_widget: " , self.access_widget(i))

        print("debug send inference: ", data_)
        zipped = self.textboxSubmitList[:]
        data = print("zipped: ", zipped)
        # data_ = pd.DataFrame(data)
        # # self.model_.setTestData(np.array(np.array(self.textboxSubmitList[:]).reshape(-1,18)))
        # self.model_.setTestData(data_)
        # data_ = pd.DataFrame(data_)
        result = self.model_.inference()
        print("inference result: ", result)
        if (result[0][0] > 0.5):
            self.messageBox = QMessageBox.information(self, 'inference pass', "give " + str(result[0][0]), QMessageBox.Ok)
            self.layout.addWidget(self.messageBox)
        else:
            self.messageBox = QMessageBox.information(self, 'inference pass', "don't give " + str(result[0][0]),QMessageBox.Ok)
            self.layout.addWidget(self.messageBox)
        # print("successfuly pass inference: ", self.model_.inference())

    def get_textbox_value(self, i):
        return self.textboxSubmitList[i].displayText()
		
def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

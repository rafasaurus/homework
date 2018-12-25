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
        self.data_to_inference = []
        inference_data_names = ['previous', 'euribor3m', 'job_blue-collar', 'job_retired','job_services', 'job_student', 'default_no', 'month_aug', 'month_dec', 'month_jul', 'month_nov', 'month_oct', 'month_sep', 'day_of_week_fri', 'day_of_week_wed', 'poutcome_failure', 'poutcome_nonexistent', 'poutcome_success']
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        inference_data_values = list(self.model_.getDataSampleValue().values)
        inference_data_values = list(inference_data_values[0])
        # print("************************* inference_data_values: ", inference_data_values) user_submission_field = inference_data_names[:] # copy not reference # info RFE
        self.textboxData = QLabel(self)
        self.textboxData.move(100, 40 * 2)
        self.textboxData.resize(400,40)
        self.textboxData.setText("After The Recursive Feature Elimination")
        self.layout.addWidget(self.textboxData)
        self.textboxSubmitList = []

        for inference_data_names_item in inference_data_names:
            self.textboxData = QLabel(self)
            self.textboxData.move(100, 40 * (3 + inference_data_names.index(inference_data_names_item)))
            self.textboxData.resize(200,40)
            self.textboxData.setText(inference_data_names_item)
            self.layout.addWidget(self.textboxData)
        
        draw_index = 3
        for inference_data_values_item in inference_data_values:
            self.textboxSubmit = QLineEdit(self)
            self.textboxSubmit.move(350, 40 * draw_index)
            self.textboxSubmit.resize(130,40)
            self.textboxSubmit.setText(str(inference_data_values_item))
            self.textboxSubmitList.append(self.textboxSubmit.text())
            self.layout.addWidget(self.textboxSubmit)
            draw_index += 1
            # print(inference_data_values_item)

        # -------------------------- info ekamut
        self.textboxData = QLabel(self)
        self.textboxData.move(550, 40 * 1)
        self.textboxData.setText("եկամուտ")
        self.layout.addWidget(self.textboxData)
        self.textboxSubmitList = []

        # ------------------------- ekamut widget number 38
        self.textboxSubmit = QLineEdit(self)
        self.textboxSubmit.move(550, 40 * 2)
        self.textboxSubmit.resize(100,40)
        self.textboxSubmit.setText(str(200000))
        self.textboxSubmitList.append(self.textboxSubmit.text())
        self.layout.addWidget(self.textboxSubmit)
        # print("38:", self.access_widget(38).text())

        # -------------------------- info percentage widget number 40
        self.textboxData = QLabel(self)
        self.textboxData.move(700, 40 * 1)
        self.textboxData.resize(200,40)
        self.textboxData.setText("տոկոսադրույք")
        self.layout.addWidget(self.textboxData)
        self.textboxSubmitList = []

        # percentage lineEdit 
        self.textboxSubmit = QLineEdit(self)
        self.textboxSubmit.move(700, 40 * 2)
        self.textboxSubmit.resize(50,40)
        self.textboxSubmit.setText(str(20))
        self.textboxSubmitList.append(self.textboxSubmit.text())
        self.layout.addWidget(self.textboxSubmit)

        # -------------------------- months
        self.textboxData = QLabel(self)
        self.textboxData.move(900, 40 * 1)
        self.textboxData.resize(200,40)
        self.textboxData.setText("տևողություն(ամիս)")
        self.layout.addWidget(self.textboxData)
        self.textboxSubmitList = []

        # months lineEdit 
        self.textboxSubmit = QLineEdit(self)
        self.textboxSubmit.move(900, 40 * 2)
        self.textboxSubmit.resize(50,40)
        self.textboxSubmit.setText(str(5))
        self.textboxSubmitList.append(self.textboxSubmit.text())
        self.layout.addWidget(self.textboxSubmit)

        # renta_after_months
        self.rentaLabel= QLabel(self)
        self.rentaLabel.move(1200, 40 * 1)
        self.rentaLabel.resize(200,40)
        self.rentaLabel.setText("մնացորդային գումար")
        self.layout.addWidget(self.rentaLabel)
        self.textboxSubmitList = []

        # percentage lineEdit 
        self.rentaLineEdit= QLineEdit(self)
        self.rentaLineEdit.move(1200, 40 * 2)
        self.rentaLineEdit.resize(200,40)
        self.rentaLineEdit.setText(str(0))
        self.textboxSubmitList.append(self.rentaLineEdit.text())
        self.layout.addWidget(self.rentaLineEdit)

        # table label
        self.rentaLabel= QLabel(self)
        self.rentaLabel.move(600, 320)
        self.rentaLabel.resize(200,40)
        self.rentaLabel.setText("Ամսեկան պլան")
        self.layout.addWidget(self.rentaLabel)
        self.textboxSubmitList = []

        # table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setHorizontalHeaderLabels(['ամիս', 'գումար'])
        self.tableWidget.setRowCount(int(self.access_widget(42).text()))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, 500)
        self.tableWidget.move(600, 350)
        self.tableWidget.resize(100, int(self.access_widget(42).text()) * 50)

        # buttons
        self.buttonTrain = QPushButton('Train', self)
        self.buttonTrain.move(200, 900)
        self.buttonTrain.resize(200,50)
        self.buttonTrain.clicked.connect(self.handleButtonTrain)
     
        self.buttonInference = QPushButton('Inference', self)
        self.buttonInference.move(400, 900)
        self.buttonInference.resize(200,50)
        self.buttonInference.clicked.connect(self.handleButtonInference)

        self.buttonInference = QPushButton('update_renta', self)
        self.buttonInference.move(600, 200)
        self.buttonInference.resize(200,50)
        self.buttonInference.clicked.connect(self.handleRentaUpdate)
        # self.layout.addWidget(self.buttonTrain)
        # self.layout.addWidget(self.buttonInference)

        # ---------------------------- վարկի տեսակներ
        loan_names = ["գյուղատնտեսական", "առևտրային", "ավտովարկ", "ուսումնական", "լոմբարդային", "հիփոթեքային" ]
        self.formLayout= QFormLayout(self)
        self.cb = QComboBox(self)
        self.cb.currentIndexChanged.connect(self.selectionchange)
        self.cb.addItems(loan_names)
        self.cb.move(500, 500)
        self.cb.setFixedSize(300, 35)



        # print("width: ", width)
        # self.cb.setMinimumWidth(width);
        # ----------------------------

        self.showMaximized() # fullscreen
        # self.textFeild = QTextEdit(parent)
        # # self.textFeild.setReadOnly(True)
        # self.textFeild.setLineWrapMode(QTextEdit.NoWrap)
        # self.textFeild.insertPlainText("hello from the other sideee")

        # self.layout.addWidget(self.textFeild)
        # self.layout.addWidget(self.textbox)
        self.formLayout.addRow(self.cb)
        # self.setLayout(self.layout)
        self.setLayout(self.formLayout)
        self.setWindowTitle("demo")

    def selectionchange(self,i):
        print("Items in the list are :")
        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index",i,"selection changed ",self.cb.currentText())
        if i == 0:
            self.change_widget_value(40, 10) # գյուղատնտեսական percentage
        elif i == 1:
            self.change_widget_value(40, 20) # առևտրային percentage
        elif i == 2:
            self.change_widget_value(40, 17) # ավտովարկ percentage
        elif i == 3:
            self.change_widget_value(40, 12) # ուսումնական percentage
        elif i == 4:
            self.change_widget_value(40, 30) # լոմբարդային percentage
        elif i == 5:
            self.change_widget_value(40, 24) # հիփոթեքային percentage

    def access_widget(self, i): # accessing each QLineWidget
        item = self.layout.itemAt(i)
        line_edit = item.widget()
        return line_edit

    def change_widget_value(self, i, value): # accessing each QLineWidget
        item = self.layout.itemAt(i)
        line_edit = item.widget()
        line_edit.setText(str(value))

    def handleButtonTrain(self):
        self.model_.train()
        print("successfully trained")

    def renta_after_month_pass(self, income, percentage, month): # how much will overall dept be after "time" months
        percentage /= 100
        back = income * (1 + percentage)**month
        for i in range(1, month + 1): # in years
            # table value update
            back -= income * percentage*i
            self.tableWidget.setItem(i - 1, 0,  QTableWidgetItem(str(int(back))))
        return int(back)

    def handleRentaUpdate(self):
        income = int(self.access_widget(38).text())
        percentage = int(self.access_widget(40).text())
        months = int(self.access_widget(42).text())
        self.rentaLineEdit.setText(str(self.renta_after_month_pass(income, percentage, months)))

        # table size update
        self.tableWidget.setRowCount(int(self.access_widget(42).text()))
        self.tableWidget.resize(100, int(self.access_widget(42).text()) * 50)

    def handleButtonInference(self):

        # get inferece data from QLineEdit
        self.data_to_inference = []
        for i in range(19, 37):
            self.data_to_inference.append(float(self.access_widget(i).text())) 

        # changin data into a good shape for inference
        inference_array = np.array(self.data_to_inference)
        inference_array = inference_array.reshape(1, -1)
        self.model_.setTestData(inference_array) # or for sample data use np_array(self.model_.getDataSampleValue())
        # get the result
        result = self.model_.inference()
        # check result
        if (result[0][0] > 0.5):
            self.messageBox = QMessageBox.information(self, 'inference pass', "give " + str(result[0][0]), QMessageBox.Ok)
            self.layout.addWidget(self.messageBox)
        else:
            self.messageBox = QMessageBox.information(self, 'inference pass', "don't give " + str(result[0][0]),QMessageBox.Ok)
            self.layout.addWidget(self.messageBox)
        print("successfuly pass inference: ", self.model_.inference())

    def get_textbox_value(self, i):
        return self.textboxSubmitList[i].displayText()
		
def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

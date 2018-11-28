#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout
from LogisticRegression import logic

class combodemo(QWidget):
    def __init__(self, parent = None):
        super(combodemo, self).__init__(parent)
        self.model_ = logic()
        layout = QHBoxLayout()
        # self.cb = QComboBox()
        inference_data_names = ["age", "job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week", "duration", "campaign", "pdays", "previous", "poutcome", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m", "nr_employed", "y"]
        # self.cb.addItems(inference_data_names)
        inference_data_values = list(self.model_.getDataSampleValue())
        print("*&************************ inference_data_values: ", inference_data_values)
        user_submission_field = inference_data_names[:] # copy not reference
        self.textboxSubmitList = []
        for inference_data_names_item in inference_data_names:
             self.textboxData = QLabel(self)
             self.textboxData.move(100, 40 * inference_data_names.index(inference_data_names_item))
             self.textboxData.resize(200,40)
             self.textboxData.setText(inference_data_names_item)
             layout.addWidget(self.textboxData)

        for inference_data_values_item in inference_data_values:
             self.textboxSubmit = QLineEdit(self)
             self.textboxSubmit.move(350, 40 * inference_data_values.index(inference_data_values_item))
             self.textboxSubmit.resize(230,40)
             self.textboxSubmit.setText(inference_data_values_item)
             self.textboxSubmitList.append(self.textboxSubmit.text())
             layout.addWidget(self.textboxSubmit)

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

        # layout.addWidget(self.textFeild)
        # layout.addWidget(self.textbox)
        # layout.addWidget(self.cb)
        layout.addWidget(self.buttonTrain)
        layout.addWidget(self.buttonInference)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.setWindowTitle("combo box demo")

    # def selectionchange(self,i):
    #     print "Items in the list are :"
    #       	
    #     for count in range(self.cb.count()):
    #        print self.cb.itemText(count)
    #     print "Current index",i,"selection changed ",self.cb.currentText()

    def handleButtonTrain(self):
        self.model_.train()
        print("successfully trained")

    def handleButtonInference(self):
        self.model_.setTestData(self.textboxSubmitList[:])
        self.model_.inference()
        print("successfuly pass inference")

    def get_textbox_value(self, i):
        return self.textboxSubmitList[i].displayText()
		
def main():
    app = QApplication(sys.argv)
    ex = combodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

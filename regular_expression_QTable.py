
import os
from typing import List

import regular_expression_re
from regular_expression_re import *


print(regular_expression_re.df)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

df = {
    'stock_nm': regular_expression_re.text2df(text).인컴,
    'general_nm': regular_expression_re.text2df(text).general,
    'Code': regular_expression_re.text2df(text).ticker
}
column_idx_lookup = {'stock_nm': 0, 'general_nm': 1, 'Code': 2}

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(1800, 600, 800, 600)


        # Text Edit Line 추가해봄
        self.TextEdit  =QTextEdit("", self)
        self.TextEdit.move(400,0)
        self.TextEdit.resize(200,400)

        self.btn_run = QPushButton('Run', self)
        self.btn_run.move(400,400)
        self.btn_run.resize(200,50 )
        self.btn_run.clicked.connect(self.btn_run_clicked)


        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(len(regular_expression_re.text2df(text)))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.setTableWidgetData()

        # self.pushButton = QPushButton("Input number")
        # self.pushButton.clicked.connect(self.pushButtonClicked)
        # self.label = QLabel()
        # self.textEdit = QTextEdit()
        # self.pushButton= QPushButton('저장')
        # self.pushButtonClicked()
        #
        layout = QVBoxLayout()
        layout.addWidget(self.TextEdit)
        layout.addWidget(self.btn_run)

#        layout = QVBoxLayout()
        #layout.addWidget(self.btn_run)
        #layout.addWidget(self.label)
        layout.addStretch(1)

        leftLayout = QVBoxLayout()
        #leftLayout.addWidget(self.canvas)
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        rightLayout = QVBoxLayout()
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def btn_run_clicked(self):
        regular_expression_re.text = self.TextEdit.toPlainText()
        #print(regular_expression_re.text)
        text2 = regular_expression_re.text
        print(text2)
    #    print(self.text2df(text))
        global df2

        df2 = {
            'stock_nm': regular_expression_re.text2df(text2).인컴,
            'general_nm': regular_expression_re.text2df(text2).general,
            'Code': regular_expression_re.text2df(text2).ticker
        }
        print(df2)
        column_idx_lookup = {'stock_nm': 0, 'general_nm': 1, 'Code': 2}
        self.tableWidget.setRowCount(len(regular_expression_re.text2df(text2)))
        self.setTableWidgetData()

    #def text2df(text):
    #   print(f'{text} : Functon text2df  is RUN start')



    def setTableWidgetData(self):
        try:
            column_headers = ['stock_nm', 'general_nm', 'Code']
            self.tableWidget.setHorizontalHeaderLabels(column_headers)

            for k, v in df2.items():
                col = column_idx_lookup[k]
                for row, val in enumerate(v):
                    item = QTableWidgetItem(val)
                    if col == 2:
                        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                    self.tableWidget.setItem(row, col, item)

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()


        except:
            column_headers = ['stock_nm', 'general_nm', 'Code']
            self.tableWidget.setHorizontalHeaderLabels(column_headers)

            for k, v in df.items():
                col = column_idx_lookup[k]
                for row, val in enumerate(v):
                    item = QTableWidgetItem(val)
                    if col == 2:
                        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                    self.tableWidget.setItem(row, col, item)

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

# # ----------------------------
# import sys
# from PyQt5.QtWidgets import *
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUI()
#
#     def setupUI(self):
#         self.setGeometry(800, 200, 300, 300)
#         self.setWindowTitle("PyStock v0.1")
#
#         self.pushButton = QPushButton("Input number")
#         self.pushButton.clicked.connect(self.pushButtonClicked)
#         self.label = QLabel()
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.pushButton)
#         layout.addWidget(self.label)
#
#         self.setLayout(layout)
#
#     def pushButtonClicked(self):
#         text, ok = QInputDialog.getInt(self, '매수 수량', '매수 수량을 입력하세요.')
#         if ok:
#             self.label.setText(str(text))
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()
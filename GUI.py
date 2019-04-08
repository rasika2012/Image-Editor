# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pw2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPicture, QFont, QColor
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
import DataModel
import PostMaker
import pickle

class QStringList(object):
    pass


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        font = QtGui.QFont()
        font.setFamily("DL-DIVANI-N")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)

        
        try:
            self.data_model = pickle.load(open('./settings','rb'))
        except:
            self.data_model = DataModel.DataModel()

        self.parent = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(896, 610)
        Dialog.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 891, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Grid.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.Grid.setContentsMargins(10, 10, 10, 10)
        self.Grid.setHorizontalSpacing(6)
        self.Grid.setObjectName("Grid")
        self.check_date = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_date.setObjectName("check_date")
        self.Grid.addWidget(self.check_date, 15, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.Grid.addWidget(self.label_4, 5, 0, 1, 1)
        self.topic_y = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.topic_y.setMaximum(1000)
        self.topic_y.setObjectName("topic_y")
        self.Grid.addWidget(self.topic_y, 7, 2, 1, 1)
        self.refresh_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.refresh_btn.setStyleSheet("background-color: rgb(255, 182, 0);")
        self.refresh_btn.setObjectName("refresh_btn")
        self.Grid.addWidget(self.refresh_btn, 16, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.Grid.addWidget(self.label_3, 2, 0, 1, 1)
        self.font_size = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.font_size.setMaximum(300)

        self.font_size.setObjectName("font_size")
        self.Grid.addWidget(self.font_size, 9, 2, 1, 1)
        self.topic_x = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.topic_x.setMaximum(1000)

        self.topic_x.setObjectName("topic_x")
        self.Grid.addWidget(self.topic_x, 6, 2, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.save_btn.setStyleSheet("background-color: rgb(22, 58, 0);")
        self.save_btn.setObjectName("save_btn")
        self.Grid.addWidget(self.save_btn, 16, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.Grid.addWidget(self.label, 9, 1, 1, 1)
        self.topic_font_size = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.topic_font_size.setMaximum(300)
        self.topic_font_size.setObjectName("topic_font_size")
        self.Grid.addWidget(self.topic_font_size, 5, 2, 1, 1)
        self.topic = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.topic.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.topic.setObjectName("topic")
        self.Grid.addWidget(self.topic, 3, 0, 1, 3)
        self.check_tag = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_tag.setObjectName("check_tag")
        self.Grid.addWidget(self.check_tag, 15, 2, 1, 1)
        self.article_font = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.article_font.setStyleSheet("background-color: rgb(224, 121, 0);")
        self.article_font.setObjectName("article_font")
        self.Grid.addWidget(self.article_font, 10, 0, 1, 1)
        self.color_btn_tpic = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.color_btn_tpic.setObjectName("color_btn_tpic")
        self.Grid.addWidget(self.color_btn_tpic, 4, 0, 1, 1)
        self.topi_font = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.topi_font.setStyleSheet("background-color: rgb(224, 121, 0);")
        self.topi_font.setObjectName("topi_font")
        self.Grid.addWidget(self.topi_font, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.Grid.addWidget(self.label_5, 6, 0, 1, 1)
        self.bg_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bg_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.bg_btn.setStyleSheet("background-color: rgb(255, 182, 0);")
        self.bg_btn.setDefault(False)
        self.bg_btn.setFlat(False)
        self.bg_btn.setObjectName("bg_btn")
        self.Grid.addWidget(self.bg_btn, 11, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.Grid.addWidget(self.label_2, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.Grid.addWidget(self.label_6, 12, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.Grid.addWidget(self.label_7, 14, 1, 1, 1)
        self.color_btn_author = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.color_btn_author.setObjectName("color_btn_author")
        self.Grid.addWidget(self.color_btn_author, 14, 0, 1, 1)
        self.author_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.author_name.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.author_name.setObjectName("author_name")
        self.Grid.addWidget(self.author_name, 13, 0, 1, 3)
        self.author_size = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.author_size.setMaximum(300)
        self.author_size.setObjectName("author_size")
        self.Grid.addWidget(self.author_size, 14, 2, 1, 1)
        self.font_y = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.font_y.setMaximum(1000)

        self.font_y.setObjectName("font_y")
        self.Grid.addWidget(self.font_y, 11, 2, 1, 1)
        self.color_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.color_btn.setObjectName("color_btn")
        self.Grid.addWidget(self.color_btn, 9, 0, 1, 1)
        self.font_x = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.font_x.setMaximum(1000)
        self.font_x.setObjectName("font_x")
        self.Grid.addWidget(self.font_x, 10, 2, 1, 1)
        self.article_text = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.article_text.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.article_text.setObjectName("article_text")

        self.Grid.addWidget(self.article_text, 8, 0, 1, 3)
        self.title_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.title_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.title_btn.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.title_btn.setObjectName("title_btn")
        self.Grid.addWidget(self.title_btn, 0, 0, 2, 3)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(300, 0))
        self.label_8.setObjectName("label_8")
        self.article_text.setFont(font)
        self.author_name.setFont(font)
        self.topic.setFont(font)

        self.Grid.addWidget(self.label_8, 0, 3, 25, 1)

        self.retranslateUi(Dialog)
        self.refresh_btn.clicked.connect(self.refresh)
        self.title_btn.clicked.connect(self.change_gui_to_model)
        self.topi_font.clicked.connect(self.change_topic_font)
        self.article_font.clicked.connect(self.change_article_font)

        self.topic.textChanged.connect(self.change_gui_to_model)
        self.author_name.textChanged.connect(self.change_gui_to_model)
        self.article_text.textChanged.connect(self.change_gui_to_model)

        self.topic_x.valueChanged.connect(self.change_gui_to_model)
        self.topic_y.valueChanged.connect(self.change_gui_to_model)
        self.font_x.valueChanged.connect(self.change_gui_to_model)
        self.font_y.valueChanged.connect(self.change_gui_to_model)
        self.font_size.valueChanged.connect(self.change_gui_to_model)
        self.topic_font_size.valueChanged.connect(self.change_gui_to_model)
        self.author_size.valueChanged.connect(self.change_gui_to_model)

        self.color_btn.clicked.connect(self.set_article_color)
        self.color_btn_author.clicked.connect(self.set_author_color)
        self.color_btn_tpic.clicked.connect(self.set_topic_color)
        self.bg_btn.clicked.connect(self.bg_chooser)
        self.save_btn.clicked.connect(self.save_chooser)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Vibhawa Post  Genarator - USE ONLY FOR VIBHAWA SOCIAL FB PAGE 1.0v"))
        self.check_date.setText(_translate("Dialog", "Date"))
        self.label_4.setText(_translate("Dialog", "Font size"))
        self.refresh_btn.setText(_translate("Dialog", "Refresh"))
        self.label_3.setText(_translate("Dialog", "Title "))
        self.save_btn.setText(_translate("Dialog", "Save As"))
        self.label.setText(_translate("Dialog", "Font size"))
        self.check_tag.setText(_translate("Dialog", "Tag Line"))
        self.article_font.setText(_translate("Dialog", "Font"))
        self.color_btn_tpic.setText(_translate("Dialog", "Colour"))
        self.topi_font.setText(_translate("Dialog", "Font"))
        self.label_5.setText(_translate("Dialog", "Position ( x | y )"))
        self.bg_btn.setText(_translate("Dialog", "Background"))
        self.label_2.setText(_translate("Dialog", "Position ( x | y )"))
        self.label_6.setText(_translate("Dialog", "Author"))
        self.label_7.setText(_translate("Dialog", "Font size"))
        self.color_btn_author.setText(_translate("Dialog", "Colour"))
        self.color_btn.setText(_translate("Dialog", "Colour"))
        self.title_btn.setText(_translate("Dialog", "Post"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))

        self.topic_x.setValue(self.data_model.title_loc[0])
        self.topic_y.setValue(self.data_model.title_loc[1])

        self.font_x.setValue(self.data_model.article_loc[0])
        self.font_y.setValue(self.data_model.article_loc[1])

        self.article_text.setPlainText(self.data_model.article)

        self.topic.setText(self.data_model.title)
        self.author_name.setText(self.data_model.author)
        self.font_size.setValue(self.data_model.article_size)
        self.topic_font_size.setValue(self.data_model.title_size)
        self.author_size.setValue(self.data_model.author_size)

        self.pix = QPixmap('./low.jpg')

        self.label_8.setPixmap(self.pix)
        self.refresh()

    def refresh(self):

        try:
            PostMaker.makePost(self.data_model.image_path, article=self.data_model.title,
                            font_path=self.data_model.title_font,
                            font_size=self.data_model.title_size, location=self.data_model.title_loc,
                            color=self.data_model.title_color)
        except:
            print ("ERRO: Post Making title")
        try:
            PostMaker.makePost("./tmp.bmp", article=self.data_model.article, font_path=self.data_model.article_font,
                            font_size=self.data_model.article_size, location=self.data_model.article_loc,
                            color=self.data_model.article_color)
        except:
            print ("ERRO: article")
        try:
            PostMaker.add_tag(author=self.data_model.author, font_size=self.data_model.author_size,
                            color=self.data_model.author_color,font=self.data_model.article_font)

        except:
            print ("ERRO: author or tag")
        try:
            self.pix = QPixmap('./low.bmp')
            self.label_8.setPixmap(self.pix)
            # print(self.data_model.article)
        except:
           print ("erro:loading")

        pickle.dump(self.data_model, open('./settings', 'wb'))

    def font_chooser(self):
        # print("font_cooser")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.parent, "QFileDialog.getOpenFileName()", "",
                                                  "Font Files (*.TTF);;Any Files (*.*)", options=options)
        return fileName

    def bg_chooser(self):
        # print("font_cooser")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.parent, "Choos Font", "",
                                                  "Any Files (*.*);; PNG Files (*.png);;JPG Files(*.jpg)", options=options)
        if fileName !="":
            self.data_model.image_path = fileName
            self.change_gui_to_model()

    def save_chooser(self):
        # print("font_cooser")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.parent, "Save as Image", "",
                                                  "Any Files (*.*);; PNG Files (*.png);;JPG Files(*.jpg)", options=options)
        if fileName !="":
            PostMaker.save(fileName)
            self.change_gui_to_model()

    def set_article_color(self):
        self.data_model.article_color = self.open_color_picker()
        self.change_gui_to_model()

    def set_topic_color(self):
        self.data_model.title_color = self.open_color_picker()
        self.change_gui_to_model()

    def set_author_color(self):
        self.data_model.author_color = self.open_color_picker()
        self.change_gui_to_model()

    def open_color_picker(self):
        val = QColorDialog.getColor()
        return (val.getRgb()[:-1])

    def change_topic_font(self):
        font = self.font_chooser()
        if font != '':
            self.data_model.title_font = font
            # print('Topic Font:', font)
        self.change_gui_to_model()

    def change_article_font(self):
        font = self.font_chooser()
        if font != '':
            self.data_model.article_font = font
            # print('Topic Font:', font)
            self.change_gui_to_model()

    def change_gui_to_model(self):
        self.data_model.title_loc = (self.topic_x.value(), self.topic_y.value())
        self.data_model.article_loc = (self.font_x.value(), self.font_y.value())

        self.data_model.article = self.article_text.toPlainText()
        self.data_model.title = self.topic.text()
        self.data_model.author = self.author_name.text()
        self.data_model.article_size = self.font_size.value()
        self.data_model.title_size = self.topic_font_size.value()
        self.data_model.author_size = self.author_size.value()

        self.refresh()

        # print(self.data_model.article)

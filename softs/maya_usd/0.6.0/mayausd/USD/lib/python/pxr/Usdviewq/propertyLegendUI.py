# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/jenkins/workspace/ecg-usd-full-windows/ecg-usd-build/usd/pxr/usdImaging/usdviewq/propertyLegendUI.ui',
# licensing of 'S:/jenkins/workspace/ecg-usd-full-windows/ecg-usd-build/usd/pxr/usdImaging/usdviewq/propertyLegendUI.ui' applies.
#
# Created: Fri Oct 30 15:43:01 2020
#      by: pyside2-uic  running on PySide2 5.14.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PropertyLegend(object):
    def setupUi(self, PropertyLegend):
        PropertyLegend.setObjectName("PropertyLegend")
        PropertyLegend.setWindowModality(QtCore.Qt.NonModal)
        PropertyLegend.resize(654, 151)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PropertyLegend.sizePolicy().hasHeightForWidth())
        PropertyLegend.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(PropertyLegend)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.propertyLegendColorNoValue = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorNoValue.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorNoValue.setObjectName("propertyLegendColorNoValue")
        self.horizontalLayout.addWidget(self.propertyLegendColorNoValue)
        self.propertyLegendLabelNoValue = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendLabelNoValue.setFont(font)
        self.propertyLegendLabelNoValue.setObjectName("propertyLegendLabelNoValue")
        self.horizontalLayout.addWidget(self.propertyLegendLabelNoValue)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.propertyLegendColorDefault = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorDefault.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorDefault.setObjectName("propertyLegendColorDefault")
        self.horizontalLayout_2.addWidget(self.propertyLegendColorDefault)
        self.propertyLegendLabelDefault = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendLabelDefault.setFont(font)
        self.propertyLegendLabelDefault.setObjectName("propertyLegendLabelDefault")
        self.horizontalLayout_2.addWidget(self.propertyLegendLabelDefault)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.propertyLegendColorTimeSample = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorTimeSample.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorTimeSample.setObjectName("propertyLegendColorTimeSample")
        self.horizontalLayout_5.addWidget(self.propertyLegendColorTimeSample)
        self.propertyLegendLabelTimeSample = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendLabelTimeSample.setFont(font)
        self.propertyLegendLabelTimeSample.setObjectName("propertyLegendLabelTimeSample")
        self.horizontalLayout_5.addWidget(self.propertyLegendLabelTimeSample)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.propertyLegendColorFallback = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorFallback.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorFallback.setObjectName("propertyLegendColorFallback")
        self.horizontalLayout_3.addWidget(self.propertyLegendColorFallback)
        self.propertyLegendLabelFallback = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendLabelFallback.setFont(font)
        self.propertyLegendLabelFallback.setObjectName("propertyLegendLabelFallback")
        self.horizontalLayout_3.addWidget(self.propertyLegendLabelFallback)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.propertyLegendColorCustom = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorCustom.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorCustom.setObjectName("propertyLegendColorCustom")
        self.horizontalLayout_4.addWidget(self.propertyLegendColorCustom)
        self.propertyLegendLabelCustom = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendLabelCustom.setObjectName("propertyLegendLabelCustom")
        self.horizontalLayout_4.addWidget(self.propertyLegendLabelCustom)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.propertyLegendColorValueClips = QtWidgets.QGraphicsView(PropertyLegend)
        self.propertyLegendColorValueClips.setMaximumSize(QtCore.QSize(20, 15))
        self.propertyLegendColorValueClips.setObjectName("propertyLegendColorValueClips")
        self.horizontalLayout_6.addWidget(self.propertyLegendColorValueClips)
        self.propertyLegendLabelValueClips = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendLabelValueClips.setFont(font)
        self.propertyLegendLabelValueClips.setObjectName("propertyLegendLabelValueClips")
        self.horizontalLayout_6.addWidget(self.propertyLegendLabelValueClips)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.propertyLegendAttrPlainIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendAttrPlainIcon.setObjectName("propertyLegendAttrPlainIcon")
        self.horizontalLayout_9.addWidget(self.propertyLegendAttrPlainIcon)
        self.propertyLegendAttrPlainDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendAttrPlainDesc.setFont(font)
        self.propertyLegendAttrPlainDesc.setObjectName("propertyLegendAttrPlainDesc")
        self.horizontalLayout_9.addWidget(self.propertyLegendAttrPlainDesc)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.propertyLegendRelPlainIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendRelPlainIcon.setObjectName("propertyLegendRelPlainIcon")
        self.horizontalLayout_10.addWidget(self.propertyLegendRelPlainIcon)
        self.propertyLegendRelPlainDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendRelPlainDesc.setFont(font)
        self.propertyLegendRelPlainDesc.setObjectName("propertyLegendRelPlainDesc")
        self.horizontalLayout_10.addWidget(self.propertyLegendRelPlainDesc)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.propertyLegendCompIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendCompIcon.setObjectName("propertyLegendCompIcon")
        self.horizontalLayout_11.addWidget(self.propertyLegendCompIcon)
        self.propertyLegendCompDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendCompDesc.setFont(font)
        self.propertyLegendCompDesc.setObjectName("propertyLegendCompDesc")
        self.horizontalLayout_11.addWidget(self.propertyLegendCompDesc)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.propertyLegendConnIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendConnIcon.setObjectName("propertyLegendConnIcon")
        self.horizontalLayout_12.addWidget(self.propertyLegendConnIcon)
        self.propertyLegendConnDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendConnDesc.setFont(font)
        self.propertyLegendConnDesc.setObjectName("propertyLegendConnDesc")
        self.horizontalLayout_12.addWidget(self.propertyLegendConnDesc)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.propertyLegendTargetIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendTargetIcon.setObjectName("propertyLegendTargetIcon")
        self.horizontalLayout_13.addWidget(self.propertyLegendTargetIcon)
        self.propertyLegendTargetDesc = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendTargetDesc.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendTargetDesc.setFont(font)
        self.propertyLegendTargetDesc.setObjectName("propertyLegendTargetDesc")
        self.horizontalLayout_13.addWidget(self.propertyLegendTargetDesc)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.inheritedPropertyIcon = QtWidgets.QLabel(PropertyLegend)
        self.inheritedPropertyIcon.setTextFormat(QtCore.Qt.RichText)
        self.inheritedPropertyIcon.setObjectName("inheritedPropertyIcon")
        self.horizontalLayout_14.addWidget(self.inheritedPropertyIcon)
        self.inheritedPropertyText = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setItalic(False)
        self.inheritedPropertyText.setFont(font)
        self.inheritedPropertyText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inheritedPropertyText.setTextFormat(QtCore.Qt.RichText)
        self.inheritedPropertyText.setAlignment(QtCore.Qt.AlignCenter)
        self.inheritedPropertyText.setWordWrap(False)
        self.inheritedPropertyText.setObjectName("inheritedPropertyText")
        self.horizontalLayout_14.addWidget(self.inheritedPropertyText)
        spacerItem11 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.propertyLegendAttrWithConnIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendAttrWithConnIcon.setObjectName("propertyLegendAttrWithConnIcon")
        self.horizontalLayout_8.addWidget(self.propertyLegendAttrWithConnIcon)
        self.propertyLegendAttrWithConnDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendAttrWithConnDesc.setFont(font)
        self.propertyLegendAttrWithConnDesc.setObjectName("propertyLegendAttrWithConnDesc")
        self.horizontalLayout_8.addWidget(self.propertyLegendAttrWithConnDesc)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.propertyLegendRelWithTargetIcon = QtWidgets.QLabel(PropertyLegend)
        self.propertyLegendRelWithTargetIcon.setObjectName("propertyLegendRelWithTargetIcon")
        self.horizontalLayout_7.addWidget(self.propertyLegendRelWithTargetIcon)
        self.propertyLegendRelWithTargetDesc = QtWidgets.QLabel(PropertyLegend)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.propertyLegendRelWithTargetDesc.setFont(font)
        self.propertyLegendRelWithTargetDesc.setObjectName("propertyLegendRelWithTargetDesc")
        self.horizontalLayout_7.addWidget(self.propertyLegendRelWithTargetDesc)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem14)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.retranslateUi(PropertyLegend)
        QtCore.QMetaObject.connectSlotsByName(PropertyLegend)

    def retranslateUi(self, PropertyLegend):
        PropertyLegend.setProperty("comment", QtWidgets.QApplication.translate("PropertyLegend", "\n"
"     Copyright 2017 Pixar                                                                   \n"
"                                                                                            \n"
"     Licensed under the Apache License, Version 2.0 (the \"Apache License\")      \n"
"     with the following modification; you may not use this file except in                   \n"
"     compliance with the Apache License and the following modification to it:               \n"
"     Section 6. Trademarks. is deleted and replaced with:                                   \n"
"                                                                                            \n"
"     6. Trademarks. This License does not grant permission to use the trade                 \n"
"        names, trademarks, service marks, or product names of the Licensor                  \n"
"        and its affiliates, except as required to comply with Section 4(c) of               \n"
"        the License and to reproduce the content of the NOTICE file.                        \n"
"                                                                                            \n"
"     You may obtain a copy of the Apache License at                                         \n"
"                                                                                            \n"
"         http://www.apache.org/licenses/LICENSE-2.0                                         \n"
"                                                                                            \n"
"     Unless required by applicable law or agreed to in writing, software                    \n"
"     distributed under the Apache License with the above modification is                    \n"
"     distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY   \n"
"     KIND, either express or implied. See the Apache License for the specific               \n"
"     language governing permissions and limitations under the Apache License.               \n"
"  ", None, -1))
        self.propertyLegendLabelNoValue.setText(QtWidgets.QApplication.translate("PropertyLegend", "No Value", None, -1))
        self.propertyLegendLabelDefault.setText(QtWidgets.QApplication.translate("PropertyLegend", "Default", None, -1))
        self.propertyLegendLabelTimeSample.setText(QtWidgets.QApplication.translate("PropertyLegend", "Time Samples (Interpolated) ", None, -1))
        self.propertyLegendLabelFallback.setText(QtWidgets.QApplication.translate("PropertyLegend", "Fallback", None, -1))
        self.propertyLegendLabelCustom.setText(QtWidgets.QApplication.translate("PropertyLegend", "Custom", None, -1))
        self.propertyLegendLabelValueClips.setText(QtWidgets.QApplication.translate("PropertyLegend", "Value Clips (Interpolated)", None, -1))
        self.propertyLegendAttrPlainDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Attribute", None, -1))
        self.propertyLegendRelPlainDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Relationship", None, -1))
        self.propertyLegendCompDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Computed Value", None, -1))
        self.propertyLegendConnDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Connection", None, -1))
        self.propertyLegendTargetDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Target", None, -1))
        self.inheritedPropertyIcon.setText(QtWidgets.QApplication.translate("PropertyLegend", "<small><i>(i)</i></small>", None, -1))
        self.inheritedPropertyText.setText(QtWidgets.QApplication.translate("PropertyLegend", "Inherited Property", None, -1))
        self.propertyLegendAttrWithConnDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Attribute w/Connection(s)", None, -1))
        self.propertyLegendRelWithTargetDesc.setText(QtWidgets.QApplication.translate("PropertyLegend", "Relationship w/Target(s)", None, -1))


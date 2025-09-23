# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'KCC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QWidget)
from . import KCC_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(566, 573)
        icon = QIcon()
        icon.addFile(u":/Icon/icons/comic2ebook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 5)
        self.jobList = QListWidget(self.centralWidget)
        self.jobList.setObjectName(u"jobList")
        self.jobList.setMinimumSize(QSize(0, 150))
        self.jobList.setStyleSheet(u"")
        self.jobList.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.jobList.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.jobList.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.gridLayout.addWidget(self.jobList, 2, 0, 1, 2)

        self.toolWidget = QWidget(self.centralWidget)
        self.toolWidget.setObjectName(u"toolWidget")
        self.horizontalLayout = QHBoxLayout(self.toolWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.editorButton = QPushButton(self.toolWidget)
        self.editorButton.setObjectName(u"editorButton")
        self.editorButton.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/Other/icons/editor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editorButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.editorButton)

        self.wikiButton = QPushButton(self.toolWidget)
        self.wikiButton.setObjectName(u"wikiButton")
        self.wikiButton.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/Other/icons/wiki.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wikiButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.wikiButton)


        self.gridLayout.addWidget(self.toolWidget, 0, 0, 1, 2)

        self.buttonWidget = QWidget(self.centralWidget)
        self.buttonWidget.setObjectName(u"buttonWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonWidget.sizePolicy().hasHeightForWidth())
        self.buttonWidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.buttonWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.convertButton = QPushButton(self.buttonWidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.convertButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/Other/icons/convert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.convertButton.setIcon(icon3)

        self.gridLayout_4.addWidget(self.convertButton, 1, 3, 1, 1)

        self.clearButton = QPushButton(self.buttonWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/Other/icons/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearButton.setIcon(icon4)

        self.gridLayout_4.addWidget(self.clearButton, 0, 3, 1, 1)

        self.deviceBox = QComboBox(self.buttonWidget)
        self.deviceBox.setObjectName(u"deviceBox")
        self.deviceBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.deviceBox, 1, 1, 1, 1)

        self.fileButton = QPushButton(self.buttonWidget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/Other/icons/document_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fileButton.setIcon(icon5)

        self.gridLayout_4.addWidget(self.fileButton, 0, 1, 1, 1)

        self.defaultOutputFolderButton = QPushButton(self.buttonWidget)
        self.defaultOutputFolderButton.setObjectName(u"defaultOutputFolderButton")
        self.defaultOutputFolderButton.setMinimumSize(QSize(0, 30))
        icon6 = QIcon()
        icon6.addFile(u":/Other/icons/folder_new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.defaultOutputFolderButton.setIcon(icon6)

        self.gridLayout_4.addWidget(self.defaultOutputFolderButton, 0, 5, 1, 1)

        self.defaultOutputFolderBox = QCheckBox(self.buttonWidget)
        self.defaultOutputFolderBox.setObjectName(u"defaultOutputFolderBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.defaultOutputFolderBox.sizePolicy().hasHeightForWidth())
        self.defaultOutputFolderBox.setSizePolicy(sizePolicy1)
        self.defaultOutputFolderBox.setTristate(True)

        self.gridLayout_4.addWidget(self.defaultOutputFolderBox, 0, 4, 1, 1)

        self.formatBox = QComboBox(self.buttonWidget)
        self.formatBox.setObjectName(u"formatBox")
        self.formatBox.setMinimumSize(QSize(0, 28))

        self.gridLayout_4.addWidget(self.formatBox, 1, 4, 1, 2)

        self.clearButton.raise_()
        self.deviceBox.raise_()
        self.convertButton.raise_()
        self.formatBox.raise_()
        self.defaultOutputFolderButton.raise_()
        self.fileButton.raise_()
        self.defaultOutputFolderBox.raise_()

        self.gridLayout.addWidget(self.buttonWidget, 3, 0, 1, 2)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setFont(font)
        self.progressBar.setVisible(False)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)

        self.customWidget = QWidget(self.centralWidget)
        self.customWidget.setObjectName(u"customWidget")
        self.customWidget.setVisible(False)
        self.gridLayout_3 = QGridLayout(self.customWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hLabel = QLabel(self.customWidget)
        self.hLabel.setObjectName(u"hLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hLabel.sizePolicy().hasHeightForWidth())
        self.hLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.hLabel, 0, 2, 1, 1)

        self.widthBox = QSpinBox(self.customWidget)
        self.widthBox.setObjectName(u"widthBox")
        self.widthBox.setMaximum(2400)

        self.gridLayout_3.addWidget(self.widthBox, 0, 1, 1, 1)

        self.wLabel = QLabel(self.customWidget)
        self.wLabel.setObjectName(u"wLabel")
        sizePolicy2.setHeightForWidth(self.wLabel.sizePolicy().hasHeightForWidth())
        self.wLabel.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.wLabel, 0, 0, 1, 1)

        self.heightBox = QSpinBox(self.customWidget)
        self.heightBox.setObjectName(u"heightBox")
        self.heightBox.setMaximum(3840)

        self.gridLayout_3.addWidget(self.heightBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.customWidget, 8, 0, 1, 2)

        self.croppingWidget = QWidget(self.centralWidget)
        self.croppingWidget.setObjectName(u"croppingWidget")
        self.croppingWidget.setVisible(False)
        self.gridLayout_5 = QGridLayout(self.croppingWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.preserveMarginLabel = QLabel(self.croppingWidget)
        self.preserveMarginLabel.setObjectName(u"preserveMarginLabel")

        self.gridLayout_5.addWidget(self.preserveMarginLabel, 1, 0, 1, 1)

        self.croppingPowerLabel = QLabel(self.croppingWidget)
        self.croppingPowerLabel.setObjectName(u"croppingPowerLabel")

        self.gridLayout_5.addWidget(self.croppingPowerLabel, 0, 0, 1, 1)

        self.croppingPowerSlider = QSlider(self.croppingWidget)
        self.croppingPowerSlider.setObjectName(u"croppingPowerSlider")
        self.croppingPowerSlider.setMaximum(300)
        self.croppingPowerSlider.setSingleStep(1)
        self.croppingPowerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.croppingPowerSlider, 0, 1, 1, 1)

        self.preserveMarginBox = QSpinBox(self.croppingWidget)
        self.preserveMarginBox.setObjectName(u"preserveMarginBox")
        sizePolicy1.setHeightForWidth(self.preserveMarginBox.sizePolicy().hasHeightForWidth())
        self.preserveMarginBox.setSizePolicy(sizePolicy1)
        self.preserveMarginBox.setMaximum(99)
        self.preserveMarginBox.setSingleStep(5)
        self.preserveMarginBox.setValue(0)

        self.gridLayout_5.addWidget(self.preserveMarginBox, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.croppingWidget, 9, 0, 1, 2)

        self.optionWidget = QWidget(self.centralWidget)
        self.optionWidget.setObjectName(u"optionWidget")
        self.gridLayout_2 = QGridLayout(self.optionWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gammaBox = QCheckBox(self.optionWidget)
        self.gammaBox.setObjectName(u"gammaBox")

        self.gridLayout_2.addWidget(self.gammaBox, 2, 2, 1, 1)

        self.mangaBox = QCheckBox(self.optionWidget)
        self.mangaBox.setObjectName(u"mangaBox")

        self.gridLayout_2.addWidget(self.mangaBox, 1, 0, 1, 1)

        self.borderBox = QCheckBox(self.optionWidget)
        self.borderBox.setObjectName(u"borderBox")
        self.borderBox.setTristate(True)

        self.gridLayout_2.addWidget(self.borderBox, 3, 0, 1, 1)

        self.interPanelCropBox = QCheckBox(self.optionWidget)
        self.interPanelCropBox.setObjectName(u"interPanelCropBox")
        self.interPanelCropBox.setTristate(True)

        self.gridLayout_2.addWidget(self.interPanelCropBox, 6, 2, 1, 1)

        self.fileFusionBox = QCheckBox(self.optionWidget)
        self.fileFusionBox.setObjectName(u"fileFusionBox")

        self.gridLayout_2.addWidget(self.fileFusionBox, 6, 0, 1, 1)

        self.authorEdit = QLineEdit(self.optionWidget)
        self.authorEdit.setObjectName(u"authorEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.authorEdit.sizePolicy().hasHeightForWidth())
        self.authorEdit.setSizePolicy(sizePolicy3)
        self.authorEdit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.authorEdit.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.authorEdit, 0, 0, 1, 1)

        self.rotateFirstBox = QCheckBox(self.optionWidget)
        self.rotateFirstBox.setObjectName(u"rotateFirstBox")

        self.gridLayout_2.addWidget(self.rotateFirstBox, 8, 1, 1, 1)

        self.eraseRainbowBox = QCheckBox(self.optionWidget)
        self.eraseRainbowBox.setObjectName(u"eraseRainbowBox")

        self.gridLayout_2.addWidget(self.eraseRainbowBox, 7, 2, 1, 1)

        self.chunkSizeCheckBox = QCheckBox(self.optionWidget)
        self.chunkSizeCheckBox.setObjectName(u"chunkSizeCheckBox")

        self.gridLayout_2.addWidget(self.chunkSizeCheckBox, 7, 1, 1, 1)

        self.rotateBox = QCheckBox(self.optionWidget)
        self.rotateBox.setObjectName(u"rotateBox")
        self.rotateBox.setTristate(True)

        self.gridLayout_2.addWidget(self.rotateBox, 1, 1, 1, 1)

        self.outputSplit = QCheckBox(self.optionWidget)
        self.outputSplit.setObjectName(u"outputSplit")

        self.gridLayout_2.addWidget(self.outputSplit, 3, 1, 1, 1)

        self.metadataTitleBox = QCheckBox(self.optionWidget)
        self.metadataTitleBox.setObjectName(u"metadataTitleBox")

        self.gridLayout_2.addWidget(self.metadataTitleBox, 7, 0, 1, 1)

        self.qualityBox = QCheckBox(self.optionWidget)
        self.qualityBox.setObjectName(u"qualityBox")
        self.qualityBox.setTristate(True)

        self.gridLayout_2.addWidget(self.qualityBox, 1, 2, 1, 1)

        self.spreadShiftBox = QCheckBox(self.optionWidget)
        self.spreadShiftBox.setObjectName(u"spreadShiftBox")

        self.gridLayout_2.addWidget(self.spreadShiftBox, 5, 0, 1, 1)

        self.disableProcessingBox = QCheckBox(self.optionWidget)
        self.disableProcessingBox.setObjectName(u"disableProcessingBox")

        self.gridLayout_2.addWidget(self.disableProcessingBox, 5, 2, 1, 1)

        self.webtoonBox = QCheckBox(self.optionWidget)
        self.webtoonBox.setObjectName(u"webtoonBox")

        self.gridLayout_2.addWidget(self.webtoonBox, 2, 0, 1, 1)

        self.colorBox = QCheckBox(self.optionWidget)
        self.colorBox.setObjectName(u"colorBox")

        self.gridLayout_2.addWidget(self.colorBox, 3, 2, 1, 1)

        self.croppingBox = QCheckBox(self.optionWidget)
        self.croppingBox.setObjectName(u"croppingBox")
        self.croppingBox.setTristate(True)

        self.gridLayout_2.addWidget(self.croppingBox, 4, 2, 1, 1)

        self.maximizeStrips = QCheckBox(self.optionWidget)
        self.maximizeStrips.setObjectName(u"maximizeStrips")

        self.gridLayout_2.addWidget(self.maximizeStrips, 4, 1, 1, 1)

        self.noRotateBox = QCheckBox(self.optionWidget)
        self.noRotateBox.setObjectName(u"noRotateBox")

        self.gridLayout_2.addWidget(self.noRotateBox, 6, 1, 1, 1)

        self.deleteBox = QCheckBox(self.optionWidget)
        self.deleteBox.setObjectName(u"deleteBox")

        self.gridLayout_2.addWidget(self.deleteBox, 5, 1, 1, 1)

        self.upscaleBox = QCheckBox(self.optionWidget)
        self.upscaleBox.setObjectName(u"upscaleBox")
        self.upscaleBox.setTristate(True)

        self.gridLayout_2.addWidget(self.upscaleBox, 2, 1, 1, 1)

        self.mozJpegBox = QCheckBox(self.optionWidget)
        self.mozJpegBox.setObjectName(u"mozJpegBox")
        self.mozJpegBox.setTristate(True)

        self.gridLayout_2.addWidget(self.mozJpegBox, 4, 0, 1, 1)

        self.autoLevelBox = QCheckBox(self.optionWidget)
        self.autoLevelBox.setObjectName(u"autoLevelBox")

        self.gridLayout_2.addWidget(self.autoLevelBox, 8, 2, 1, 1)


        self.gridLayout.addWidget(self.optionWidget, 5, 0, 1, 2)

        self.gammaWidget = QWidget(self.centralWidget)
        self.gammaWidget.setObjectName(u"gammaWidget")
        self.gammaWidget.setVisible(False)
        self.horizontalLayout_2 = QHBoxLayout(self.gammaWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gammaLabel = QLabel(self.gammaWidget)
        self.gammaLabel.setObjectName(u"gammaLabel")

        self.horizontalLayout_2.addWidget(self.gammaLabel)

        self.gammaSlider = QSlider(self.gammaWidget)
        self.gammaSlider.setObjectName(u"gammaSlider")
        self.gammaSlider.setMaximum(250)
        self.gammaSlider.setSingleStep(5)
        self.gammaSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.gammaSlider)


        self.gridLayout.addWidget(self.gammaWidget, 7, 0, 1, 2)

        self.chunkSizeWidget = QWidget(self.centralWidget)
        self.chunkSizeWidget.setObjectName(u"chunkSizeWidget")
        sizePolicy3.setHeightForWidth(self.chunkSizeWidget.sizePolicy().hasHeightForWidth())
        self.chunkSizeWidget.setSizePolicy(sizePolicy3)
        self.chunkSizeWidget.setVisible(False)
        self.horizontalLayout_4 = QHBoxLayout(self.chunkSizeWidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.chunkSizeLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeLabel.setObjectName(u"chunkSizeLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.chunkSizeLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.chunkSizeLabel)

        self.chunkSizeBox = QSpinBox(self.chunkSizeWidget)
        self.chunkSizeBox.setObjectName(u"chunkSizeBox")
        self.chunkSizeBox.setMinimum(100)
        self.chunkSizeBox.setMaximum(600)
        self.chunkSizeBox.setValue(400)

        self.horizontalLayout_4.addWidget(self.chunkSizeBox)

        self.chunkSizeWarnLabel = QLabel(self.chunkSizeWidget)
        self.chunkSizeWarnLabel.setObjectName(u"chunkSizeWarnLabel")
        sizePolicy4.setHeightForWidth(self.chunkSizeWarnLabel.sizePolicy().hasHeightForWidth())
        self.chunkSizeWarnLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.chunkSizeWarnLabel)


        self.gridLayout.addWidget(self.chunkSizeWidget, 6, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(mainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setSizeGripEnabled(False)
        mainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.convertButton, self.clearButton)
        QWidget.setTabOrder(self.clearButton, self.deviceBox)
        QWidget.setTabOrder(self.deviceBox, self.formatBox)
        QWidget.setTabOrder(self.formatBox, self.mangaBox)
        QWidget.setTabOrder(self.mangaBox, self.rotateBox)
        QWidget.setTabOrder(self.rotateBox, self.qualityBox)
        QWidget.setTabOrder(self.qualityBox, self.webtoonBox)
        QWidget.setTabOrder(self.webtoonBox, self.upscaleBox)
        QWidget.setTabOrder(self.upscaleBox, self.gammaBox)
        QWidget.setTabOrder(self.gammaBox, self.borderBox)
        QWidget.setTabOrder(self.borderBox, self.outputSplit)
        QWidget.setTabOrder(self.outputSplit, self.colorBox)
        QWidget.setTabOrder(self.colorBox, self.mozJpegBox)
        QWidget.setTabOrder(self.mozJpegBox, self.maximizeStrips)
        QWidget.setTabOrder(self.maximizeStrips, self.croppingBox)
        QWidget.setTabOrder(self.croppingBox, self.spreadShiftBox)
        QWidget.setTabOrder(self.spreadShiftBox, self.deleteBox)
        QWidget.setTabOrder(self.deleteBox, self.disableProcessingBox)
        QWidget.setTabOrder(self.disableProcessingBox, self.chunkSizeBox)
        QWidget.setTabOrder(self.chunkSizeBox, self.noRotateBox)
        QWidget.setTabOrder(self.noRotateBox, self.interPanelCropBox)
        QWidget.setTabOrder(self.interPanelCropBox, self.eraseRainbowBox)
        QWidget.setTabOrder(self.eraseRainbowBox, self.heightBox)
        QWidget.setTabOrder(self.heightBox, self.croppingPowerSlider)
        QWidget.setTabOrder(self.croppingPowerSlider, self.editorButton)
        QWidget.setTabOrder(self.editorButton, self.wikiButton)
        QWidget.setTabOrder(self.wikiButton, self.jobList)
        QWidget.setTabOrder(self.jobList, self.gammaSlider)
        QWidget.setTabOrder(self.gammaSlider, self.widthBox)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Kindle Comic Converter", None))
#if QT_CONFIG(tooltip)
        self.editorButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+Click to edit directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.editorButton.setText(QCoreApplication.translate("mainWindow", u"\u5143\u6570\u636e\u7f16\u8f91\u5668", None))
        self.wikiButton.setText(QCoreApplication.translate("mainWindow", u"Wiki", None))
#if QT_CONFIG(tooltip)
        self.convertButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Shift+\u5355\u51fb\u4ee5\u9009\u62e9\u6b64\u5217\u8868\u7684\u8f93\u51fa\u76ee\u5f55.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.convertButton.setText(QCoreApplication.translate("mainWindow", u"\u8f6c\u6362", None))
        self.clearButton.setText(QCoreApplication.translate("mainWindow", u"\u6e05\u7a7a", None))
#if QT_CONFIG(tooltip)
        self.deviceBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u76ee\u6807\u8bbe\u5907.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fileButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u6dfb\u52a0 CBR, CBZ, CB7 or PDF \u6587\u4ef6\u5230\u961f\u5217.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileButton.setText(QCoreApplication.translate("mainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u4f7f\u7528\u6b64\u64cd\u4f5c\u9009\u62e9\u9ed8\u8ba4\u8f93\u51fa\u76ee\u5f55.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderButton.setText("")
#if QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u8f93\u51fa\u5230\u539f\u59cb\u8def\u5f84<br /></span>\u8f93\u51fa\u5230\u539f\u59cb\u6587\u4ef6\u8def\u5f84</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u6e90\u65c1\u8fb9\u7684\u6587\u4ef6\u5939<br /></span>\u5c06\u8f93\u51fa\u6587\u4ef6\u653e\u5728\u6e90\u6587\u4ef6\u65c1\u8fb9\u7684\u6587\u4ef6\u5939\u4e2d</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u81ea\u5b9a\u4e49<br /></span>\u5c06\u8f93\u51fa\u6587\u4ef6\u653e\u5165\u7531\u53f3\u952e\u6307\u5b9a\u7684\u81ea\u5b9a\u4e49\u76ee\u5f55\u4e2d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.defaultOutputFolderBox.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u51fa\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.formatBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u8f93\u51fa\u683c\u5f0f.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.hLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolution of the target device.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.hLabel.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49\u9ad8\u5ea6:", None))
#if QT_CONFIG(tooltip)
        self.widthBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolution of the target device.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolution of the target device.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wLabel.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49\u5bbd\u5ea6:", None))
#if QT_CONFIG(tooltip)
        self.heightBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>Resolution of the target device.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.preserveMarginLabel.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>After calculating the cropping boundaries, &quot;back up&quot; a specified percentage amount.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.preserveMarginLabel.setText(QCoreApplication.translate("mainWindow", u"\u4fdd\u7559\u8fb9\u8ddd %", None))
        self.croppingPowerLabel.setText(QCoreApplication.translate("mainWindow", u"Cropping power:", None))
#if QT_CONFIG(tooltip)
        self.gammaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u7981\u7528\u81ea\u52a8\u4f3d\u9a6c\u6821\u6b63.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gammaBox.setText(QCoreApplication.translate("mainWindow", u"\u81ea\u5b9a\u4e49gamma", None))
#if QT_CONFIG(tooltip)
        self.mangaBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u542f\u7528\u4ece\u53f3\u5230\u5de6\u6a21\u5f0f.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mangaBox.setText(QCoreApplication.translate("mainWindow", u"\u4ece\u53f3\u5230\u5de6\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.borderBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u81ea\u52a8\u68c0\u6d4b<br /></span>\u5c06\u81ea\u52a8\u68c0\u6d4b\u8fb9\u8ddd\u586b\u5145\u7684\u989c\u8272.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u767d\u8272<br /></span>\u8fb9\u6846\u5c06\u7528\u767d\u8272\u586b\u5145.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u9ed1\u8272<br /></span>\u8fb9\u6846\u5c06\u7528\u9ed1\u8272\u586b\u5145.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.borderBox.setText(QCoreApplication.translate("mainWindow", u"W/B \u586b\u5145\u8fb9\u8ddd", None))
#if QT_CONFIG(tooltip)
        self.interPanelCropBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u7981\u7528<br /></span>\u7981\u7528</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u6a2a\u5411<br /></span>\u88c1\u5207\u7a7a\u767d\u6c34\u5e73\u884c.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u90fd\u88c1\u5207<br /></span>\u88c1\u5207\u7a7a\u767d\u6c34\u5e73\u548c\u7ad6\u76f4\u884c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.interPanelCropBox.setText(QCoreApplication.translate("mainWindow", u"\u9762\u677f\u95f4\u88c1\u526a", None))
#if QT_CONFIG(tooltip)
        self.fileFusionBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u5c06\u6240\u6709\u9009\u5b9a\u7684\u6587\u4ef6\u5408\u5e76\u4e3a\u4e00\u4e2a\u6587\u4ef6. (\u6709\u52a9\u4e8e\u5c06\u7ae0\u8282\u5408\u5e76\u4e3a\u5377.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileFusionBox.setText(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6\u878d\u5408", None))
#if QT_CONFIG(tooltip)
        self.authorEdit.setToolTip(QCoreApplication.translate("mainWindow", u"\u5728KCC\u4e2d\u7684\u9ed8\u8ba4\u4f5c\u8005", None))
#endif // QT_CONFIG(tooltip)
        self.authorEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u9ed8\u8ba4\u4f5c\u8005", None))
#if QT_CONFIG(tooltip)
        self.rotateFirstBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p>\u5f53\u90e8\u5206\u68c0\u67e5\u70b9\u62c6\u5206\u5668\u9009\u9879\u65f6,</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u65cb\u8f6c\u4e4b\u540e<br /></span>\u5c06\u65cb\u8f6c\u7684 2 \u9875\u8de8\u9875\u653e\u5728\u62c6\u5206\u8de8\u9875\u4e4b\u540e.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u65cb\u8f6c\u4e4b\u524d<br /></span>\u5c06\u65cb\u8f6c\u7684 2 \u9875\u8de8\u9875\u653e\u5728\u62c6\u5206\u8de8\u9875\u4e4b\u524d.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateFirstBox.setText(QCoreApplication.translate("mainWindow", u"\u65cb\u8f6c\u7b2c\u4e00\u4e2a", None))
#if QT_CONFIG(tooltip)
        self.eraseRainbowBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u901a\u8fc7\u7565\u5fae\u6a21\u7cca\u56fe\u50cf\u6765\u51cf\u5c11\u5f69\u8272eink\u4e0a\u7684\u5f69\u8679\u7eb9\u6548\u679c", None))
#endif // QT_CONFIG(tooltip)
        self.eraseRainbowBox.setText(QCoreApplication.translate("mainWindow", u"\u5f69\u8679\u7eb9\u6a21\u7cca\u4fee\u590d", None))
#if QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:700; text-decoration: underline;\">\u672a\u9009\u4e2d<br /></span>\u6761\u6f2b\u7684\u6700\u5927\u8f93\u51fa\u6587\u4ef6\u5927\u5c0f\u4e3a100MB\uff0c\u5176\u4ed6\u6587\u4ef6\u5927\u5c0f\u4e3a 400 MB\u3002</p><p><span style=\" font-weight:700; text-decoration: underline;\">\u9009\u4e2d</span><br />\u4f7f\u7528&quot;\u5757\u5c3a\u5bf8\u5927\u5c0fMB&quot; \u5206\u5272\u6587\u4ef6.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u5757\u5927\u5c0f", None))
#if QT_CONFIG(tooltip)
        self.rotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d-\u5206\u5272<br /></span>\u5c06\u8de8\u9875\u62fc\u63a5\u5207\u5272\u4e3a\u72ec\u7acb\u5355\u9875.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009\uff0d\u65cb\u8f6c\u5e76\u5206\u5272<br /></span>\u8de8\u9875\u56fe\u5c06\u663e\u793a\u4e24\u6b21\u3002\u9996\u5148\u8fdb\u884c\u65cb\u8f6c\uff0c\u7136\u540e\u8fdb\u884c\u5206\u5272. </p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d-\u65cb\u8f6c<br /></span>\u8de8\u9875\u5c06\u88ab\u65cb\u8f6c.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.rotateBox.setText(QCoreApplication.translate("mainWindow", u"\u667a\u80fd\u5206\u9875", None))
#if QT_CONFIG(tooltip)
        self.outputSplit.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u81ea\u52a8\u6a21\u5f0f<br /></span>\u8f93\u51fa\u5c06\u81ea\u52a8\u62c6\u5206.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u5377\u6a21\u5f0f<br /></span>\u6bcf\u4e2a\u5b50\u76ee\u5f55\u90fd\u5c06\u88ab\u89c6\u4e3a\u4e00\u4e2a\u5355\u72ec\u7684\u5377.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.outputSplit.setText(QCoreApplication.translate("mainWindow", u"\u62c6\u5206\u8f93\u51fa", None))
#if QT_CONFIG(tooltip)
        self.metadataTitleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>\u4eceComicInfo.xml\u6216\u5176\u4ed6\u5d4c\u5165\u5143\u6570\u636e\u5199\u5165\u6807\u9898.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.metadataTitleBox.setText(QCoreApplication.translate("mainWindow", u"\u5143\u6570\u636e\u6807\u9898", None))
#if QT_CONFIG(tooltip)
        self.qualityBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - 4\u9762\u677f<br /></span>\u5206\u522b\u7f29\u653e\u6bcf\u4e2a\u89d2\u843d.</p><p style='white-space:pre'><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - 2\u9762\u677f<br /></span>\u4ec5\u7f29\u653e\u9875\u9762\u7684\u9876\u90e8\u548c\u5e95\u90e8.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - 4\u9ad8\u8d28\u91cf\u9762\u677f<br /></span>\u5206\u522b\u653e\u5927\u6bcf\u4e2a\u89d2\u3002\u5c1d\u8bd5\u63d0\u9ad8\u653e\u5927\u8d28\u91cf\u3002\u66f4\u591a\u8be6\u60c5\u8bf7\u67e5\u770b\u7ef4\u57fa\u767e\u79d1\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.qualityBox.setText(QCoreApplication.translate("mainWindow", u"\u9762\u677f\u89c6\u56fe 4/2/HQ", None))
#if QT_CONFIG(tooltip)
        self.spreadShiftBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5c06\u7b2c\u4e00\u9875\u6a2a\u5411\u79fb\u81f3\u53e6\u4e00\u4fa7\uff0c\u4ee5\u5b9e\u73b0\u4e24\u9875\u9875\u7801\u5bf9\u9f50", None))
#endif // QT_CONFIG(tooltip)
        self.spreadShiftBox.setText(QCoreApplication.translate("mainWindow", u"\u9996\u9875\u504f\u79fb", None))
#if QT_CONFIG(tooltip)
        self.disableProcessingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u4e0d\u5904\u7406\u4efb\u4f55\u56fe\u50cf\uff0c\u5ffd\u7565\u914d\u7f6e\u6587\u4ef6\u548c\u5904\u7406\u9009\u9879.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.disableProcessingBox.setText(QCoreApplication.translate("mainWindow", u"\u7981\u7528\u5904\u7406", None))
#if QT_CONFIG(tooltip)
        self.webtoonBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u542f\u7528\u97e9\u56fd\u6761\u6f2b\u4f18\u5316\u6a21\u5f0f.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.webtoonBox.setText(QCoreApplication.translate("mainWindow", u"\u6761\u6f2b\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.colorBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p style='white-space:pre'>\u7981\u7528\u8f6c\u6362\u4e3a\u7070\u5ea6.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.colorBox.setText(QCoreApplication.translate("mainWindow", u"\u5f69\u8272\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.croppingBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - \u7981\u7528</span></p><p>\u7981\u7528</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u8fb9\u6846<br /></span>\u8fb9\u6846</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u8fb9\u6846+\u9875\u7801<br /></span>\u8fb9\u6846+\u9875\u7801</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.croppingBox.setText(QCoreApplication.translate("mainWindow", u"\u88c1\u526a\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.maximizeStrips.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - 1x4<br /></span>\u4fdd\u6301\u683c\u5f0f 1x4 panels strips.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - 2x2<br /></span>\u5c06 1x4 strips\u53d8\u4e3a 2x2\uff0c\u6700\u5927\u9650\u5ea6\u5730\u63d0\u9ad8\u5c4f\u5e55\u4f7f\u7528\u7387.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeStrips.setText(QCoreApplication.translate("mainWindow", u"1x4 to 2x2 strips", None))
#if QT_CONFIG(tooltip)
        self.noRotateBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u4e0d\u8981\u5728\u8de8\u9875\u62c6\u5206\u5668\u9009\u9879\u4e2d\u65cb\u8f6c\u53cc\u9875\u8de8\u9875.", None))
#endif // QT_CONFIG(tooltip)
        self.noRotateBox.setText(QCoreApplication.translate("mainWindow", u"\u4e0d\u8981\u65cb\u8f6c", None))
#if QT_CONFIG(tooltip)
        self.deleteBox.setToolTip(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u8f93\u5165\u6587\u4ef6\u6216\u76ee\u5f55\u3002\u65e0\u6cd5\u6062\u590d\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBox.setText(QCoreApplication.translate("mainWindow", u"\u5220\u9664\u8f93\u5165", None))
#if QT_CONFIG(tooltip)
        self.upscaleBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - Nothing<br /></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u4e0d\u4f1a\u8c03\u6574\u5927\u5c0f.</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u62c9\u4f38<br /></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u5c06\u88ab\u8c03\u6574\u5927\u5c0f\u3002\u5bbd\u9ad8\u6bd4\u5c06\u4e0d\u4f1a\u4fdd\u7559\u3002</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - \u7f29\u653e<br /></span>\u5c0f\u4e8e\u8bbe\u5907\u5206\u8fa8\u7387\u7684\u56fe\u50cf\u5c06\u88ab\u8c03\u6574\u5927\u5c0f\u3002\u7eb5\u6a2a\u6bd4\u5c06\u88ab\u4fdd\u7559\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.upscaleBox.setText(QCoreApplication.translate("mainWindow", u"\u62c9\u4f38/\u7f29\u653e", None))
#if QT_CONFIG(tooltip)
        self.mozJpegBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p><span style=\" font-weight:600; text-decoration: underline;\">\u672a\u9009\u4e2d - JPEG<br /></span>\u4f7f\u7528 JPEG \u6587\u4ef6</p><p><span style=\" font-weight:600; text-decoration: underline;\">\u534a\u9009 - \u5f3a\u5236 PNG<br /></span>\u521b\u5efa PNG \u6587\u4ef6\u800c\u4e0d\u662f JPEG </p><p><span style=\" font-weight:600; text-decoration: underline;\">\u9009\u4e2d - mozJpeg<br /></span>JPEG\u6587\u4ef6\u7f29\u5c0f10-20%\uff0c\u56fe\u50cf\u8d28\u91cf\u4e0d\u53d8\uff0c\u4f46\u5904\u7406\u65f6\u95f4\u589e\u52a02\u500d</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.mozJpegBox.setText(QCoreApplication.translate("mainWindow", u"JPEG/PNG/mozJpeg", None))
#if QT_CONFIG(tooltip)
        self.autoLevelBox.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head /><body><p>\u5c06\u6700\u5e38\u89c1\u7684\u6697\u50cf\u7d20\u503c\u8bbe\u7f6e\u4e3a\u9010\u9875\u8c03\u5e73\u7684\u9ed1\u70b9.</p><p>\u8df3\u8fc7\u4efb\u4f55\u6700\u521d\u4e3a\u5f69\u8272\u7684\u56fe\u50cf.</p><p>\u4ec5\u5f53\u9ed8\u8ba4\u81ea\u52a8\u5316\u5bf9\u4f8b\u4ecd\u7136\u4f1a\u5bfc\u81f4\u975e\u5e38\u7070\u8272\u7684\u9ed1\u8272\u65f6\u4f7f\u7528. </p><p>\u5efa\u8bae\u4e0e\u81ea\u5b9a\u4e49\u4f3d\u9a6c= 1.0\u4e00\u8d77\u4f7f\u7528\uff08\u7981\u7528\uff09.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.autoLevelBox.setText(QCoreApplication.translate("mainWindow", u"\u6fc0\u8fdb\u7684\u9ed1\u70b9", None))
        self.gammaLabel.setText(QCoreApplication.translate("mainWindow", u"Gamma: Auto", None))
#if QT_CONFIG(tooltip)
        self.chunkSizeWidget.setToolTip(QCoreApplication.translate("mainWindow", u"<html><head/><body><p>Warning: chunk size greater than default may cause<br/>performance/battery issues, especially on older devices.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chunkSizeLabel.setText(QCoreApplication.translate("mainWindow", u"\u5206\u5757 MB:", None))
        self.chunkSizeWarnLabel.setText(QCoreApplication.translate("mainWindow", u"\u5927\u4e8e\u9ed8\u8ba4\u503c\u53ef\u80fd\u4f1a\u5bfc\u81f4\u65e5\u7248\u9605\u8bfb\u5668\u51fa\u73b0\u6027\u80fd\u95ee\u9898\u3002", None))
    # retranslateUi


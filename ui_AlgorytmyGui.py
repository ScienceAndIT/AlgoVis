# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlgorytmyGui.ui'
#
# Created: Thu Jul 04 16:06:18 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 596)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.webView = QtWebKit.QWebView(self.tab)
        self.webView.setToolTip(_fromUtf8(""))
        self.webView.setStatusTip(_fromUtf8(""))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout.addWidget(self.webView)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.webView2 = QtWebKit.QWebView(self.tab_2)
        self.webView2.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView2.setObjectName(_fromUtf8("webView2"))
        self.horizontalLayout_2.addWidget(self.webView2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpcje = QtGui.QMenu(self.menubar)
        self.menuOpcje.setObjectName(_fromUtf8("menuOpcje"))
        self.menuZapisz_jako = QtGui.QMenu(self.menuOpcje)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuZapisz_jako.setIcon(icon1)
        self.menuZapisz_jako.setObjectName(_fromUtf8("menuZapisz_jako"))
        self.menuEdycja = QtGui.QMenu(self.menubar)
        self.menuEdycja.setObjectName(_fromUtf8("menuEdycja"))
        self.menuPomoc = QtGui.QMenu(self.menubar)
        self.menuPomoc.setObjectName(_fromUtf8("menuPomoc"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.libDockWidget = QtGui.QDockWidget(MainWindow)
        self.libDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.libDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.libDockWidget.setObjectName(_fromUtf8("libDockWidget"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.line = QtGui.QFrame(self.dockWidgetContents_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.libTree = QtGui.QTreeWidget(self.dockWidgetContents_4)
        self.libTree.setHeaderHidden(True)
        self.libTree.setObjectName(_fromUtf8("libTree"))
        item_0 = QtGui.QTreeWidgetItem(self.libTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout_3.addWidget(self.libTree)
        self.libDockWidget.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.libDockWidget)
        self.inputDockWidget = QtGui.QDockWidget(MainWindow)
        self.inputDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.inputDockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.inputDockWidget.setObjectName(_fromUtf8("inputDockWidget"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.dockWidgetContents_5)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.optionsTabWidget = QtGui.QTabWidget(self.frame)
        self.optionsTabWidget.setObjectName(_fromUtf8("optionsTabWidget"))
        self.optionsTab1 = QtGui.QWidget()
        self.optionsTab1.setObjectName(_fromUtf8("optionsTab1"))
        self.optionsTabWidget.addTab(self.optionsTab1, _fromUtf8(""))
        self.optionsTab2 = QtGui.QWidget()
        self.optionsTab2.setObjectName(_fromUtf8("optionsTab2"))
        self.optionsTabWidget.addTab(self.optionsTab2, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.optionsTabWidget)
        self.verticalLayout.addWidget(self.frame)
        self.runButton = QtGui.QPushButton(self.dockWidgetContents_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/3d graph.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon2)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.verticalLayout.addWidget(self.runButton)
        self.inputDockWidget.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.inputDockWidget)
        self.zamknijAction = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zamknijAction.setIcon(icon3)
        self.zamknijAction.setWhatsThis(_fromUtf8(""))
        self.zamknijAction.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.zamknijAction.setObjectName(_fromUtf8("zamknijAction"))
        self.nowyAction = QtGui.QAction(MainWindow)
        self.nowyAction.setObjectName(_fromUtf8("nowyAction"))
        self.aboutAction = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutAction.setIcon(icon4)
        self.aboutAction.setMenuRole(QtGui.QAction.AboutRole)
        self.aboutAction.setObjectName(_fromUtf8("aboutAction"))
        self.pomocAction = QtGui.QAction(MainWindow)
        self.pomocAction.setObjectName(_fromUtf8("pomocAction"))
        self.renameAction = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renameAction.setIcon(icon5)
        self.renameAction.setObjectName(_fromUtf8("renameAction"))
        self.gifAction = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/gif.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gifAction.setIcon(icon6)
        self.gifAction.setObjectName(_fromUtf8("gifAction"))
        self.mpegAction = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/mpeg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpegAction.setIcon(icon7)
        self.mpegAction.setObjectName(_fromUtf8("mpegAction"))
        self.menuZapisz_jako.addAction(self.gifAction)
        self.menuZapisz_jako.addAction(self.mpegAction)
        self.menuOpcje.addAction(self.nowyAction)
        self.menuOpcje.addAction(self.menuZapisz_jako.menuAction())
        self.menuOpcje.addAction(self.zamknijAction)
        self.menuEdycja.addAction(self.renameAction)
        self.menuPomoc.addAction(self.pomocAction)
        self.menuPomoc.addAction(self.aboutAction)
        self.menubar.addAction(self.menuOpcje.menuAction())
        self.menubar.addAction(self.menuEdycja.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.optionsTabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.zamknijAction, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Wizualizacja algorytmów", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.menuOpcje.setTitle(_translate("MainWindow", "Opcje", None))
        self.menuZapisz_jako.setToolTip(_translate("MainWindow", "Zapisz jako...", None))
        self.menuZapisz_jako.setStatusTip(_translate("MainWindow", "Wybierz format zapisu", None))
        self.menuZapisz_jako.setTitle(_translate("MainWindow", "Zapisz jako ...", None))
        self.menuEdycja.setTitle(_translate("MainWindow", "Edycja", None))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc", None))
        self.libDockWidget.setWindowTitle(_translate("MainWindow", "Biblioteka algorytmów", None))
        self.libTree.headerItem().setText(0, _translate("MainWindow", "1", None))
        __sortingEnabled = self.libTree.isSortingEnabled()
        self.libTree.setSortingEnabled(False)
        self.libTree.topLevelItem(0).setText(0, _translate("MainWindow", "Sortowanie", None))
        self.libTree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Quick Sort", None))
        self.libTree.setSortingEnabled(__sortingEnabled)
        self.inputDockWidget.setWindowTitle(_translate("MainWindow", "Parametry wejściowe", None))
        self.optionsTabWidget.setTabText(self.optionsTabWidget.indexOf(self.optionsTab1), _translate("MainWindow", "Tab 1", None))
        self.optionsTabWidget.setTabText(self.optionsTabWidget.indexOf(self.optionsTab2), _translate("MainWindow", "Tab 2", None))
        self.runButton.setStatusTip(_translate("MainWindow", "Uruchamia wizualizację z wybranymi parametrami wejściowymi", None))
        self.runButton.setText(_translate("MainWindow", "Uruchom", None))
        self.zamknijAction.setText(_translate("MainWindow", "Zamknij", None))
        self.zamknijAction.setIconText(_translate("MainWindow", "Zamknij", None))
        self.zamknijAction.setToolTip(_translate("MainWindow", "Zamknij", None))
        self.zamknijAction.setStatusTip(_translate("MainWindow", "Kończy działanie aplikacji", None))
        self.nowyAction.setText(_translate("MainWindow", "Nowy", None))
        self.aboutAction.setText(_translate("MainWindow", "O programie", None))
        self.aboutAction.setStatusTip(_translate("MainWindow", "Wyświetla okno z informacją o programie", None))
        self.pomocAction.setText(_translate("MainWindow", "Pomoc", None))
        self.renameAction.setText(_translate("MainWindow", "Zmień nazwę", None))
        self.renameAction.setStatusTip(_translate("MainWindow", "Zmienia nazwę algorytmu", None))
        self.gifAction.setText(_translate("MainWindow", "GIF", None))
        self.gifAction.setStatusTip(_translate("MainWindow", "Zapisuje wizualizację w pliku GIF", None))
        self.mpegAction.setText(_translate("MainWindow", "MPEG", None))
        self.mpegAction.setStatusTip(_translate("MainWindow", "Zapisuje wizualizację w pliku MPEG", None))

from PyQt4 import QtWebKit
import icons_rc

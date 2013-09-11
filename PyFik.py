# -*- coding: utf-8 -*-

#
#	Autor: Paweł FIK
#	Akademia Marynarki Wojennej
#
#	ver. 0.0.3 - 04.07.2013
#

import os
import os.path
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from platform import python_version, system
import shutil
import random
import PIL
import matplotlib
from visualization.makeGif import *
from algorytmy import algorytmy
import ui_AlgorytmyGui

__version__ = "0.0.3 04.07.2013"


class PyFik(QMainWindow, ui_AlgorytmyGui.Ui_MainWindow):
				
		def __init__(self, parent=None):
				"""Inicjalizuje okno główne aplikacji 
				"""
				super(PyFik,self).__init__(parent)
				self.setupUi(self)
							
				self.algDir = 'algorytmy'
				self.confFilePath = os.path.join(self.algDir,'algorytmy.conf')
				self.helpFile = os.path.join('help','index.html')
								
				
				self.initialView()
				
				self.selectedAlg = None
				self.connect(self.libTree, SIGNAL("itemClicked(QTreeWidgetItem*,int)"), self.algInput)
				
				self.connect(self.runButton, SIGNAL("clicked()"), self.updateWebView)
				
				
				#Menu actions
				self.connect(self.mpegAction, SIGNAL("triggered()"), self.saveMpeg)
				self.connect(self.gifAction, SIGNAL("triggered()"), self.saveGif)
				self.connect(self.renameAction, SIGNAL("triggered()"), self.renameItem)
				self.connect(self.aboutAction, SIGNAL("triggered()"), self.showAbout)
				
				
		def inputList(self):
				"""Generuje wejściową listę argumentów
				"""
				listSize = 20
				inputList = range(listSize)
				random.shuffle(inputList)
				return inputList[:]
		
		def initialView(self):
				"""Ustawia początkowy wygląd aplikacji:
				* ukrywa okno parametrów wejściowych
				* wczytuje bibliotekę algorytmów z pliku algorytmy.conf
				* tworzy ToolBar z ikonami przedstawiającymi główne funkcje aplikacji
				
				"""
				self.createToolBar()
				self.updatelibTree()
				self.inputDockWidget.hide()
								
				self.statusBar().showMessage("Gotowe")
				
		def updatelibTree(self,separator=';'):
				"""Wczytuje plik konfiguracyjny algorytmy.conf
				i uaktualnia bibliotekę algorytmów.
				"""
				self.confFile = []
				try:
						file = open(self.confFilePath)
						lines = file.readlines()
						file.close()
						for line in lines:
								if line !='\n':
										self.confFile.append(line.strip('\n').split(separator))
				except IOError:
						pass

				self.libTree.clear()

				sections = set([self.confFile[i][0] for i in range(len(self.confFile))])
				for section in sections:
						algTypeItem = QTreeWidgetItem(None, QStringList(section))
						self.libTree.addTopLevelItem(algTypeItem)
						self.libTree.expandItem(algTypeItem)
						algTypeItem.setFlags(Qt.ItemIsEnabled)
						algTypeWidget = QTreeWidget(self.libTree.itemWidget(algTypeItem,1))

						for i in range(len(self.confFile)):
								if self.confFile[i][0] == section:
										children  = self.confFile[i][1]
										algTypeWidget.addTopLevelItem(QTreeWidgetItem(algTypeItem, QStringList(children)))
				self.sections = sections
				
		def createToolBar(self):
				"""Tworzy ToolBar z ikonami przedstawiającymi
				główne funkcje aplikacji
				"""
				self.mainToolBar = self.addToolBar("Main")
				self.mainToolBar.addAction(self.renameAction)
				self.mainToolBar.addAction(self.gifAction)
				self.mainToolBar.addAction(self.mpegAction)
				
				self.optionalToolBar = self.addToolBar("Optional")
				self.optionalToolBar.addAction(self.zamknijAction)
				self.optionalToolBar.addAction(self.aboutAction)
				
		def updateWebView(self):
				"""Ładuje utworzony GIF do webView
				"""
				self.gifFileName = "temp.gif"		
				algorytmy.bubbleSort(self.inputList())
				makeGIF(self.gifFileName)
				self.webView.setUrl(QUrl(self.gifFileName))

		def showAbout(self):
				"""Otwiera okno zawierające podstawowe informacje o aplikacji.
				"""
				QMessageBox.information(self, "O Programie",
					"""<b>Wizualizacja Algorytmow</b> v %s
					<p>Program do wizualizacji przebiegu wybranych algorytmow.
					<p>Copyright &copy; 2013. 
					Pawel FIK.
					<p>Python %s -Qt %s -PyQt %s 
					<p>-PIL %s -matplotlib %s on %s"""
					% (__version__,python_version(),QT_VERSION_STR,PYQT_VERSION_STR, Image.VERSION, matplotlib.__version__, system()))
			
		def renameItem(self):
				"""Zmienia nazwę wybranego algorytmu w Bibliotece Algorytmów
				"""
				currItem = self.libTree.currentItem()
				if currItem:
					if currItem.childCount() == 0:
						itemName = str(self.libTree.currentItem().text(0))
						(newName,reply) = QInputDialog.getText(self,u"Zmień nazwę","Nowa nazwa:",
							QLineEdit.Normal,itemName)
						newName = newName.trimmed()
						if reply and newName != itemName:
							if len([i for i in range(len(self.confFile)) if newName in [self.confFile[i][1]]])==0:
								el = [i for i in range(len(self.confFile)) if itemName in [self.confFile[i][1]]][0]
								self.confFile[el][1] = newName
								self.saveConfFile()
							else:
								QMessageBox(QMessageBox.Warning, u"Uwaga", u"Nazwa została już użyta.").exec_()
					else:
						typeName = str(self.libTree.currentItem().text(0))
						(newType,reply) = QInputDialog.getText(self, u"Zmień nazwę","Nowa nazwa:",
							QLineEdit.Normal,typeName)
						newType = newType.trimmed()
						if reply and newType != typeName:
							if len([i for i in range(len(self.confFile)) if newType in [self.confFile[i][0]]])==0:
								for i in range(len(self.confFile)):
									if typeName in [self.confFile[i][0]]:
										self.confFile[i][0] = newType
								self.saveConfFile()
				else:
					QMessageBox(QMessageBox.Warning, u"Uwaga", "Nie wybrano algorytmu.").exec_()  
					
		def algInput(self, item):
				"""Pokazuje parametry wejściowe wybranego algorytmu 
				do ustawienia.
				"""
				#Nie skończone
				itemParent = item.parent()
				if itemParent is not None:
					if self.selectedAlg is not item:
						self.webView.setUrl(QUrl('about:blank'))
						self.inputDockWidget.show()
			
				else:
					self.webView.setUrl(QUrl('about:blank'))
					self.selectedAlgorithm = item
					self.inputDockWidget.hide()
					
		def saveGif(self):
				QMessageBox(QMessageBox.Warning, u"Uwaga", "Working in progress...").exec_()
					
		def saveMpeg(self):
				QMessageBox(QMessageBox.Warning, u"Uwaga", "Working in progress...").exec_()
		
		def saveConfFile(self):
				"""Zapisuje aktualny stan Biblioteki Algorytmów do pliku
				konfiguracyjnego i jednocześnie ją uaktualnia w apliacji
				"""
				with open(self.confFilePath,'w') as file:
					for i in range(len(self.confFile)):
						file.write(self.confFile[i][0]+';'+self.confFile[i][1]+';'+self.confFile[i][2]+'\n')
				self.updatelibTree()
						
if __name__ == "__main__":
		import sys
		app = QApplication(sys.argv)
		app.setApplicationName(u"Wizualizacja algorytmów")
		form = PyFik()
		form.show()
		app.exec_()